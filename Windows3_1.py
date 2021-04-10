import os
import sys
import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import playsound
import psutil
import pygame
from PIL import Image, ImageTk

import Windows3_1_setup
import windows3_1_control_panel
import windows3_1_filemanager
import windows3_1_run

pygame.init()

rot = Tk()
screen_width = rot.winfo_screenwidth()
screen_height = rot.winfo_screenheight()
ra = '%sx%s' % (screen_width, screen_height)
rot.destroy()

Windows3_1_setup.setup()
if not os.path.exists('win31/windowsSetupEnds'):
    messagebox.showerror('',
                         'Не удалось установить Windows. Попробуйте перезапустить установку Windows')
    sys.exit()

DISK = 'C:'
free = psutil.disk_usage(DISK).free / (1024 * 1024 * 1024)
stop = False
root = Tk()
root.title('Starting...')
root.overrideredirect(1)
root.geometry(ra)
startIcon = PhotoImage(file='images/startIcon.png')
Label(root, image=startIcon).place(x=screen_width / 2, y=screen_height / 2)
for r in range(15):
    root.update()
    root.update_idletasks()
    time.sleep(0.1)
playsound.playsound('CHORD.wav')
messagebox.showerror('Не поддерживается драйвер ShowNamesOfCreatedFolders',
                     'Не поддерживается драйвер ShowNamesOfCreatedFolders и поэтому имена папок которые вы сделали не будут показываться!')
root.destroy()
desktop = Tk()
programmng = Toplevel()
programmng.iconbitmap("bitmap_images/WINTU002.ICO")
programmng.wm_attributes('-topmost', 1)
programmng.geometry('500x500')
IconProgramManager = PhotoImage(file='images/IconProgramManager.png')
forAccessories = PhotoImage(file='images/IconForAccessories.png')
aboutImg = PhotoImage(file='images/aboutImg.png')
thanksImg = PhotoImage(file='images/thanksImg.png')
titrsImg = PhotoImage(file='images/titrs.png')
filemngImg = PhotoImage(file='images/filemng.png')
cursorImg = PhotoImage(file='images/cursor.png')
imgcp = Image.open('images/control_panel.png')
imgcp = imgcp.resize((104, 74), Image.ANTIALIAS)
cpimg = ImageTk.PhotoImage(imgcp)
desktop.overrideredirect(1)


def moveCursor(event):
    cursor.place(x=event.x, y=event.y)


canvas = Canvas(desktop, width=screen_width, height=screen_height, bg='light grey')
cursor = Label(desktop, image=cursorImg)
canvas.bind('<Motion>', moveCursor)
canvas.grid_propagate(False)
canvas.grid()


def moveCursor2(event):
    cursor2.place(x=event.x, y=event.y)


cursor2 = Label(programmng, image=cursorImg)
programmng.bind('<Motion>', moveCursor2)


def iconfy3(c, group):
    c.deiconify()
    group.grid_forget()


def deiconfy3(c):
    c.iconify()
    group = Button(programmng, image=forAccessories, command=lambda: iconfy3(c, group))
    group.grid()


def fullscreen3(fullscreenbutton2, c, deiconifybutton2):
    if fullscreenbutton2['text'] == '>':
        c.geometry('%s+0+0' % ra)
        fullscreenbutton2['text'] = '<>'
        deiconifybutton2.place(x=screen_width - 65, y=0)
        fullscreenbutton2.place(x=screen_width - 40, y=0)
    elif fullscreenbutton2['text'] == '<>':
        c.geometry('500x500+0+0')
        fullscreenbutton2['text'] = '>'
        deiconifybutton2.place(x=450, y=0)
        fullscreenbutton2.place(x=470, y=0)


