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
                LIVELLO 2
	'''
	d = raw_input("0110121391 WHERE IS THE LOCATION OF THIS SPAM PHONE NUMBER? (IT --> EX:Firenze: ")
	if d == "Torino":
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
