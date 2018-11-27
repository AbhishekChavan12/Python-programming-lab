from easygui import*
import sys

while 1:
      msgbox("Welocme to Numbers Check")

      msg="What would you like to check number for?"
      title="NUMBER FUN"
      choices=["PALINDROME","ARMSTRONG"]
      choice=buttonbox(msg,title,choices)

      msg="ENTER A NUMBER"
      num=int(enterbox(msg))

      if choice=="PALINDROME":
         n=0
         a=num
         while a>0:
           x=a%10
           n=(n*10) + x
           a=a//10

         if n==num:
            msgbox("PALINDROME NUMBER")
         else:
            msgbox("NOT A PALINDROME")
      else:
         n=0
         a=num
         while a>0:
           x=a%10
           n=(x*x*x) + n
           a=a//10

         if n==num:
            msgbox("ARMSTRONG NUMBER")
         else:
            msgbox("NOT ARMSTRONG NUMBER")
      msg="Play More"
      title="CONFIRMATION"
      if ccbox(msg,title):
         pass
      else:
         sys.exit(0)


