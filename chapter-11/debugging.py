#raising an exception
"""try:
    x = dh4
except:
    raise Exception("x is not defined.because we have not assign any proper value to it.")"""

#getting the tracebake as a string
"""def spam():
    bacon()

def bacon():
    raise Exception("this is the error message.")

spam()"""

#import tracebake
import traceback
try:
    raise Exception("this is the error message.")
except:
    errorFile = open("D:/my_skills/dev/backend_roadmap/python/ABSP/chapter-11/myErrorFile.txt","w")
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The tracebake info was written to myErrorFile.txt.")

#Assertions
ages = [23,4,5,2,312,42,52,20]
print(ages[0] <= ages[-1])
ages.sort()
print(ages[0] <= ages[-1])

#using the logging module
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s-%(levelname)s-%(message)s")#when it will called by loggin.debug()it prints the information in the format specified
logging.debug("start of the program")#used toprint log information.it also calls the basicConfig()
def factorial(n):
    logging.debug("start of factorial(%s%%)" %n)
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug("i is " + str(i) + ",total is " + str(total))
    logging.debug("end of factorial (%s%%)" %n)
    return total 
print(factorial(6))
logging.debug("end of program")

#logging levels
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s -  %(message)s')
print(logging.debug('Some debugging details.'))
print(logging.info('The logging module is working.'))
print(logging.warning('An error message is about to be logged.'))
print(logging.error('An error has occurred.'))
print(logging.critical('The program is unable to recover!'))
print(logging.disable(logging.CRITICAL))