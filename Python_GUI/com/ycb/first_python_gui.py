import tkinter as tk

from tkinter import ttk    # 添加一个组件
from tkinter import scrolledtext
from tkinter import Menu,Spinbox
from tkinter import messagebox as mBox


win = tk.Tk()
win.title("YCB's GUI")
win.resizable(2, 10)

# 定义一个模块级的全局变量
GLOBAL_CONST = 42
print(GLOBAL_CONST)
# 添加一个菜单栏
menuBar = Menu(win)
win.configure(menu=menuBar)

# 取消按钮的功能
# def _quit():
#    win.quit()
#    win.destroy()
#    exit()

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
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)


#######################################################################
# tabControl = ttk.Notebook(win)  # 创建一个控制标签
# tab1 = ttk.Frame(tabControl)  # 添加一个tab
# tabControl.add(tab1, text='Tab 1')  # 添加一个tab
# tab2 = ttk.Frame(tabControl)
# tabControl.add(tab2, text='Tab 2')
# tabControl.pack(expand=1, fill="both")   # 使包可见
#
# monty = ttk.LabelFrame(tab1, text='Monty Python')
# monty.grid(column=0, row=0, padx=8, pady=4)
# ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky='W')
##########################################################################

# Add a title
# We are creating a container frame to hold all other widgets # 1
monty = ttk.LabelFrame(win, text=' Monty Python ')
monty.grid(column=0, row=0)
aLabel = ttk.Label(monty, text="A Label")

aLabel = ttk.Label(monty, text="Enter a name:")  # 插入一个文本框
aLabel.grid(column=1, row=1, sticky=tk.W)

name = tk.StringVar()  # 使用tkinter必须声明变量名作为类型，因为他不属于python语言
nameEntered = ttk.Entry(monty, width=12, textvariable=name).grid(column=2, row=1)
# nameEntered.focus()   # 游标现在默认驻留在文本输入框中

def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

spin = Spinbox(monty, from_=0, to=10, width=5, bd=8, relief=tk.RIDGE, command=_spin)
spin.grid(column=0, row=2)

# 注意与第一个spinbox对比
spin = Spinbox(monty, values=(0, 50, 100), width=5, bd=20, relief=tk.GROOVE, command=_spin)
spin.grid(column=1, row=2)


def clickMe():
    action.configure(text='Hello ' + name.get())
    aLabel.configure(foreground='red')


# Adding a Button
action = ttk.Button(monty, text="Click Me!", command=clickMe)
action.grid(column=2, row=2)
# action.configure(state='disabled') # Disable the Button Widget


# Adding a Combobox
aLabel = ttk.Label(monty, text="please choose a number:").grid(column=2, row=3)
number = tk.StringVar()
numberEntered = ttk.Entry(monty, width=12, textvariable=number).grid(column=0, row=1)
numberChosen = ttk.Combobox(monty, width=12, textvariable=number, state='readonly')
numberChosen['values'] = [1, 2, 4, 42, 100]
numberChosen.grid(column=3, row=3)
numberChosen.current(0)

# Creating three checkbuttons   创建3个可选框
chVarDis = tk.IntVar()   # 创建第一个整型变量
check1 = tk.Checkbutton(monty, text="disabled", variable=chVarDis, state='disabled')
check1.select()   # 设为可选
check1.anchor()
check1.grid(column=0, row=4, sticky=tk.S)  # 向左靠齐

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(monty, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)


# radiobutton globals
# COLOR1 = "Blue"
# COLOR2 = "Gold"
# COLOR3 = "Green"
# refactor 重构一下
colors = ["Blue", "Gold", "Red"]

# radiobutton callback
def radCall():
    radSel=radVar.get()
    if radSel == 1: win.configure(background=colors[0])
    elif radSel == 2:win.configure(background=colors[1])
    elif radSel == 3: win.configure(background=colors[2])

# create three Radiobuttons
radVar = tk.IntVar()   # create three Radiobuttons using one variable
radVar.set(99)   # Next we are selecting a non-existing index value for radVar.

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)


# using a scrolled text control   使用一个滚动条
scrolW = 30
scrolH = 3


# By setting the wrap property to tk.WORD we are telling the ScrolledText widget to breaklines by words,
# so that we do not wrap around within a word. The default option is tk.CHAR,
# which wraps any character regardless of whether we are in the middle of a word
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.CHAR)     # 最后一个属性是将滚动文本框随文字多少自动扩展
scr.grid(column=1, columnspan=3)

# Create a container to hold labels  将label放在win里面
labelsFrame = ttk.LabelFrame(monty, text=' Labels in a Frame ')
labelsFrame.grid(column=1, row=7)

# 将小标签放在labelsFrame里面,column值不同，就可设置为水平放置
ttk.Label(labelsFrame, text="label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="label2").grid(column=1, row=0)
ttk.Label(labelsFrame, text="label3").grid(column=2, row=0)

##########################################################
# 创建消息提示框
def _msgBox():
    mBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2018.')
##########################################################
# 如何从组件中取数据
strData = spin.get()   # 只需要一个get函数
print("Spinbox value" + strData)

win.mainloop()