def opencreatedfolder(group, name):
    group.grid_forget()
    group.grid_forget()
    group.grid_forget()
    group.grid_forget()

    def closeCreatedFolder(event):
        c.destroy()
        group.grid()

    c = Toplevel()
    c.bind('<Control-F4>', closeCreatedFolder)
    c.title(name)
    menu2 = Menu(c)
    new_item2 = Menu(menu2, tearoff=0)
    new_item2.add_command(label='Закрыть', command=lambda: closeCreatedFolder(''))
    menu2.add_cascade(label='Меню', menu=new_item2)
    c.config(menu=menu2)
    c.geometry('500x500')
    deiconifybutton2 = Button(c, text='<', command=lambda: deiconfy3(c))
    deiconifybutton2.place(x=450, y=0)
    fullscreenbutton2 = Button(c, text='>', command=lambda: fullscreen3(fullscreenbutton2, c, deiconifybutton2))
    fullscreenbutton2.place(x=470, y=0)
    c.mainloop()


def dltFile(group, menuOffile, name):
    group.grid_forget()
    group.place_forget()
    menuOffile.destroy()
    currentUser2 = open('.\\win31\\users\\currentUser.txt', 'r')
    os.rmdir('.\\win31\\users\\%s\\%s' % (currentUser2.readline(), name))


def stopmove():
    global stop
    stop = True


def movebutton(group, menuOffile):
    global stop
    stop = False

    def movebutton2(event):
        global stop
        Okmovebtn = Button(menuOffile, command=stopmove, text='Ок')
        Okmovebtn.grid(row=0, column=1)
        if not stop:
            group.place(x=event.x, y=event.y)

    programmng.bind('<B1-Motion>', movebutton2)


def nextcreate(o):
    try:
        def fileMenu(event):
            menuOffile = Toplevel()
            moveBtn = Button(menuOffile, text='Переместить', command=lambda: movebutton(group, menuOffile))
            moveBtn.grid()
            dltBtn = Button(menuOffile, text='Удалить', command=lambda: dltFile(group, menuOffile, name))
            dltBtn.grid()
            menuOffile.mainloop()

        currentUser = open('.\\win31\\users\\currentUser.txt', 'r')
        os.mkdir('.\\win31\\users\\%s\\%s' % (currentUser.readline(), o.get()))
        name = os.path.basename('.\\win31\\users\\%s\\%s' % (currentUser.readline(), o.get()))

        group = Button(programmng, image=forAccessories, command=lambda: opencreatedfolder(group, name))
        group.bind('<Button-3>', fileMenu)
        group.grid()
    except:
        playsound.playsound('CHORD.wav')
        messagebox.showerror('Невозможно', 'Невозможно сделать файл,проверте правильно ли введено имя файла')


def create():
    def des(event):
        createTk.destroy()

    createTk = Toplevel()
    createTk.bind('<Control-F4>', des)
    createTk.title('Свойства Группы программ')
    Label(createTk, text='Описание:').grid(row=0, column=0)
    Label(createTk, text='Файл группы:').grid(row=1, column=0)
    o = Entry(createTk)
    o.grid(row=0, column=1)
    f = Entry(createTk)
    f.grid(row=1, column=1)
    btn = Button(createTk, text='OK', state='disable', command=lambda: nextcreate(o))
    btn.grid(row=0, column=2)
    Button(createTk, text='Отменить', command=lambda: createTk.destroy()).grid(row=1, column=2)
    while True:
        createTk.update()
        createTk.update_idletasks()
        if o.get().rstrip() != '' and f.get().rstrip() != '' and '.GRP' in f.get():
            btn['state'] = 'normal'
        else:
            btn['state'] = 'disable'


def des(mainwindow):
    mainwindow.destroy()
    mainButton.grid()
    mainLbl.grid()


def fullscreen2(fullscreenbutton2, deiconifybutton2, mainWindow):
    if fullscreenbutton2['text'] == '>':
        mainWindow.geometry(ra + '+0+0')
        fullscreenbutton2['text'] = '<>'
        deiconifybutton2.place(x=1850, y=0)
        fullscreenbutton2.place(x=1875, y=0)
    elif fullscreenbutton2['text'] == '<>':
        mainWindow.geometry('500x500+0+0')
        fullscreenbutton2['text'] = '>'
        deiconifybutton2.place(x=450, y=0)
        fullscreenbutton2.place(x=470, y=0)


def filemngstart(filemng, mainWindow):
    filemng.grid_forget()
    windows3_1_filemanager.main(mainWindow, filemng)


