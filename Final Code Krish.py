# Start of Imports

from tkinter import *
from tkinter import messagebox


# End of Imports


# over here you can see iam setting up the main class that holds the events such as the points, events and winners
class HouseEvent:
    def __init__(self, eventname, eventtype, pointsforred, pointsforblue, pointsgreen, pointsforyellow, thewinnner):
        self.eventname = eventname
        self.eventtype = eventtype
        self.pointsforred = int(pointsforred)
        self.pointsforblue = int(pointsforblue)
        self.pointsgreen = int(pointsgreen)
        self.pointsforyellow = int(pointsforyellow)
        self.thewinnner = thewinnner

        houseevents.append(self)
        houseeventsnames.append(eventname)

    # this part is a function which holds the vaule for my tickbox
    confirmpoint1 = False

    def printinfo(self):
        # these if and else statements determines if the event being played is an sports or not a sports
        if self.eventtype:
            isitasport = "This Event is a Sport"
        else:
            isitasport = "This Event isn't a Sport"
        # ive got these infoprint statments sorted for each house and the points they have
        infoprint = "For the Event: " + self.eventname + "\n" + isitasport + "\nThe Points Earned by RED are: " + str(
            self.pointsforred) + "\nThe Points Earned by BLUE are: " + str(
            self.pointsforblue) + "\nThe Points Earned by GREEN are: " + str(
            self.pointsgreen) + "\nThe Points Earned by YELLOW are: " + str(
            self.pointsforyellow) + "\nThe thewinnner of this Event was: " + self.thewinnner
        # lastly in this peice of code it returns these statement to the message box for printing on display events
        return infoprint


# the code over here is another funtion that finds the house event that the user wants to see the infomation of and calls to the printinfo funtion that
# makes the message, then puts it into a messagebox for the user to see visually

def displayinfo():
    for house_event in houseevents:
        if selectedview.get() == house_event.eventname:
            messagebox.showinfo("House Event Information", house_event.printinfo())

#the code over is another function that adds up the scores for each of the houses

def addfuntion(housecolour):
    sumofred = 0
    sumofblue = 0
    sumofyellow = 0
    sumofgreen = 0
    for house_event in houseevents:
        sumofred = house_event.pointsforred + sumofred
        sumofblue = house_event.pointsforblue + sumofblue
        sumofyellow = house_event.pointsforyellow + sumofyellow
        sumofgreen = house_event.pointsgreen + sumofgreen

    if housecolour == "red":
        return sumofred
    elif housecolour == "blue":
        return sumofblue
    elif housecolour == "yellow":
        return sumofyellow
    elif housecolour == "green":
        return sumofgreen


#this leaderborad fucntion sorts the houses and its scores into a list that then sorts it from lowest to higest points
#it is a tricky peice of code but it seems to work :)
def leaderboard():
    def custom_sort(t):
        return t[1]

    standings = [("Red", addfuntion("red")), ("Blue", addfuntion("blue")), ("Green", addfuntion("green")),
                 ("Yellow", addfuntion("yellow"))]
    standings.sort(key=custom_sort)
    standingsprint = "First place with " + str(standings[3][1]) + " is " + standings[3][
        0] + "\nSecond place with " + str(standings[2][1]) + " is " + standings[2][0] + "\nThird place with " + str(
        standings[1][1]) + " is " + standings[1][0] + "\nFourth place with " + str(standings[0][1]) + " is " + \
                     standings[0][0]
    return standingsprint


def thewinnnerofevent():
    def custom_sort(t):
        return t[1]

    standings = [("Red", pointsforredEntry.get()), ("Blue", pointsforblueEntry.get()),
                 ("Green", pointsgreenEntry.get()), ("Yellow", pointsforyellowEntry.get())]
    standings.sort(key=custom_sort)
    # checks to see if there is  a tie
    #though it is long it reduces total masses of code , doing it any other way will be inenficent
    if standings[3][1] == standings[2][1] and standings[3][1] == standings[1][1] and standings[3][1] == standings[0][1]:
        return str(standings[3][0]) + " Tied with " + str(standings[2][0]) + " Tied with " + str(
            standings[1][0]) + " Tied with " + str(standings[0][0])
    if standings[3][1] == standings[2][1] and standings[3][1] == standings[1][1]:
        return str(standings[3][0]) + " Tied with " + str(standings[2][0]) + " Tied with " + str(standings[1][0])
    elif standings[3][1] == standings[2][1]:
        return str(standings[3][0]) + " Tied with " + str(standings[2][0])
    else:
        return str(standings[3][0])


