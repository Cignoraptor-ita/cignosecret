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
	print "LIVELLO 11"
	
	d = raw_input("IN code.cigno THERE IS A DISPOSITION THAT WAS SIGNED BY?(case sensitive): ")
	if d == "The duck army":
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
