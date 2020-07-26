from tkinter import *
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import time
import random
import webbrowser
import sys

try:
    os.rmdir('.\\win31\\windowsSetupEnds')
except:
    pass

if not os.path.exists('.\\win31'):
    messagebox.showerror('', 'Cannot start Install manager,try it later')
    sys.exit()
if not os.path.exists('.\\win31\\users'):
    messagebox.showerror('', 'Cannot start Install manager,try it later')
    sys.exit()


def check(username, u, pa, root6):
    usern = open('.\\win31\\users\\%s\\username.txt' % username, 'r')
    passwo = open('.\\win31\\users\\%s\\password.txt' % username, 'r')
    if usern.read() == u.get() and passwo.read() == pa.get():
        root6.destroy()
    else:
        messagebox.showerror('', 'Некоректный пароль или имя!')


def restart(username, root5):
    os.mkdir('.\\win31\\windowsSetupEnds')
    root5.destroy()
    root6 = Tk()
    root6.title('')
    Label(root6, text='Имя:').grid()
    Label(root6, text='Пароль:').grid()
    u = Entry(root6)
    pa = Entry(root6, show='*')
    u.grid(column=1, row=0)
    pa.grid(column=1, row=1)
    OKbtn = Button(root6, command=lambda: check(username, u, pa, root6), text='OK')
    OKbtn.grid(columnspan=3)
    root6.mainloop()


def lasts(username, root5):
    lastIcon = Toplevel()
    lastIcon.title('Windows setup ends!')

    Button(lastIcon, text='Перезагрузить', command=lambda: restart(username, root5)).grid(row=0, column=0)
    Button(lastIcon, text='Вернуться в MS-DOS',
           command=lambda: os.startfile('C:\\Windows\\System32\\cmd.exe')).grid(row=0, column=1)


