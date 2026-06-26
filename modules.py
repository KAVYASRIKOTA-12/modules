#math module
import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,2))
print(math.log(10))
print(math.sin(30))
print(math.cos(30))
print(math.tan(45))
print(math.ceil(6.9))
print(math.ceil(0.5))
print(math.floor(4.9))
print(math.factorial(12))

3example
from math import pi,sqrt,log
print(pi)
print(sqrt(4))
print(log(20))


#sys module
#ex 1
import sys
print(sys.path)

#ex 2
import sys
for i in sys.path:  #to print in different lines
    print(i)

#ex 3
import sys
print(sys.version)


#os module
import os
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.mkdir("may25"))
print(os.chdir("C:\\Users\\Kavya\\Downloads"))
print(os.listdir())


#random module
#To generate the random number in python , randinit function is used this function is defined in random module.
#Python defines a set of functions that are used to generate or manipulate random numbers through the module.
import random
a=random.sample(range(10,40),5)
print(a)
#randint()
import random
a=random.randint(20,50) #to print single number
print(a)
#choice()
import random
a=[10,20,30,40,50]
b=random.choice(a)  #to print assigned numbers
print(b)


#task
import random
a=int(input("enter the roll of dice"))
b=random.randint(1,7)

#calendar module
#ex 1
import calendar
year=2026
month=6
print(calendar.month(year,month))

#ex 2
import calendar
year=2026
print(calendar.calendar(year))

#ex 3
import calendar
year=int(input("year"))
month=int(input("month"))
print(calendar.month(year,month))

#date & time
from datetime import date
a=date.today()
print(a)

import datetime
a=datetime.datetime.now()
print(a)

#time
import time
a=time.time()
print(a)      #epoch time

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")

print(f"day is {b.tm_yday}-{b.tm_wday}-{b.tm_isdst}")



#error handling
#1.syntax error->compile error
#2.runtime error->during execution time
#3.logical error->error in logic(it cant visible)

#syntax error
for i in range(10):
print(a)

#runtime error
a=int(input("a value"))
b=int(input("b value"))
print(a/b)

#logical error
a=10
if a<5:
    print("true")



#exception handling
#1.try->instructions from which we are expecting the exceptions.
#2.except->exception is raised in try block.It will be handle by this block.
#3.error->optional(no exceptions).
#4.finally->(always).
while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exceptions raised")
    else:
        print("no exceptions")
    finally:
        print("program ends......")

#task
#dice code
import random
while True:
    input("enter the roll of dice")
    a=random.randint(1,6)
    print(a)
    option=input("roll again?(y/n)")
    if option=="y":
        continue
    elif option=="n":
        break
    else:
        print("invalid option")

#task
import random
import time
for i in range(10):
    a=random.randint(20,50)
    print(a)
    time.sleep(2)

#regex methods->compile(),search(),findall(),split(),sub()
#sequence characters:
#\w->it matches alphanumeric
#\W->it matches non-alphanumeric
#\d->it matches any digit
#\D->it matches non-digit
#\s->it represents white spaces
#\S->it represents non-white spaces

#compile()
import re
a="code map maths cash money cup monkey cap mug"
b=re.compile(r"m\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)

#to print a single word that starts with m letter
import re
a="code map maths cash money cup monkey cap mug"
c=re.search(r"m\w+",a)
print(c)   


#findall()
#to print all m letter words
import re
a="code map maths cash money cup monkey cap mug"
d=re.findall(r"m\w+",a)
print(d)   

#to print all c letter words
import re
a="code map maths cash money cup monkey cap mug"
d=re.findall(r"c\w+",a)
print(d)


#split()
 #to split m from m letter words
import re
a="code map maths cash money cup monkey cap mug"
b=re.split(r"m",a)  
print(b)
#to remove white spaces
c=re.split(r"\s",a)  
print(c)

#sub()
#ex 1
import re
a="code map maths cash money cup monkey cap mug"
b=re.sub(r"m","k",a)
print(b)

#ex 2
#to print all digits in given data 
import re
a="python java 23 87 money 98 cake 53"
b=re.findall(r"\d+",a)   
print(b)



