#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# from tkinter import *
# from tkinter import messagebox as msb
# import functools as ft
#
# # def resize(ev=None):
# #     label.config(font='Helvetica -%d bold' % scale.get())
# #
# # top = Tk()
# # top.geometry('250x150')
# #
# # label = Label(top, text='Hello World!', font='Helvetica -12 bold')
# # label.pack(fill=Y, expand=1)
# #
# # scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
# # scale.set(12)
# # scale.pack(fill=X, expand=1)
# #
# # quit = Button(top, text='QUIT', command=top.quit, activeforeground='red',
# #               activebackground ='white')
# #
# # quit.pack()
# # mainloop()
#
# WARN = 'warn'
# CRIT = 'crit'
# REGU = 'regu'
#
# SIGNS = {
#     'do not enter': CRIT,
#     'railroad crossing': REGU,
#     'wrong way': CRIT,
#     'merging traffic': WARN,
#     'one way': REGU,
# }
#
# critCB = lambda: msb.showerror('Error', 'Error button Pressed!')
# warnCB = lambda: msb.showwarning('Warning', 'Warning Button Pressed!')
# infoCB = lambda: msb.showinfo('Info', 'Info Button pressed!')
#
# top = Tk()
# top.title('Road Signs')
# Button(top, text='QUIT', command=top.quit, bg='red', fg='white').pack()
#
# MyButton = ft.partial(Button, top)
# CritButton = ft.partial(MyButton, command=critCB, bg='white', fg='red')
# WarnButton = ft.partial(MyButton, command=warnCB, bg='goldenrod1')
# ReguButton = ft.partial(MyButton, command=infoCB, bg='white')
#
# for eachsign in SIGNS:
#     signType = SIGNS[eachsign]
#     print(signType, signType.title())
#     cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (
#         signType.title(), eachsign, '.upper()' if signType == CRIT else '.title()')
#     eval(cmd)
# top.mainloop()

## 字符串拼接
s1 = 'xiaoming'
s2 = '.upper()'
s3 = '(%r%s)' % (s1, s2)
print(s3)