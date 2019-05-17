import re
import sys
import PySimpleGUI as sg
from tkinter import filedialog
from tkinter import *

#####################################
# The GUI which takes input of files
####################################
files = []
if len(sys.argv) == 1:
    event, (fname,) = sg.Window('My Script').Layout([[sg.Text('Document to open')],[sg.In(), sg.FileBrowse()],[sg.CloseButton('Open'), sg.CloseButton('Cancel')]]).Read()
else:
    fname = sys.argv[1]

if not fname:
    sg.Popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")

files.append(fname)
###########################################################
# Files that were input are to be analyzed in this section
##########################################################
f1 = open(files[0])
flag = 0

if f1 is None:
    sys.exit("Couldn't Open the file!")

def firstline(l):
    global flag
    if flag is 0:
        p = l.split("|")
        flag = 1
        #print(p)
    else:
        sys.exit("ERROR: Not a fasta File")

def sequence(l):
    global flag
    x = re.findall("[ATGC]", l)
    c = len(x)
    if l[-1] is '\n':
        c = len(x) + 1

    if c is len(l):
        flag = 0
    else:
        sys.exit("ERROR: Not a fasta File")

for l in f1:
    if l[0] == '>':
        firstline(l)
    else:
        sequence(l)

f1.seek(0,0)

###############################################################
#GUI to save the output file and To write into the output file
###############################################################
class DownloadButton:
    def __init__(self, master):
        master.geometry("400x200")
        #master.resizable(width=False,height=False)
        label1 = Label(master,text = "Download Window for processed FASTA File")
        frame = Frame(master)
        label = Label(master, text="The Fasta file is correct.\nPlease Save As and Quit to get the output file.",bd = 1,relief = "solid",font = "Times 16",width = 32,height = 4)
        label1.pack()
        label.pack()
        frame.pack()

        self.printButton = Button(frame, text="Save As", command=self.saveFile)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def saveFile(self):
        self.filename =  filedialog.asksaveasfilename(initialdir = "C:/Users/HP/code2/SElab",initialfile = "Output",title = "Select file",defaultextension=".txt",filetypes =[("All Files","*.*"),("Text Documents","*.txt")])
    	# Try to save the file
        f2 = open(self.filename,"w")
        f2.write("Sl No.\t\tInfo\t\t\t\t\t\t\t\t\t\t\t\t\tGene")
        count=1
        for l in f1:
            if l[0]=='>':
                f2.write("\n")
                c=str(count)
                f2.write(c)
                f2.write("\t\t")
                count=count+1
                flag1=1

            elif flag1==1:
                f2.write("\t\t\t")
                flag1=0
            if l[0]=='>':
                l=l[1:len(l)-1]
            else:
                l=l[0:len(l)-1]
            f2.write(l)

        label2 = Label(root,text = "Output File Created.\nPress Quit.")
        label2.pack()


root = Tk()
b = DownloadButton(root)
root.mainloop()
