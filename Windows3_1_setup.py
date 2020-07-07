from tkinter import *
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import time
import random
import webbrowser
import sys


def setup():
    def AskName():
        def next(event):
            MakeSureYourName(root,username=namee.get())

        def nextbtn(name):
            MakeSureYourName(root,username=namee.get())

        def helpME():
            helping = Tk()
            helping.geometry('0x0')
            helping.title('Справка')
            helping.mainloop()
        root = Tk()
        root.title('Windows Setup')
        lbl = Label(root,text='В окне внизу введите Ваше полное имя\n\nЗатем выберите Продолжить или нажмите \nENTER.\n\nВведеная вами информация будет\nиспользована программой Setup для\nдальнейшей установки сиситемы Windows.')
        lbl.grid(columnspan=3)
        Label(root, text='Имя:').grid(row=1,columnspan=3)
        namee = Entry(root)
        namee.grid(row=2,columnspan=3)
        Button(root,command=lambda: nextbtn(namee.get()),text='Продолжить').grid(row=3,column=0)
        Button(root, command=lambda: sys.exit(), text='Выход из Setup').grid(row=3, column=1)
        Button(root, command=helpME, text='Справка').grid(row=3, column=2)
        root.bind('<KeyPress-Return>',next)
        root.mainloop()

    def MakeSureYourName(rootForDestroy,username):
        def next():
            root2.destroy()
            try:
                os.mkdir('C:\\win31')
            except:
               messagebox.showerror('Нет винды!','Невозможно установить операционную систему Windows,не удается начать копирование файлов,попробуйте перезапустить установку Windows')
               sys.exit()
            f = open('C:\\win31\\username.txt','w')
            f.write(username)
            f.close()
            ApplicationInstallingNow = 'Календарь'
            FileInstallingNow = 'Calendar.exe'
            root3 = Tk()
            root4 = Toplevel()
            root3.title('Windows Setup')
            root4.title('Windows Setup')
            root4.geometry('+500+500')
            root4['bg'] = 'white'
            setupIcon = PhotoImage(file='images/setupIcon.png')
            setupLbl = Label(root4,image=setupIcon)
            setupLbl.grid(column=0)
            Label(root4,text='Добро пожаловать в Микрусофт(только из одного человека) Windows 3.1!\n\n-Если у Вас нет опыта работы с Windows, см. \"Краткое путешествие по Микрусофт Windows\" в книге \"Приступая к работе\".\n-Если вы уже работали с Windows, см. \"Новые возможности этой версии\" в книге \"Приступая к работе\"').grid(row=0,column=1)
            lblApplication = Label(root3,text='Копируем: %s' % ApplicationInstallingNow)
            lblApplication.grid(row=0,column=0)
            lblFile = Label(root3,text='Файл: %s' % FileInstallingNow)
            lblFile.grid(row=1,column=0)
            pb = ttk.Progressbar(root3, length=525)
            pb.grid(column=0, row=2,columnspan=4)
            Button(root3,text='Выход из Setup',command=lambda: sys.exit()).grid(row=3)
            pb.step(random.randint(4,12))
            time.sleep(1)
            root3.update()
            ApplicationInstallingNow = 'Файл менеджер'
            FileInstallingNow = 'File manager.exe'
            lblApplication['text'] = 'Копируем: %s' % ApplicationInstallingNow
            lblFile['text'] = 'Файл: %s' % FileInstallingNow
            root3.update_idletasks()
            pb.step(random.randint(4,12))
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
            Label(root5,text='Сейчас Setup может запустить\nкраткую обучающий текст, демонстрирующую основные навыки работы с Windows и мышью.\n\nКроме того, Вы можете, запустить Учебник и после установки Windows. ').grid(row=0,column=0)
            Button(root5,text='Запустить Учебник',command=lambda: webbrowser.open('https://www.pc-school.ru/rabota-s-myshyu-v-windows/')).grid(row=0,column=1)

            def lasts():
                lastIcon = Toplevel()
                lastIcon.title('Windows setup ends!')

                def restart():
                    os.mkdir('C:\\win31\\windowsSetupEnds')
                    root5.destroy()
                Button(lastIcon,text='Перезагрузить', command=restart).grid(row=0, column=0)
                Button(lastIcon,text='Вернуться в MS-DOS', command=lambda: os.startfile('C:\\Windows\\System32\\cmd.exe')).grid(row=0, column=1)
            Button(root5, text='Пропустить Учебник',command=lasts).grid(row=2,column=1)
            Button(root5, command=lambda: sys.exit(), text='Выход из Setup').grid(row=3,column=1)
            Button(root5, command=helpME, text='Справка').grid(row=4,column=1)
            root5.mainloop()

        def edit():
            root2.destroy()
            AskName()

        def helpME():
            helping = Toplevel()
            helping.geometry('0x0')
            helping.title('Справка')
            helping.mainloop()

        rootForDestroy.destroy()
        root2 = Tk()
        root2.title('Windows Setup')
        Label(root2,text='Убедитесь в правильности введенного Вами имени. Чтобы\nизменить его, выберите изменить. В противном случае,\nвыберите Продолжить.').grid(row=0,columnspan=4)
        Label(root2,text='Имя:      %s' % username).grid(row=1,column=0)
        Button(root2,text='Продолжить',command=next).grid(row=2,column=0)
        Button(root2, text='Изменить', command=edit).grid(row=2, column=1)
        Button(root2, command=lambda: sys.exit(), text='Выход из Setup').grid(row=2, column=2)
        Button(root2, command=helpME, text='Справка').grid(row=2, column=3)
        root2.mainloop()
    AskName()