def next(root2, username, password):
    root2.destroy()
    os.mkdir('.\\win31\\users\\%s' % username)
    f = open('.\\win31\\users\\%s\\username.txt' % username, 'w')
    f.write(username)
    f.close()
    p = open('.\\win31\\users\\%s\\password.txt' % username, 'w')
    p.write(password)
    p.close()
    tu = open('.\\win31\\users\\currentUser.txt', 'w')
    tu.write(username)
    tu.close()
    ApplicationInstallingNow = 'Календарь'
    FileInstallingNow = 'Calendar.exe'
    root3 = Tk()
    root4 = Toplevel()
    root3.title('Windows Setup')
    root4.title('Windows Setup')
    root4.geometry('+500+500')
    root4['bg'] = 'white'
    setupIcon = PhotoImage(file='images/setupIcon.png')
    setupLbl = Label(root4, image=setupIcon)
    setupLbl.grid(column=0)
    Label(root4,
          text='Добро пожаловать в Микрусофт(только из одного человека) Windows 3.1!\n\n-Если у Вас нет опыта работы с Windows, см. \"Краткое путешествие по Микрусофт Windows\" в книге \"Приступая к работе\".\n-Если вы уже работали с Windows, см. \"Новые возможности этой версии\" в книге \"Приступая к работе\"').grid(
        row=0, column=1)
    lblApplication = Label(root3, text='Копируем: %s' % ApplicationInstallingNow)
    lblApplication.grid(row=0, column=0)
    lblFile = Label(root3, text='Файл: %s' % FileInstallingNow)
    lblFile.grid(row=1, column=0)
    pb = ttk.Progressbar(root3, length=525)
    pb.grid(column=0, row=2)
    Button(root3, text='Выход из Setup', command=lambda: sys.exit()).grid(row=3)
    pb.step(random.randint(4, 12))
    time.sleep(1)
    root3.update()
    ApplicationInstallingNow = 'Файл менеджер'
    FileInstallingNow = 'File manager.exe'
    lblApplication['text'] = 'Копируем: %s' % ApplicationInstallingNow
    lblFile['text'] = 'Файл: %s' % FileInstallingNow
    root3.update_idletasks()
    pb.step(random.randint(4, 12))
    time.sleep(1)
    root3.update()
    root3.update_idletasks()
    root4.update()
    root4.update_idletasks()
    ApplicationInstallingNow = 'Документ Write'
    FileInstallingNow = 'Write.exe'
    lblApplication['text'] = 'Копируем: %s' % ApplicationInstallingNow
    lblFile['text'] = 'Файл: %s' % FileInstallingNow
    root3.update_idletasks()
    pb.step(random.randint(4, 12))
    time.sleep(1)
    root3.update()
    root3.update_idletasks()
    root4.update()
    root4.update_idletasks()
    ApplicationInstallingNow = 'Часы'
    FileInstallingNow = 'Clock.exe'
    lblApplication['text'] = 'Копируем: %s' % ApplicationInstallingNow
    lblFile['text'] = 'Файл: %s' % FileInstallingNow
    root3.update_idletasks()
    pb.step(random.randint(4, 12))
    time.sleep(1)
    root3.update()
    root3.update_idletasks()
    root4.update()
    root4.update_idletasks()
    ApplicationInstallingNow = 'Рисовалка'
    FileInstallingNow = 'PaintBrush.exe'
    lblApplication['text'] = 'Копируем: %s' % ApplicationInstallingNow
    lblFile['text'] = 'Файл: %s' % FileInstallingNow
    root3.update_idletasks()
    pb.step(random.randint(4, 12))
    time.sleep(1)
    root3.update()
    root3.update_idletasks()
    root4.update()
    root4.update_idletasks()
    ApplicationInstallingNow = 'Игры'
    FileInstallingNow = 'Игры.GRP'
    lblApplication['text'] = 'Копируем: %s' % ApplicationInstallingNow
    lblFile['text'] = 'Файл: %s' % FileInstallingNow
    root3.update_idletasks()
    pb.step(random.randint(4, 12))
    time.sleep(1)
    root3.update()
    root3.update_idletasks()
    root4.update()
    root4.update_idletasks()
    ApplicationInstallingNow = 'Шрифты'
    FileInstallingNow = 'Fonts'
    lblApplication['text'] = 'Копируем: %s' % ApplicationInstallingNow
    lblFile['text'] = 'Файл: %s' % FileInstallingNow
    root3.update_idletasks()
    pb.step(random.randint(4, 12))
    time.sleep(1)
    root3.update()
    root3.update_idletasks()
    root4.update()
    root4.update_idletasks()
    ApplicationInstallingNow = 'ReadMe'
    FileInstallingNow = 'ReadMe(Прочти меня).doc'
    lblApplication['text'] = 'Копируем: %s' % ApplicationInstallingNow
    lblFile['text'] = 'Файл: %s' % FileInstallingNow
    root3.update_idletasks()
    pb.step(random.randint(4, 12))
    time.sleep(1)
    root3.update()
    root3.update_idletasks()
    root4.update()
    root4.update_idletasks()
    root3.destroy()
    root5 = Tk()
    root5.title('Windows Setup')
    Label(root5,
          text='Сейчас Setup может запустить\nкраткую обучающий текст, демонстрирующую основные навыки работы с Windows и мышью.\n\nКроме того, Вы можете, запустить Учебник и после установки Windows. ').grid(
        row=0, column=0)
    Button(root5, text='Запустить Учебник',
           command=lambda: webbrowser.open('https://www.pc-school.ru/rabota-s-myshyu-v-windows/')).grid(row=0,
                                                                                                        column=1)

    Button(root5, text='Пропустить Учебник', command=lambda: lasts(username, root5)).grid(row=2, column=1)
    Button(root5, command=lambda: sys.exit(), text='Выход из Setup').grid(row=3, column=1)
    Button(root5, command=helpME, text='Справка').grid(row=4, column=1)
    root5.mainloop()


def edit(root2):
    root2.destroy()
    AskName()


def helpME2():
    helping = Toplevel()
    helping.geometry('0x0')
    helping.title('Справка')
    helping.mainloop()