# down below is code that is functions used for making messageboxs for errors and success

def showleaderboard():
    messagebox.showinfo("House Placing", leaderboard())


def verifyevent():
    if not checkboxticked1.get():
        messagebox.showerror("Error", "Please check the confirm checkbox to show all your entries are correct.")
        return False

    event = eventnameEntry.get()
    if event.isnumeric():
        messagebox.showerror("Error", "Please enter a string (starting with an alphabet) for the event name")
        return
    if event == "":
        messagebox.showerror("Error", "Please enter the event name")
        return

    # this is for checking that only whole numbers are entered for the score therefore it rejects decimal places
    for i in (pointsforredEntry, pointsforblueEntry, pointsgreenEntry, pointsforyellowEntry):
        if not i.get().isnumeric():
            messagebox.showerror('Error', "Failure, Unable to create New Event. Please check that house points "
                                          "entered are numbers")
            return False

    eventsport = False
    if checkboxticked.get():
        eventsport = True
    HouseEvent(event, eventsport, pointsforredEntry.get(), pointsforblueEntry.get(),
               pointsgreenEntry.get(), pointsforyellowEntry.get(), thewinnnerofevent())
    return True

# this part funtion decides weather to make a success box or failure box, and if info is correct it runs refreshdropdown funtion to refresh the drop down to make sure it is updated with the new event
# and runs cleaerbox funtion to clear the entryboxes ready for a new event to be entered
def makeSuccessBox():
    messagebox.showinfo("Success", "New Event Has Been Entered")


def makeevent():
    if verifyevent():
        makeSuccessBox()
        refreshdropdown()
        clearbox()


# This message box is for errors

def makeFailureBox():
    messagebox.showinfo("Failure",
                        "Unable to create New Event. Please check that house points entered are numbers, and all required information is filled in")



# the prupose of this code is to refresh the dropdown menus for house event so when new infomation is added it will show up .
def refreshdropdown():
    houseeventsnames = []
    viewchoice.children["menu"].delete(0, "end")
    for h in houseevents:
        houseeventsnames.append(h.eventname)
        viewchoice.children["menu"].add_command(label=h.eventname, command=lambda b=h.eventname: selectedview.set(b))

def clearbox():
    eventnameEntry.delete(0, END)
    checkboxticked.set(0)
    pointsforredEntry.delete(0, END)
    pointsforblueEntry.delete(0, END)
    pointsgreenEntry.delete(0, END)
    pointsforyellowEntry.delete(0, END)


# these are my lists and objects
houses = ["Red", "Blue", "Green", "Yellow"]
houseevents = []
houseeventsnames = [""]


# GUI

# Creating the main window and setting some attributes so it looks nice
root = Tk()
root.geometry("750x650")
root.config(bg="black")
root.title("House Points Calculator")
root.tk_setPalette("black")

# Creating frames so that I can pack the widgets nicely and space everything evenly

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
frame6 = Frame(root)
frame7 = Frame(root)
frame8 = Frame(root)
frame9 = Frame(root)
frame10 = Frame(root)
frame11 = Frame(root)
frame12 = Frame(root)
frame13 = Frame(root)
frame14 = Frame(root)
frame15 = Frame(root)

# Creating a Title

titleLabel = Label(frame13, text="-------- Create New Event -------- \n", font=("Comic Sans MS", 20, "bold"))
titleLabel.pack()
titleLabel.config(bg="black")

# Making a place where user can create new events

# At the start of every block I make a label to tell the user what the input box/dropdown/tickbox is for. Then i make the box/dropdown/tickbox
# I will comment on the first block and anything new

# create a label
eventnameLabel = Label(frame1, text="Event Name")
# this part pushes it to the left side
eventnameLabel.pack(side=LEFT, padx=10)
# this part creates an entry box
eventnameEntry = Entry(frame1)
# this part makes it look nice
eventnameEntry.config(fg="BLACK", bg="#b0b0b0")
# this part pushes it to the right hand side
eventnameEntry.pack(side=RIGHT)

