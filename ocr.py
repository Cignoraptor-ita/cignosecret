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
                LIVELLO 5
	'''
	d = raw_input("NAME OF THE GOOSE IN ocar.jpeg? (In lower case): ")
	if d == "becco di rame":
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