def MakeSureYourName(rootForDestroy, username, password):
    if os.path.exists('.\\win31\\users\\%s' % username):
        messagebox.showerror('', 'Пользователь с таки именем уже существует')
        rootForDestroy.destroy()
        AskName()

    rootForDestroy.destroy()
    if username.rstrip() == '':
        messagebox.showerror('', 'Увы, но НУЖНО ВВОДИТЬ СВОЕ ИМЯ!')
        AskName()
    if password.rstrip() == '':
        messagebox.showerror('', 'Увы, но НУЖНО ВВОДИТЬ СВОЙ ПАРОЛЬ!')
        AskName()
    root2 = Tk()
    root2.title('Windows Setup')
    Label(root2,
          text='Убедитесь в правильности введенного Вами имени. Чтобы\nизменить его, выберите изменить. В противном случае,\nвыберите Продолжить.').grid(
        row=0, columnspan=4)
    if password.rstrip() == '' and username.rstrip() == '':
        messagebox.showerror('', 'Увы, но НУЖНО ВВОДИТЬ СВОЙ ПАРОЛЬ И ИМЯ!')
        AskName()
    Label(root2, text='Имя:      %s' % username).grid(row=1, column=0)
    Label(root2, text='Пароль:      %s' % password).grid(row=2, column=0)
    Button(root2, text='Продолжить', command=lambda: next(root2, username, password)).grid(row=3, column=0)
    Button(root2, text='Изменить', command=lambda: edit(root2)).grid(row=3, column=1)
    Button(root2, command=lambda: sys.exit(), text='Выход из Setup').grid(row=3, column=2)
    Button(root2, command=helpME2, text='Справка').grid(row=3, column=3)
    root2.mainloop()


def sign_in(namee, passw, root):
    if not os.path.exists('.\\win31\\users\\%s' % namee.get()):
        messagebox.showerror('', 'Такого пользователя не существует')
    else:
        try:
            usernam = open('.\\win31\\users\\%s\\username.txt' % namee.get(), 'r')
            passwo = open('.\\win31\\users\\%s\\password.txt' % namee.get(), 'r')
            if usernam.readline() == namee.get() and passwo.readline() == passw.get():
                tu = open('.\\win31\\users\\currentUser.txt', 'w')
                tu.write(namee.get())
                tu.close()
                root.destroy()
                os.mkdir('.\\win31\\windowsSetupEnds')
            else:
                messagebox.showerror('', 'Некоректный пароль или имя!')
        except:
            messagebox.showerror('', 'Некоректное имя пользователя')
            sys.exit()


def nextbtn(namee, passw, root):
    MakeSureYourName(root, username=namee.get(), password=passw.get())


def helpME():
    helping = Tk()
    helping.geometry('0x0')
    helping.title('Справка')
    helping.mainloop()


def AskName():
    def next(event):
        MakeSureYourName(root, username=namee.get(), password=passw.get())

    root = Tk()
    root.title('Windows Setup')
    lbl = Label(root,
                text='В окне внизу введите Ваше полное имя и пароль\n\nЗатем выберите Продолжить или нажмите \nENTER.\n\nВведеная вами информация будет\nиспользована программой Setup для\nдальнейшей установки сиситемы Windows.')
    lbl.grid(columnspan=3)
    Label(root, text='Имя:').grid(row=1, columnspan=3)
    Label(root, text='Пароль: ').grid(row=4, columnspan=3)
    namee = Entry(root)
    namee.grid(row=3, columnspan=3)
    passw = Entry(root, show='*')
    passw.grid(row=5, columnspan=3)
    Button(root, command=lambda: nextbtn(namee, passw, root), text='Создать нового пользователя').grid(row=6, column=0)
    Button(root, command=lambda: sys.exit(), text='Выход из Setup').grid(row=6, column=1)
    Button(root, command=helpME, text='Справка').grid(row=6, column=2)
    Button(root, command=lambda: sign_in(namee, passw, root), text='Войти').grid(row=6, column=3)
    root.bind('<KeyPress-Return>', next)
    root.mainloop()


def setup():
    AskName()
