import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0,tk.END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents",".txt")])
    if file == "":
        file= None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0,tk.END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file == None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents",".txt")])
        if file == "":
            file=None
        else:
            #save as a new file
            f = open(file,"w")
            f.write(TextArea.get(1.0,tk.END))
            f.close()
            root.title(os.path.basename(file)+"- Notepad")
            print("File Saved")
    else:
        f = open(file,"w")
        f.write(TextArea.get(1.0,tk.END))
        f.close()
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","NotePad by Subhankit")
    
if __name__=="__main__":
    root=tk.Tk()
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("3.ico")
    root.geometry("644x788")
    #Add TextArea
    TextArea=tk.Text(root,font="lucida 13")
    file = None
    TextArea.pack(fill=tk.BOTH,expand=True)
    #Lets create a menubar
    Menubar = tk.Menu(root)
    #FileMenu Starts
    FileMenu= tk.Menu(Menubar,tearoff=0)
    #To open a new file
    FileMenu.add_command(label="New",command=newFile)
    #To open already exisiting file
    FileMenu.add_command(label="Open",command=openFile)
    #To save the current file
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    Menubar.add_cascade(label="File",menu=FileMenu)
    #Edit Menu Starts
    EditMenu=tk.Menu(Menubar,tearoff=0)
    #Feature of cut,copy,past
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    Menubar.add_cascade(label="Edit",menu=EditMenu)
    #Edit Menu Ends
    #Help Menu Starts
    HelpMenu=tk.Menu(Menubar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="Help",menu=HelpMenu)
    
    root.config(menu=Menubar)
    #Adding Scroll using rules from Tkinter lectures
    scroll=tk.Scrollbar(TextArea)
    scroll.pack(side=tk.RIGHT,fill=tk.Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)
    root.mainloop()
