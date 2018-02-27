import tkinter as tk
from tkinter import ttk    # 添加一个组件
from tkinter import scrolledtext
from tkinter import messagebox as mBox
from tkinter import Menu
from tkinter import Spinbox

##############################################################
# creating tooltips using Python
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


    def createToolTip(widget, text):
        toolTip = ToolTip(widget)

        def enter(event):
            toolTip.showtip(text)

        def leave(event):
            toolTip.hidetip()

        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)
##############################################################

win = tk.Tk()
# win.withdraw 隐藏窗口并在后台运行
win.title("YCB's GUI")
win.iconbitmap(r'C:\Users\Public\Pictures\IMG_20161217_115902.jpg')  # 设置图标
tabControl = ttk.Notebook(win)  # 创建一个控制标签
tab1 = ttk.Frame(tabControl)  # 添加一个tab
tabControl.add(tab1, text='Tab 1')  # 添加一个tab
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")   # 使包可见
####################################################################
# 添加一个菜单栏
menuBar = Menu(win)
win.configure(menu=menuBar)

# 取消按钮的功能
# def _quit():
#    win.quit()
#    win.destroy()
#    exit()

# 。。。。。。。。。。。。。。。。。。。。
# 自定义消息提示框
def _msgBox():
    answer = mBox.askyesno("Python Message Dual Choice Box","Are you sure you really wish to do this?")
    print(answer)
# 。。。。。。。。。。。。。。。。。。。。

# 。。。。。。。。。。。。。。。。。。。。
# 消息提示框回调函数
#def _msgBox():
    # mBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2018.')
    # mBox.showwarning('Python Message Warning Box', 'A Python GUI created using tkinter:\nWarning: There might be a bug in this code.')
    # mBox.askquestion('Python Message question Box', 'Do you Know 1+1=?')
    # mBox.showerror('Python Message Error Box', 'A Python GUI created using tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
#  。。。。。。。。。。。。。。。。。。。。
# 在菜单栏上添加文件按钮
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")   # 文件按钮里面添加
fileMenu.add_separator()
fileMenu.add_command(label="View")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")
# fileMenu.add_command(label="Exit", command=_quit())  # command命令属性，绑定取消按钮的功能
menuBar.add_cascade(label="File", menu=fileMenu)


# 在菜单栏上添加Help按钮
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)

##########################################################################
monty = ttk.LabelFrame(tab1, text='Monty Python')
monty.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky='W')

scrolW = 30; scrolH = 3
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)

# Spinbox callback
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

# 设置不同的relief的属性来改变spinbox的形状，tk.SUNKEN tk.RAISED tk.FLAT tk.GROOVE tk.RIDGE
spin = Spinbox(monty, from_=0, to=10, width=5, bd=8, relief=tk.RIDGE, command=_spin)
spin.grid(column=0, row=2)

# 注意与第一个spinbox对比
spin = Spinbox(monty, values=(0, 50, 100), width=5, bd=20, relief=tk.GROOVE, command=_spin)
spin.grid(column=1, row=2)


###################################################################
# 增加一个monty2，然后添加三个复选框
monty2 = ttk.LabelFrame(tab2, text=' The Snake')
monty2.grid(column=0, row=0, padx=8, pady=4)

# Creating three checkbuttons   创建3个可选框
chVarDis = tk.IntVar()   # 创建第一个整型变量
check1 = tk.Checkbutton(monty2, text="disabled", variable=chVarDis, state='disabled')
check1.select()   # 设为可选
check1.anchor()
check1.grid(column=0, row=4, sticky=tk.S)  # 向左靠齐

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(monty2, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W, columnspan=3)
##############################################################
# 增加三个背景色
colors = ["Blue", "Gold", "Red"]

# radiobutton callback
def radCall():
    radSel=radVar.get()
    if radSel == 1: monty2.configure(background=colors[0])
    elif radSel == 2:monty2.configure(background=colors[1])
    elif radSel == 3: monty2.configure(background=colors[2])

# create three Radiobuttons 创建三个单选框
radVar = tk.IntVar()   # create three Radiobuttons using one variable
radVar.set(99)   # Next we are selecting a non-existing index value for radVar.

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty2, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)


# using a scrolled text control   使用一个带滚动条的文本框
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(monty2, width=scrolW, height=scrolH, wrap=tk.CHAR)     # 最后一个属性是将滚动文本框随文字多少自动扩展
scr.grid(column=0, sticky='WE',  columnspan=3)
# curRad.grid(column=col, row=6, sticky=tk.W, columnspan=3)
# labelsFrame.grid(column=0, row=7)
################################################################

win.mainloop()
