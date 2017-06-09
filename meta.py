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
			
	print "***||||CIGNOSECRET ==****|||| "
        print '''
		CIGNOSECRET
                LIVELLO 1
	'''
	d = raw_input("THE IMAGE moon.jpeg HAVE A GPS POSITION RECORD FROM? (ES: France): ")
	if d == "Ireland":
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
