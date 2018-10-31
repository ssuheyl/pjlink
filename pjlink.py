from pypjlink import Projector
from pypjlink.cliutils import make_command, print_error
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
power=31
src1=33
src2=35
src3=37

GPIO.setup(power, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(src1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(src2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(src3, GPIO.IN, pull_up_down=GPIO.PUD_UP)




def main():
    host='172.16.24.70'
    port=4352
    password='admin'
    #port, password = resolve_projector(projector)

    #if not password:
        #password = getpass
    try: 
    	proj = Projector.from_address(host, port)
    	rv = proj.authenticate(password)
    	if rv is False:
        	print_error('Incorrect password.')
        	return
    except:
	pass
    #print proj.get_power()	
    while True:
	input_state1=GPIO.input(power)
	input_state2=GPIO.input(src1)
	input_state3=GPIO.input(src2)
	input_state4=GPIO.input(src3)
	if input_state1 == False:
		stat = "stf"
		try:
			if proj.get_power()  is not None:
				stat = proj.get_power()
				print stat
		except:
			try:
				proj = Projector.from_address(host, port)
				rv = proj.authenticate(password)
			except:
				pass
			print "impossible"
		if stat=="on":
			proj.set_power("off")
		elif stat=="off":
			proj.set_power("on")		
	elif input_state2 == False:
		try:
			proj.set_input("RGB",1)
		except:
			pass
        elif input_state3 == False:
		try:
			proj.set_input("RGB",2)
		except:
			pass
	elif  input_state4 == False:
		try:
			proj.set_input("NETWORK",2)
		except:
			print "hata"
	time.sleep(1)		
#print proj.get_power()


if __name__ == '__main__':
    main()

