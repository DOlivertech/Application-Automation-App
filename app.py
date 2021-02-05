import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',') #splits the text output of the app path's into an array
        apps = [x for x in tempApps if x.strip()]  #strips out the empty spaces left behind after opening the file browser but not selecting an app

def addApp():
    for widget in frame .winfo_children():        # When you add an additonal app, it destroys the reference to the previous app, avoiding duplication
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title="Select File",                  # This function opens a file dialogue at the / directory, displays " selection file" and shows/allows all executables 
    filetypes=(("executeables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:                                                     #this attaches the filename on screen within the frame
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)   # starts the file via the Run Apps button
 
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp) #add Apps button

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)   #runApps button

runApps.pack()

# deleteApps = tk.Button(root, text="Delete Apps(Non Working)", padx=10, pady=5, fg="white", bg="#263D42", #command=destroyApps)   #deleteApps button

# deleteApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()    #displays the saved apps on new startup

root.mainloop()




with open('save.txt', 'w') as f:        #whenever we close the app a text file gets saved, write to the text file all of the apps you previously selected
    for app in apps:
        f.write(app + ',')

