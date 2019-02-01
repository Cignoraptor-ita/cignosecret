#canaccio
import sys, os, webbrowser, platform
import time
import webbrowser

def __limpiar():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')
def menu():
	__limpiar()
			
	print "****||||CIGNOSECRET ==****|||| "
        print '''
		CIGNOSECRET
	'''
	print "LIVELLO 8"
	
	d = raw_input("NAME AND SURNAME OF THE PERSON WHO USE THIS EMAIL ----> 344ris@mailzi.ru (EX: Ippolito Senderoti : ")
	if d == "Francesco Zorin":
		print "SUCCESS!"
		time.sleep(2)
	
	else:
		print "NO!"
                time.sleep(2)
                menu()
def main():
	menu()
if __name__ == '__main__':
	main()