eventtypeLabel = Label(frame2, text="Is This Event A Sport?")
eventtypeLabel.pack(side=LEFT, padx=21)
# this part makes a checkbox
checkboxticked = IntVar()
eventtypeCheckbox = Checkbutton(frame2, variable=checkboxticked)
# this part pushes it to the right hand side
eventtypeCheckbox.pack(side=RIGHT)

pointsforredLabel = Label(frame3, text="Amount of points earned by Red house")
pointsforredLabel.pack(side=LEFT, padx=12)
pointsforredEntry = Entry(frame3)
pointsforredEntry.pack(side=RIGHT)
pointsforredEntry.config(fg="WHITE", bg="#ff2945")

pointsforblueLabel = Label(frame4, text="Amount of points earned by Blue house")
pointsforblueLabel.pack(side=LEFT, padx=11)
pointsforblueEntry = Entry(frame4)
pointsforblueEntry.pack(side=RIGHT)
pointsforblueEntry.config(fg="WHITE", bg="#2977ff")

pointsgreenLabel = Label(frame5, text="Amount of points earned by Green house")
pointsgreenLabel.pack(side=LEFT, padx=11)
pointsgreenEntry = Entry(frame5)
pointsgreenEntry.pack(side=RIGHT)
pointsgreenEntry.config(fg="BLACK", bg="#3dff4a")

pointsforyellowLabel = Label(frame6, text="Amount of points earned by Yellow house")
pointsforyellowLabel.pack(side=LEFT, padx=11)
pointsforyellowEntry = Entry(frame6)
pointsforyellowEntry.pack(side=RIGHT)
pointsforyellowEntry.config(fg="BLACK", bg="#fff53d")

# this part is for aligning things- you can ignore it
space1Label = Label(frame8, text="")
space1Label.pack()

# this part maks a button, and runs a command when it is pushed
addeventbutton = Button(frame8, text="Enter Event", command=makeevent)
# this part makes it look nice
addeventbutton.config(fg="BLACK", bg=("#87c783"), width=15, height=1, font=("Comic Sans MS", 13, "bold"))
# this part makes it apear on the screen
addeventbutton.pack()

title2Label = Label(frame14, text="\n -------- Show House Event Information -------- \n",
                    font=("Comic Sans MS", 20, "bold"))
title2Label.pack()

# this part makes a dropdown box/option menu
selectedview = StringVar()
viewLabel = Label(frame9, text="Select House Event Information To Display:    ")
viewLabel.pack(side=LEFT)
viewchoice = OptionMenu(frame9, selectedview, *houseeventsnames)
# this part makes the option menu/dropdown box look nice
viewchoice.config(width=17, fg="BLACK", bg="#b0b0b0")
# this part pushes it to the right hand side
viewchoice.pack(side=RIGHT)

spaceLabel = Label(frame10, text="")
spaceLabel.pack()
printinfobutton = Button(frame10, text="Display Event", command=displayinfo)
printinfobutton.config(fg="BLACK", bg="#87c783", width=15, height=1, font=("Comic Sans MS", 13, "bold"))
printinfobutton.pack()

leaderLabel = Label(frame11, text="\n -------- Leader Board -------- \n", font=("Comic Sans MS", 20, "bold"))
leaderLabel.pack()

leaderboardbutton = Button(frame12, text="Show Leader Board", command=showleaderboard,
                           font=("Comic Sans MS", 13, "bold"))
leaderboardbutton.config(fg="BLACK", bg="#87c783", width=15, height=1)
leaderboardbutton.pack()

ConfirmLabel = Label(frame15, text="Please Tick Box To Confirm Entry")
ConfirmLabel.pack(side=LEFT, padx=12)
# this part makes a checkbox
checkboxticked1 = IntVar()
ConfirmLabelCheckbox = Checkbutton(frame15, variable=checkboxticked1)
# this part pushes it to the right hand side
ConfirmLabelCheckbox.pack(side=RIGHT)

# this part packs the frames in the order I want so it looks nice, the ipadx is for alignment purposes
frame13.pack()
frame1.pack(ipadx=92)
frame2.pack(ipadx=142)
frame3.pack(ipadx=7)
frame4.pack(ipadx=6)
frame5.pack(ipadx=2)
frame6.pack(ipadx=1)
frame7.pack(ipadx=74)
frame15.pack(ipadx=112)
frame8.pack()
frame14.pack()
frame9.pack()
frame10.pack()
frame11.pack()
frame12.pack()
# End of GUI

# Run the program
root.mainloop()
