
from easygui import *
import sys
sum=0
while 1:
    
    msgbox("Hello dear customer , WELCOME TO AMAZEKART !")

    msg ="What are you looking for?"
    title = "AMAZEKART"
    choices = ["SHOES", "TSHIRTS", "MOBILES"]
    choice = indexbox(msg, title, choices)
    
    if choice==0:
       msg="Choose the following Brands"
       title="SHOES"
       choices = ['NIKE','BATA','PUMA']
       choice= indexbox(msg,title,choices)
       if choice==0:
            msg="Choose the following vendors"
            title="NIKE"
            choices = ['PAPPU SALES','TAPPU SALES','BAPPU SALES']
            choice= indexbox(msg,title,choices)
            if choice==0:
             sum+=500
             textbox(sum,"your total bill is")
            
            elif choice==1:
             sum+=700
             textbox(sum,"your total bill is")
           
            elif choice==2:
             sum+=900
             textbox(sum,"your total bill is")
       
       elif choice==1:
            msg="Choose the following vendors"
            title="BATA"
            choices = ['PAPPU SALES','TAPPU SALES','BAPPU SALES']
            choice= indexbox(msg,title,choices)
            if choice==0:
             sum+=500
             textbox(sum,"your total bill is")
            
            elif choice==1:
             sum+=700
             textbox(sum,"your total bill is")
           
            elif choice==2:
             sum+=900
             textbox(sum,"your total bill is")
  
       elif choice==2:
            msg="Choose the following vendors"
            title="PUMA"
            choices = ['PAPPU SALES','TAPPU SALES','BAPPU SALES']
            choice= indexbox(msg,title,choices)
            if choice==0:
             sum+=500
             textbox(sum,"your total bill is")
            
            elif choice==1:
             sum+=700
             textbox(sum,"your total bill is")
           
            elif choice==2:
             sum+=900
             textbox(sum,"your total bill is")
     
      
    if choice==1:
       msg="Choose the following Brands"
       title="TSHIRTS"
       choices = ['NIKE','ADIDAS','PUMA']
       choice= indexbox(msg,title,choices)
       if choice==0:
            msg="Choose the following vendors"
            title="NIKE"
            choices = ['PAPPU SALES','TAPPU SALES','BAPPU SALES']
            choice= indexbox(msg,title,choices)
            if choice==0:
             sum+=5000
             textbox(sum,"your total bill is")
            
            elif choice==1:
             sum+=7000
             textbox(sum,"your total bill is")
           
            elif choice==2:
             sum+=9000
             textbox(sum,"your total bill is")
       
       elif choice==1:
            msg="Choose the following vendors"
            title="ADIDAS"
            choices = ['PAPPU SALES','TAPPU SALES','BAPPU SALES']
            choice= indexbox(msg,title,choices)
            if choice==0:
             sum+=5005
             textbox(sum,"your total bill is")
            
            elif choice==1:
             sum+=7006
             textbox(sum,"your total bill is")
           
            elif choice==2:
             sum+=9007
             textbox(sum,"your total bill is")
  
       elif choice==2:
            msg="Choose the following vendors"
            title="PUMA"
            choices = ['PAPPU SALES','TAPPU SALES','BAPPU SALES']
            choice= indexbox(msg,title,choices)
            if choice==0:
             sum+=5000
             textbox(sum,"your total bill is")
            
            elif choice==1:
             sum+=7000
             textbox(sum,"your total bill is")
           
            elif choice==2:
             sum+=9000
             textbox(sum,"your total bill is")


    if choice==2:
       msg="Choose the following Brands"
       title="MOBILE PHONES"
       choices = ['APPLE','GOOGLE','SAMSUNG']
       choice= indexbox(msg,title,choices)
       if choice==0:
            msg="Choose the following vendors"
            title="APPLE"
            choices = ['PAPPU SALES','TAPPU SALES','BAPPU SALES']
            choice= indexbox(msg,title,choices)
            if choice==0:
             sum+=85000
             textbox(sum,"your total bill is")
            
            elif choice==1:
             sum+=88000
             textbox(sum,"your total bill is")
           
            elif choice==2:
             sum+=90000
             textbox(sum,"your total bill is")
       
       elif choice==1:
            msg="Choose the following vendors"
            title="GOOGLE"
            choices = ['PAPPU SALES','TAPPU SALES','BAPPU SALES']
            choice= indexbox(msg,title,choices)
            if choice==0:
             sum+=75000
             textbox(sum,"your total bill is")
            
            elif choice==1:
             sum+=70000
             textbox(sum,"your total bill is")
            
            elif choice==2:
             sum+=78000
             textbox(sum,"your total bill is")
  
       elif choice==2:
            msg="Choose the following vendors"
            title="SAMSUNG"
            choices = ['PAPPU SALES','TAPPU SALES','BAPPU SALES']
            choice= indexbox(msg,title,choices)
            if choice==0:
             sum+=15500
             textbox(sum,"your total bill is")
            
            elif choice==1:
             sum+=17000
             textbox(sum,"your total bill is")
           
            elif choice==2:
             sum+=19000
             textbox(sum,"your total bill is")
     
       
          

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):    
        pass 
    else:
sys.exit(0)
