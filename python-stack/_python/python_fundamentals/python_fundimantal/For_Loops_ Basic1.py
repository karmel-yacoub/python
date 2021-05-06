#1-Basic - Print all integers from 0 to 150
for x in range (0,151,1):
    print(x)
 #2-Multiples of Five 
for x in range (5,1001,5):
    print(x)
#3-Counting, the Dojo Way 
for i in range (1,101,1):
    if i%10==0:
        print ("coding Dojo")
        continue
    elif i%5==0:
        print ("coding")
        continue
    print (i)
    
#4-Whoa. That Sucker's Huge
Oddtotal = 0
for i in range(1,500000,2):
    Oddtotal += i
print(Oddtotal)

#5-Countdown by Fours
for i in range (2018,0,-4):
    print(i)

#6-Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,highNum+1):
    if i%mult == 0:
        print(i)

