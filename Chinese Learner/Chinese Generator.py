try:
    from Tkinter import *
except:
    from tkinter import *
from Toolbox import *
from WordDisplay import *




if __name__ == "__main__":

    root = Tk()
    root.configure(bg = "grey25")
    root.title("Chinese Generator")
    root.resizable(False,False)
    tb = ToolBar(root,0,0)
    wd = Display(root,0,1)

    tb.pass_LoadNextInfo = wd.loadNext
    tb.pass_LoadAllInfo = wd.loadAll
    tb.pass_ShowNextInfo = wd.showNext
    tb.pass_ShowPageInfo = wd.showPage
    tb.pass_ShowAllInfo = wd.showAll
    tb.clearListBoxes = wd.clearListBoxes
    tb.pass_Mode = wd.setMode
    tb.readFile()
    root.mainloop()
