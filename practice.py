from easygui import *
import sys
while 1:
    msgbox("Hello people!")

    msg ="What is your favorite subject?"
    title = "Subject Survey"
    choices = ["Calculus", "Python", "Electrical engineering", "Applied Science"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")

    msg = "BEST OF LUCK FOR END-SEM"
    title = "WISHESH"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
sys.exit(0)
