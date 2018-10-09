def ArmN(x):                        #function declaration
  sum=0
  t=x
  
  while(t>0):                       #while loop starts
    d=t%10                          #extracts last digit
    sum=sum+(d**3)                  #adds the cube
    t=t//10                         #removes remaining digits aside

  if sum==x:                        #checks sum with initial number
    print("Armstrong number")       #prints if condition true
  else:
    print("Not an armstrong number")#prints if condition false

x=int(input(" Enter a number"))     # accepts number from user
ArmN(x)                             #function call
  
