from tkinter import *
from time import *
from functools import partial;

#gets current time and updates display
def displayTime():
    currentTime = strftime("%I:%M:%S")
    currentDate = strftime("%m/%d/%Y")
    timeLabel.config(text=currentTime + "  " + currentDate, padx=5)
    root.after(200,displayTime) #set timer to redo function


#       ~~~~~~~~~~~~~~~setup stuff~~~~~~~~~~~~~~~
root = Tk(); #create window
#create window size
root.geometry("512x512")
#name window
root.title("NathOS");
#set bgcolor
root.configure(bg="yellow")



#Right clicks on desktop
def RightClickPos(event):

    #Desktop Color Change Menu
    def ChangeDesktopColor():
        def DesktopColorDestroy(event):
            DesktopColorOptionMenu.destroy();
        RightWindowDestroy(event) #get rid of rightclick window
        DesktopColorOptionMenu = Toplevel(root);
        DesktopColorOptionMenu.overrideredirect(1) #get rid of min/max buttons

        DesktopRedButton = Button(DesktopColorOptionMenu, text="Red", bg="#ff4242", fg="white", padx=20,pady=20, command=partial(DesktopColorRed, DesktopColorOptionMenu)).grid(row=0, column=0);
        DesktopGreenButton = Button(DesktopColorOptionMenu, text="Green", bg="#42ff84", fg="black", padx=20,pady=20, command=partial(DesktopColorGreen, DesktopColorOptionMenu)).grid(row=0, column=1);
        DesktopBlueButton = Button(DesktopColorOptionMenu, text="Blue", bg="#42a4ff", fg="white", padx=20,pady=20, command=partial(DesktopColorBlue, DesktopColorOptionMenu)).grid(row=0, column=2);
        DesktopYellowButton = Button(DesktopColorOptionMenu, text="yellow", bg="#fff942", fg="black", padx=20,pady=20, command=partial(DesktopColorYellow, DesktopColorOptionMenu)).grid(row=1, column=0);
        DesktopPurpleButton = Button(DesktopColorOptionMenu, text="purple", bg="#d342ff", fg="white", padx=20,pady=20, command=partial(DesktopColorPurple, DesktopColorOptionMenu)).grid(row=1, column=1);
        DesktopOrangeButton = Button(DesktopColorOptionMenu, text="orange", bg="#ffc042", fg="white", padx=20,pady=20, command=partial(DesktopColorOrange, DesktopColorOptionMenu)).grid(row=1, column=2);

        #position
        x = root.winfo_x()
        y = root.winfo_y()
        DesktopColorOptionMenu.geometry("+%d+%d" % (x+50, y+50))
        Desktop.bind("<Button-1>", DesktopColorDestroy)


        #desktop color change
    def DesktopColorRed(ColorMenu):
        Desktop.config(bg="#ff4242")
        ColorMenu.destroy()
    def DesktopColorGreen(ColorMenu):
        Desktop.config(bg="#42ff84")
        ColorMenu.destroy()
    def DesktopColorBlue(ColorMenu):
        Desktop.config(bg="#42a4ff")
        ColorMenu.destroy()
    def DesktopColorYellow(ColorMenu):
        Desktop.config(bg="#fff942")
        ColorMenu.destroy()
    def DesktopColorPurple(ColorMenu):
        Desktop.config(bg="#d342ff")
        ColorMenu.destroy()
    def DesktopColorOrange(ColorMenu):
        Desktop.config(bg="#ffc042")
        ColorMenu.destroy()
    


    #destroys the right window after use
    def RightWindowDestroy(event):
        RightWindow.destroy()
    #destroy on button press
    def RightWindowDestroyButton():
        RightWindow.destroy();

    def destroyTopdowns():
        for widget in root.winfo_children:
            if isinstance(widget, Toplevel):
                widget.destroy()

    #Main Right Window
    RightWindow = Toplevel(Desktop) #create new window
    
    Desktop.focus_set();
    RightWindowButton1 = Button(RightWindow, text="Color options", command=ChangeDesktopColor, pady=1, borderwidth=1, bg="#d1d1d1").pack(side=TOP, fill=X)
    RightWindowButton2 = Button(RightWindow, text="Open Files", pady=1, borderwidth=1, bg="#d1d1d1").pack(side=TOP, fill=X) 
    RightWindowButton3 = Button(RightWindow, text="Close", command=RightWindowDestroyButton, pady=1, borderwidth=1, bg="#d1d1d1").pack(side=TOP, fill=X)
    RightWindowButton4 = Button(RightWindow, text="Close All", command=destroyTopdowns, pady=1, borderwidth=1, bg="#d1d1d1").pack(side=TOP, fill=X)
    RightWindow.overrideredirect(1) #get rid of min/max buttons
    #set position
    x = root.winfo_x()
    y = root.winfo_y()
    RightWindow.geometry("+%d+%d" % (x + event.x, y + event.y))
     #Destory TopLevel on leftclick
    Desktop.bind('<Button-1>', RightWindowDestroy)
    #RightWindow.bind('<Leave>', RightWindowDestroy);


#create desktop frame
Desktop = Frame(root, bg="#42a4ff", width=512, height=512-25)
Desktop.bind("<Button-3>", RightClickPos) #call rightclick event
photo = PhotoImage(file = 'icon.png')
Game1 = Button(Desktop, text="Space Rocks", padx=5, pady=5, image=photo).pack
Desktop.pack()







#       ~~~~~~~~~~~~~~~toolbar~~~~~~~~~~~~~~~
toolbar = Frame(root, bg="#dedede", height=25);

#time
time = Frame(toolbar, bg="#dedede", width=150);
timeLabel = Label(time, text="time", bg="#dedede", fg="black")
timeLabel.pack(side=RIGHT, pady=5);
displayTime()



#button placeholders
FilesButton = Button(toolbar, text="Files", borderwidth=0);
FilesButton.pack(side=LEFT, padx=4,pady=2);
OtherButton = Button(toolbar, text="Button", borderwidth=0);
OtherButton.pack(side=LEFT, padx=4,pady=2);


#display toolbar
time.pack(side=RIGHT, fill=Y)
toolbar.pack(side=BOTTOM, fill=X);


#keep window running
root.mainloop()