def iconfy2(mainWindow, mainButton2):
    mainWindow.deiconify()
    mainButton2.grid_forget()
    mainLbl.grid_forget()


def deiconfy2(mainWindow):
    mainWindow.iconify()
    mainButton2 = Button(programmng, image=forAccessories, command=lambda: iconfy2(mainWindow, mainButton2))
    mainButton2.grid()
    mainLbl.grid()


def control_panel_start(cp, mainWindow, cnvs):
    cp.grid_forget()
    windows3_1_control_panel.main(cp, mainWindow, canvas)


def mainAccessories():
    mainButton.grid_forget()
    mainLbl.grid_forget()
    mainWindow = Toplevel()
    mainWindow.geometry('500x500')
    mainWindow.title('Главный')
    deiconifybutton2 = Button(mainWindow, text='<', command=lambda: deiconfy2(mainWindow))
    deiconifybutton2.place(x=450, y=0)
    fullscreenbutton2 = Button(mainWindow, text='>',
                               command=lambda: fullscreen2(fullscreenbutton2, deiconifybutton2, mainWindow))
    fullscreenbutton2.place(x=470, y=0)
    filemng = Button(mainWindow, image=filemngImg, command=lambda: filemngstart(filemng, mainWindow))
    filemng.grid()
    cp = Button(mainWindow, image=cpimg, command=lambda: control_panel_start(cp, mainWindow, canvas))
    cp.grid(column=1, row=0)
    m = Menu(mainWindow, tearoff=0)
    ni3 = Menu(m)
    ni3.add_command(label='Выход', command=lambda: des(mainWindow))
    m.add_cascade(label='Закрыть', menu=ni3)
    mainWindow.config(menu=m)
    mainWindow.mainloop()


def fullscreen():
    if fullscreenbutton['text'] == '>':
        programmng.geometry('%s+0+0' % ra)
        fullscreenbutton['text'] = '<>'
        deiconifybutton.place(x=screen_width - 65, y=0)
        fullscreenbutton.place(x=screen_width - 40, y=0)
    elif fullscreenbutton['text'] == '<>':
        programmng.geometry('500x500+0+0')
        fullscreenbutton['text'] = '>'
        deiconifybutton.place(x=450, y=0)
        fullscreenbutton.place(x=470, y=0)


def closed(event):
    closewindows = messagebox.askyesno('Конец сеанса', 'Вы действительно хотите завершить сеанс?')
    if closewindows == True:
        playsound.playsound('CHIMES.wav')
        desktop.destroy()
        sys.exit()
    else:
        pass


def iconfy(iconifyProgramManager):
    programmng.deiconify()
    iconifyProgramManager.grid_forget()


def deiconfy():
    programmng.iconify()
    iconifyProgramManager = Button(canvas, image=IconProgramManager, command=lambda: iconfy(iconifyProgramManager))
    iconifyProgramManager.grid()


def run():
    windows3_1_run.startrun()


def about():
    def diss(event):
        aboutTk.destroy()

    aboutTk = Toplevel()
    aboutTk.bind('<Control-F4>', diss)
    th = Label(aboutTk, image=thanksImg)
    th2 = Label(aboutTk, text='Спасибо вам за то, что нашли эту пасхалку и тестируете мою Версию Windows')
    titrs = Label(aboutTk, image=titrsImg)

    def thanks(event):
        th.grid()
        th2.grid(row=1, column=1)
        titrs.grid_forget()

    def titres(event):
        th.grid_forget()
        th2.grid_forget()
        titrs.grid()

    img = Label(aboutTk, image=aboutImg)
    img.grid()
    Label(aboutTk,
          text='Майкрософт Windows Диспетчер программ \nВерсия 3.11 \nАвторское право @ 2020 Майкрософт Корп. \nЭтот продукт имеет лицензию на: \nВы. \n\nВаш серийный номер указан на внутренней стороне задней \nобложки руководства по началу работы с Майкрософт Windows. \nСтандартный режим \nПамять: %s' % int(
              free) + str('GB')).grid(row=0, column=1, columnspan=2)
    Button(aboutTk, text='OK', command=lambda: aboutTk.destroy()).grid(row=0, column=3)
    img.bind('<Double-Button-1>', thanks)
    img.bind('<Triple-Button-1>', titres)
    aboutTk.mainloop()


