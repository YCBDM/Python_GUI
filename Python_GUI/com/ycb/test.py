'''''7.组件使用多列（多行）'''
# -*- coding: utf-8 -*-
# 使用多行（多列)
from tkinter import *

root = Tk()
# 创建如下布局（一个字符占用一个grid位置）
# A  E
# B C
# D
# A占用(0,0)(0,1),B占用(1,0),C占用(1,1),D占用(2,0),E占用(0,2)
# 创建5个Label，分别以背景色区别
lbA = Label(root, text='A', bg='red')
lbB = Label(root, text='B', bg='green')
lbC = Label(root, text='C', bg='red')
lbD = Label(root, text='D', bg='blue')
lbE = Label(root, text='E', bg='blue')
# 以下为布局参数设置
lbA.grid(row=0, column=0, columnspan=2)
lbB.grid(row=1, column=0)
lbC.grid(row=1, column=1)
lbD.grid(row=2, column=0, columnspan=5)
lbE.grid(row=0, column=2)

root.mainloop()
# A与B、D的区别，它左边已改变，由于使用了两个表格；
# C与E的区别：C的右边与E的左边对齐，也就是说E被放置到第2列的下一个位置了，原因由于A已使用了第2列。