def ArmN(x):
  sum=0
  t=x
  
  while(t>0):
    d=t%10
    sum=sum+(d**3)
    t=t//10

  if sum==x:
    print("Armstrong number")
  else:
    print("Not an armstrong number")

x=int(input(" Enter a number"))
ArmN(x)
  
