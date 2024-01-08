#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    from Tkinter import *
except:
    from tkinter import *
from tkinter.font import Font, families
import sys
import io
import random
import pyglet
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class ToolBar:
    def __init__ (self, master, r, c):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.grid(row = r, column = c,sticky ="N")



        #self.font = Font(family = "Ink Free",size = 15)
        self.font = ("consolas",13)
        self.fgColour = "white"
        self.bgColour = "grey25"


        #Initialise variables
        self.chinese = []
        self.pyEng = []
        self.chineseDict = {}
        self.popUpOn = False

        self.v = StringVar()
        self.v.set("Hide Eng")
        self.mode1 = Radiobutton(self.frame,
                    text = "Hide Eng",
                    variable = self.v,
                    value = "Hide Eng",
                    indicatoron = False,
                    width = 15,
                    font = self.font,
                    selectcolor = "grey15",
                    bg = self.bgColour,
                    fg = "white",
                    command = lambda: self.pass_Mode(self.v.get())
                    )
        self.mode1.grid()

        self.mode2 = Radiobutton(self.frame,
                    text = "Hide Chn",
                    variable = self.v,
                    value = "Hide Chn",
                    indicatoron = False,
                    width = 15,
                    font = self.font,
                    selectcolor = "grey15",
                    bg = self.bgColour,
                    fg = "white",
                    command = lambda: self.pass_Mode(self.v.get())
                    )
        self.mode2.grid()

        self.txt = Label(self.frame,text = "", width = 15, bg = "grey50", font = self.font)
        self.txt.grid()

        self.randBtn = Button(self.frame, text = "Randomise", width = 15, font = self.font, bg = self.bgColour, fg = "white", command = lambda: self.randomiseList())
        self.randBtn.grid()

        self.loadNextBtn = Button(self.frame, text = "Load Next", width = 15, font = self.font, bg = self.bgColour, fg = "white", command = lambda: self.pass_LoadNextInfo(self.chinese, self.pyEng))
        self.loadNextBtn.grid()

        self.loadAllBtn = Button(self.frame, text = "Load All", width = 15, font = self.font, bg = self.bgColour, fg = "white", command = lambda: self.pass_LoadAllInfo(self.chinese, self.pyEng))
        self.loadAllBtn.grid()

        self.showNextBtn = Button(self.frame, text = "Show Next", width = 15, font = self.font, bg = self.bgColour, fg = "white", command = lambda: self.pass_ShowNextInfo(self.chinese, self.pyEng))
        self.showNextBtn.grid()

        self.showPageBtn = Button(self.frame, text = "Show Page", width = 15, font = self.font, bg = self.bgColour, fg = "white", command = lambda: self.pass_ShowPageInfo(self.chinese, self.pyEng))
        self.showPageBtn.grid()

        self.showAllBtn = Button(self.frame, text = "Show all", width = 15, font = self.font, bg = self.bgColour, fg = "white", command = lambda: self.pass_ShowAllInfo(self.chinese, self.pyEng))
        self.showAllBtn.grid()

        self.addWordBtn = Button(self.frame, text = "Add Word", width = 15, font = self.font, bg = self.bgColour, fg = "white", command = lambda: self.addWord())
        self.addWordBtn.grid()

        self.clearBtn = Button(self.frame, text = "Clear", width = 15, font = self.font, bg = self.bgColour, fg = "white", command = lambda: self.clearListBoxes())
        self.clearBtn.grid()

    def pass_Mode(self,mode):
        pass


        """
    def setMode(self):
        self.mode = self.v.get()
        self.clearListBoxes()
        print(self.mode)"""


    def setDictVal(self):
        self.chineseDict = {}
        for i in range (len(self.chinese)):
            self.chineseDict[self.chinese[i]] = self.pyEng[i]


    def readFile(self):
        self.chinese = []
        self.pyEng = []
        with open("chineseVocab.txt", "r",encoding = "utf-8") as f:
            allContents = f.read()
            lineContents = allContents.split( "\n")
            lineContents.remove("")
            for index in range(len(lineContents)):
                wordContents = lineContents[index].split("  ")
                self.chinese.append(wordContents[0])
                self.pyEng.append(wordContents[1]+"  "+wordContents[2])
            f.close()
        self.setDictVal()


    def randomiseList(self):
        self.clearListBoxes()
        random.shuffle(self.chinese)
        self.pyEng = []
        for i in range (len(self.chinese)):
            self.pyEng.append(self.chineseDict[self.chinese[i]])


    def pass_LoadNextInfo(self,chinese,pyEng):
        pass


    def pass_LoadAllInfo(self,chinese):
        pass


    def pass_ShowNextInfo(self,pyEng):
        pass

    def pass_ShowPageInfo(self,pyEng):
        pass


    def pass_ShowAllInfo(self,pyEng):
        pass



    def addWord(self):
        if self.popUpOn == False:
            self.popUpOn = True
            self.addWin = Toplevel(bg ="grey25")
            self.addWin.title("Add Word")
            self.addWin.resizable(False,False)
            self.font2 = ("consolas",15)
            self.chLabel = Label(self.addWin, text ="Chinese: ", width = 10, font = self.font2, bg = self.bgColour, fg = "white")
            self.chLabel.grid(row = 0, column = 0)
            self.pyLabel = Label(self.addWin, text ="Pinyin: ", width = 10, font = self.font2, bg = self.bgColour, fg = "white")
            self.pyLabel.grid(row = 1, column = 0)
            self.enLabel = Label(self.addWin, text ="English: ", width = 10, font = self.font2, bg = self.bgColour, fg = "white")
            self.enLabel.grid(row = 2, column = 0)
            self.chEntry = Entry(self.addWin, width = 10, font = self.font2, bg = self.bgColour, fg = "white")
            self.chEntry.insert(0,"")
            self.chEntry.grid(row = 0, column = 1)
            self.pyEntry = Entry(self.addWin, width = 10, font = self.font2, bg = self.bgColour, fg = "white")
            self.pyEntry.insert(0,"")
            self.pyEntry.grid(row = 1, column = 1)
            self.enEntry = Entry(self.addWin, width = 10, font = self.font2, bg = self.bgColour, fg = "white")
            self.enEntry.insert(0,"")
            self.enEntry.grid(row = 2, column = 1)

            self.enterBtn = Button(self.addWin,text = "Enter",  font = self.font2, bg = self.bgColour, fg = "white",command =lambda: self.writeFile())
            self.enterBtn.grid(row = 3, columnspan = 2)


    def writeFile(self):
        self.chIn = self.chEntry.get()
        self.pyIn = self.pyEntry.get()
        self.enIn = self.enEntry.get()
        self.addWin.destroy()
        self.popUpOn = False

        with open("chineseVocab.txt", "a",encoding = "utf-8") as f:
            self.content = self.chIn +"  "+ self.pyIn +"  "+self.enIn
            if len(self.content) > 4:
                f.write(self.content)
                f.close()



    def clearListBoxes(self):
        pass


if __name__ == "__main__":

    root = Tk()
    tb = ToolBar(root,0,0)


    root.mainloop()
