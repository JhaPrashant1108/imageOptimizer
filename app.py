from imageOptimizer import *
import tkinter as tk
from tkinter import font,filedialog


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        appHighlightFont = font.Font(family='Helvetica', size=20)
        lable = tk.Label(self , text="",font=appHighlightFont)
        lable.pack()
        lable = tk.Label(self , text="",font=appHighlightFont)
        lable.pack()
        lable = tk.Label(self , text="",font=appHighlightFont)
        lable.pack()
        lable1 = tk.Label(self , text="imageOptimizer",font=appHighlightFont)
        lable1.pack()
      
        
        lable = tk.Label(self , text="",font=appHighlightFont)
        lable.pack()
        tk.Button(self, text="Single Image",
                  command=lambda: master.switch_frame(PageOne)).pack()
        lable = tk.Label(self , text="",font=appHighlightFont)
        lable.pack()
        lable = tk.Label(self , text="",font=appHighlightFont)
        lable.pack()
        tk.Button(self, text="Multiple Images",
                  command=lambda: master.switch_frame(PageTwo)).pack()
        

       
                 

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        appHighlightFont = font.Font(family='Helvetica', size=20)
        lbl1 = tk.Label(self,text="Select the path of image",font=appHighlightFont)
        button1 = tk.Button(self,text="Browse", command= lambda: self.browse_button())
        button2 = tk.Button(self, text="continue",command = lambda:[Downloader(data),data.clear(),master.switch_frame(FinishedPage)] if data else master.switch_frame(PageOne) )
        button3 = tk.Button(self,text="back" , command= lambda: master.switch_frame(StartPage))
        for i in (0,1,2,3,4,9,18,6,8,10,11,13,14,21,16,17,19,20,22,23,24,25):
            tk.Label(self,text="").grid(row=i,column=0)
        lbl1.grid(row=5)
        button1.grid(row=7)
        button2.grid(row=12)
        button3.grid(row=15)
        
 
    def browse_button(self):
        filename = filedialog.askopenfilename(filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        data.append(filename)
        data.append("")
        data.append('single')

        
        

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        appHighlightFont = font.Font(family='Helvetica', size=20)
        lbl1 = tk.Label(self,text="Select the path of image folder",font=appHighlightFont)
        button1 = tk.Button(self,text="Browse", command= lambda: self.browse_button())
        button2 = tk.Button(self, text="continue",command = lambda: [Downloader(data),data.clear(), master.switch_frame(FinishedPage)] if data else master.switch_frame(PageTwo) )
        button3 = tk.Button(self,text="back" , command= lambda: master.switch_frame(StartPage))
        for i in (0,1,2,3,4,9,18,6,8,10,11,13,14,21,16,17,19,20,22,23,24,25):
            tk.Label(self,text="").grid(row=i,column=0)
        lbl1.grid(row=5)
        button1.grid(row=7)
        button2.grid(row=12)
        button3.grid(row=15)
        
 
    def browse_button(self):
        filename = filedialog.askdirectory()
        data.append(filename)
        data.append("")
        data.append('multiple')
        print(filename)

class FinishedPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        appHighlightFont = font.Font(family='Helvetica', size=20)
        lbl1 = tk.Label(self,text="Image Compression completed",font=appHighlightFont)
        lbl2 = tk.Label(self,text="Image is stored in pictures directory of user")
        button3 = tk.Button(self, text="quit",command = lambda: app.destroy())
        button2 = tk.Button(self,text="return" , command= lambda: master.switch_frame(StartPage))
        for i in (0,1,2,3,4,9,18,7,8,10,11,13,14,21,16,17,19,20,22,23,24,25):
            tk.Label(self,text="").grid(row=i,column=0)
        lbl1.grid(row=5)
        lbl2.grid(row=6)

        button2.grid(row=12)
        button3.grid(row=15)
        

   


if __name__ == "__main__":
    data = list()
    app = App()
    app.title('imageOptimizer')
    app.geometry('400x500')
    Image = tk.PhotoImage(file = 'imageOptimizer.png') 
    app.iconphoto(False, Image) 
    app.mainloop()