def search():
    def dys(event):
        searchTk.destroy()

    searchTk = Toplevel()
    searchTk.bind('<Control-F4>', dys)
    searchTk.title('Поиск')
    Label(searchTk, text='Введите слово или выберите его из списка. Затем выберите Показать темы').grid()
    c = Combobox(searchTk)
    c['values'] = (
        'приложения', 'упорядочивание', 'изменение', 'копирование', 'создание', 'удаление', 'документы', 'иконки',
        'группы',
        'перемещение')
    c.current(0)
    Entry(searchTk).grid()
    c.grid(column=0, row=2)
    Button(searchTk, text='Отменить', command=lambda: searchTk.destroy()).grid(row=0, column=1)
    Button(searchTk, text='Показать темы', command=lambda: messagebox.showerror('', 'Не удалось найти тему')).grid(
        row=1, column=1)
    Label(searchTk, text='выберите тему, затем выберите Перейти к').grid(row=3, column=0)
    Button(searchTk, text='Перейти К').grid(row=2, column=1)
    searchTk.mainloop()


def autoarrange():
    tkk = Tk()
    tkk.title('Тут пусто,это тут не работает)')
    tkk.mainloop()


def content():
    def dos(event):
        contentTk.destroy()

    contentTk = Toplevel()
    contentTk.bind('<Control-F4>', dos)
    contentTk.title('Справка - Диспетчер программ')
    Button(contentTk, text='Назад', command=lambda: contentTk.destroy()).grid()
    text = Text(contentTk, height=10)
    text.insert(END,
                'Содержание Справки Диспетчера Программ\nДиспетчер программ Windows - это инструмент,\n с помощью которого можно легко запускать \n приложения и организовывать приложения \n и файлы в логические группы.\nКак...')
    text.grid(columnspan=10)
    Button(contentTk, text='Упорядочить окна и значки', command=autoarrange).grid()
    contentTk.mainloop()


deiconifybutton = Button(programmng, text='<', command=deiconfy)
deiconifybutton.place(x=450, y=0)
fullscreenbutton = Button(programmng, text='>', command=fullscreen)
fullscreenbutton.place(x=470, y=0)
mainButton = Button(programmng, image=forAccessories, command=mainAccessories)
mainButton.grid(row=0, column=0)
mainLbl = Label(programmng, text='Главный')
mainLbl.grid(row=0, column=1)
programmng.title('Диспетчер программ')

menu = Menu(programmng)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Создать', command=create)
new_item.add_separator()
new_item.add_command(label='Выполнить', command=run)
new_item.add_separator()
new_item.add_command(label='Выход из Windows',
                     command=lambda: closed('<KeyPress event state=Control|Mod1 keysym=F4 keycode=115 x=93 y=50>'))
menu.add_cascade(label='Файл', menu=new_item)
new_item2 = Menu(menu, tearoff=0)
new_item2.add_checkbutton(label='Автоупорядочивание')
new_item2.add_checkbutton(label='Сворачивать при работе')
new_item2.add_checkbutton(label='Сохранять параметры при выходе')
menu.add_cascade(label='Параметры', menu=new_item2)
new_item3 = Menu(menu, tearoff=0)
new_item3.add_command(label='Содержание', command=content)
new_item3.add_command(label='Поиск справки по', command=search)
new_item3.add_command(label='О диспетчере программ', command=about)
menu.add_cascade(label='Справка', menu=new_item3)
programmng.config(menu=menu)

programmng.protocol('WM_DELETE_WINDOW',
                    lambda: closed('<KeyPress event state=Control|Mod1 keysym=F4 keycode=115 x=93 y=50>'))
programmng.bind('<Control-F4>', closed)
desktop.geometry(ra)
desktop.title('Windows 3.1!')
desktop['bg'] = 'light grey'
playsound.playsound('TADA.wav')
desktop.mainloop()
