try:
    from Tkinter import *
except:
    from tkinter import *
import pyglet

from tkinter.font import Font, families

class Display:
    def __init__(self, master, r, c):
        self.master = master
        self.font = ("consolas",13)
        #self.font = Font(family = "Ink Free",size = 15)

        self.fgColour = "white"
        self.bgColour = "grey25"
        self.shownList = 0
        self.mode = "Hide Eng"


        self.frame = Frame(self.master)
        self.frame.grid(row = r, column = c)
        self.chFrame = Frame(self.frame)
        self.chFrame.pack(side = LEFT)
        self.pyFrame = Frame(self.frame)
        self.pyFrame.pack(side = LEFT)
        self.enFrame = Frame(self.frame)
        self.enFrame.pack(side = LEFT)
        self.scrollBar = Scrollbar(self.frame, orient=VERTICAL)
        self.scrollBar.pack(side=RIGHT, fill=Y)
        self.scrollBar.config(command =self.yview)


        self.chListBox = Listbox(self.chFrame, height = 20, font = self.font, bg = self.bgColour, fg = "white", yscrollcommand =self.scrollBar.set)
        self.chListBox.pack()
        self.pyListBox = Listbox(self.pyFrame, height = 20, font = self.font, bg = self.bgColour, fg = "white", yscrollcommand =self.scrollBar.set)
        self.pyListBox.pack()
        self.enListBox = Listbox(self.enFrame, height = 20, font = self.font, bg = self.bgColour, fg = "white", yscrollcommand =self.scrollBar.set)
        self.enListBox.pack()

    def yview(self, *args):
        self.chListBox.yview(*args)
        self.pyListBox.yview(*args)
        self.enListBox.yview(*args)


    def popDone(self):
        self.popWin = Toplevel(bg =self.bgColour)
        self.popWin.title("Error")
        self.fullLabel = Label(self.popWin, text = "Displayed All Vocabs", font = self.font, bg = self.bgColour, fg = "white")
        self.fullLabel.pack()
        self.exitBtn = Button(self.popWin, text = "Exit", command = lambda: self.popWin.destroy(), font = self.font, bg = self.bgColour, fg = "white")
        self.exitBtn.pack()


    def clearListBoxes(self):
        self.shownList = 0
        self.chListBox.delete(0, END)
        self.chListBox.pack()
        self.pyListBox.delete(0, END)
        self.pyListBox.pack()
        self.enListBox.delete(0, END)
        self.enListBox.pack()


    def loadNext(self, chinese, pyEng):
        self.chinese = chinese
        self.pyEng = pyEng

        if self.mode == "Hide Eng":
            self.chListBoxSize = self.chListBox.size()
            if self.chListBoxSize == len(self.chinese):
                self.popDone()
            else:
                self.chListBox.delete(0, END)
                for index in range(self.chListBoxSize + 1):
                    self.chListBox.insert(END, self.chinese[index])
                    self.chListBox.pack()
        else:
            self.pyListBoxSize = self.pyListBox.size()
            if self.pyListBoxSize == len(self.pyEng):
                self.popDone()
            else:
                self.pyListBox.delete(0, END)
                self.enListBox.delete(0, END)
                for index in range(self.pyListBoxSize + 1):
                    self.entry = self.pyEng[index].split("  ")
                    self.pinyin = self.entry[0]
                    self.english = self.entry[1]
                    self.pyListBox.insert(END, self.pinyin)
                    self.enListBox.insert(END, self.english)
                    self.pyListBox.pack()
                    self.enListBox.pack()



    def loadAll(self, chinese, pyEng):
        self.chinese = chinese
        self.pyEng = pyEng
        if self.mode == self.mode == "Hide Eng":
            self.chListBox.delete(0, END)
            for entry in self.chinese:
                self.chListBox.insert(END, entry)
                self.chListBox.pack()
        else:
            self.pyListBox.delete(0, END)
            self.enListBox.delete(0, END)
            for entry in self.pyEng:
                self.entry = entry.split("  ")
                self.pinyin = self.entry[0]
                self.english = self.entry[1]
                self.pyListBox.insert(END, self.pinyin)
                self.pyListBox.pack()
                self.enListBox.insert(END, self.english)
                self.enListBox.pack()



    def showNext(self, chinese, pyEng):
        self.chinese = chinese
        self.pyEng = pyEng
        self.chListBoxSize = self.chListBox.size()
        self.pyListBoxSize = self.pyListBox.size()

        if self.mode == self.mode == "Hide Eng":
            if self.shownList < self.chListBoxSize:
                self.pyListBox.delete(0, END)
                self.enListBox.delete(0, END)
                for index in range(self.shownList+1):
                    self.entry = self.pyEng[index].split("  ")
                    self.pinyin = self.entry[0]
                    self.english = self.entry[1]
                    self.pyListBox.insert(END, self.pinyin)
                    self.pyListBox.pack()
                    self.enListBox.insert(END, self.english)
                    self.enListBox.pack()
                for blank in range (self.chListBoxSize - self.shownList):
                    self.pyListBox.insert(END, "")
                    self.pyListBox.pack()
                    self.enListBox.insert(END, "")
                    self.enListBox.pack()
                self.shownList += 1
        else:
            if self.shownList < self.pyListBoxSize:
                self.chListBox.delete(0, END)
                for index in range(self.shownList+1):
                    self.chListBox.insert(END, self.chinese[index])
                    self.chListBox.pack()
                for blank in range (self.pyListBoxSize - self.shownList):
                    self.chListBox.insert(END, "")
                    self.chListBox.pack()
                self.shownList += 1

    def showPage(self, chinese, pyEng):
        self.chinese = chinese
        self.pyEng = pyEng
        self.chListBoxSize = self.chListBox.size()
        self.pyListBoxSize = self.pyListBox.size()

        if self.mode == self.mode == "Hide Eng":
            if self.shownList < self.chListBoxSize:
                self.pyListBox.delete(0, END)
                self.enListBox.delete(0, END)
                if self.chListBoxSize - self.shownList < 20:
                    self.showAll(self.chinese,self.pyEng)
                else:
                    for index in range(self.shownList+20):
                        self.entry = self.pyEng[index].split("  ")
                        self.pinyin = self.entry[0]
                        self.english = self.entry[1]
                        self.pyListBox.insert(END, self.pinyin)
                        self.pyListBox.pack()
                        self.enListBox.insert(END, self.english)
                        self.enListBox.pack()
                    for blank in range (self.chListBoxSize - self.shownList - 20):
                        self.pyListBox.insert(END, "")
                        self.pyListBox.pack()
                        self.enListBox.insert(END, "")
                        self.enListBox.pack()
                    self.shownList += 20
        else:
            if self.shownList < self.pyListBoxSize:
                self.chListBox.delete(0, END)
                if self.pyListBoxSize - self.shownList < 20:
                    self.showAll(self.chinese,self.pyEng)
                else:
                    for index in range(self.shownList+20):
                        self.chListBox.insert(END, self.chinese[index])
                        self.chListBox.pack()
                    for blank in range (self.pyListBoxSize - self.shownList - 20):
                        self.chListBox.insert(END, "")
                        self.chListBox.pack()
                    self.shownList += 20

    def showAll(self, chinese, pyEng):
        self.chinese = chinese
        self.pyEng = pyEng
        self.pyListBoxSize = self.pyListBox.size()
        self.chListBoxSize = self.chListBox.size()
        if self.mode == self.mode == "Hide Eng":
            self.shownList = self.chListBoxSize
            self.pyListBox.delete(0, END)
            self.enListBox.delete(0, END)
            for index in range(self.chListBoxSize):
                entry = self.pyEng[index].split("  ")
                self.pinyin = entry[0]
                self.english = entry[1]
                self.pyListBox.insert(END, self.pinyin)
                self.pyListBox.pack()
                self.enListBox.insert(END, self.english)
                self.enListBox.pack()
        else:
            self.shownList = self.pyListBoxSize
            self.chListBox.delete(0, END)
            for index in range(self.pyListBoxSize):
                self.chListBox.insert(END, self.chinese[index])
                self.chListBox.pack()


    def setMode(self,mode):
        self.mode = mode
        self.clearListBoxes()
        print(self.mode)

if __name__ == "__main__":

    root = Tk()
    d = Display(root,0,0)
    root.mainloop()
