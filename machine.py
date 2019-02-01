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
                LIVELLO 7
	'''
	d = raw_input("FILENAME (without extension) OF THE IMAGE IN THE LEFT OF THE TEXT, APPEAR THE  10 feb 2010 IN AGRARIA.ORG: ")
	if d == "homehighland":
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
