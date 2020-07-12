from tkinter import *
import time
import sys
import os
import playsound
import psutil
from windows3_1_filemanager import DRIVE_LETTER_C
from windows3_1_filemanager import DRIVE_LETTER_D
from tkinter import messagebox
from tkinter.ttk import Combobox
import Windows3_1_setup
import windows3_1_run
import windows3_1_filemanager

Windows3_1_setup.setup()
if not os.path.exists(DRIVE_LETTER_C + 'win31\\windowsSetupEnds'):
    messagebox.showerror('',
                         'Не удалось установить Windows. Попробуйте перезапустить установку Windows')
    sys.exit()

DISK = 'C:'
free = psutil.disk_usage(DISK).free / (1024 * 1024 * 1024)
stop = False
root = Tk()
root.title('Starting...')
root.geometry('2000x1500')
startIcon = PhotoImage(file='images/startIcon.png')
Label(root, image=startIcon).place(x=500, y=375)
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
programmng.geometry('500x500')
IconProgramManager = PhotoImage(file='images/IconProgramManager.png')
forAccessories = PhotoImage(file='images/IconForAccessories.png')
aboutImg = PhotoImage(file='images/aboutImg.png')
thanksImg = PhotoImage(file='images/thanksImg.png')
titrsImg = PhotoImage(file='images/titrs.png')
filemngImg = PhotoImage(file='images/filemng.png')


def create():
    def nextcreate():
        try:
            def fileMenu(event):
                def dltFile():
                    group.grid_forget()
                    group.place_forget()
                    menuOffile.destroy()
                    os.rmdir('C:\\win31\\%s' % name)

                def movebutton():
                    global stop
                    stop = False

                    def movebutton2(event):
                        global stop

                        def stopmove():
                            global stop
                            stop = True

                        Okmovebtn = Button(menuOffile, command=stopmove, text='Ок')
                        Okmovebtn.grid(row=0, column=1)
                        if not stop:
                            group.place(x=event.x, y=event.y)

                    programmng.bind('<B1-Motion>', movebutton2)

                menuOffile = Toplevel()
                moveBtn = Button(menuOffile, text='Переместить', command=movebutton)
                moveBtn.grid()
                dltBtn = Button(menuOffile, text='Удалить', command=dltFile)
                dltBtn.grid()
                menuOffile.mainloop()

            def opencreatedfolder():
                def closeCreatedFolder():
                    global group
                    c.destroy()
                    group = Button(programmng, image=forAccessories, command=opencreatedfolder)
                    group.grid()

                group.grid_forget()
                group.grid_forget()
                group.grid_forget()
                group.grid_forget()

                def deiconfy2():
                    def iconfy():
                        c.deiconify()
                        group.grid_forget()

                    c.iconify()
                    group = Button(programmng, image=forAccessories, command=iconfy)
                    group.grid()

                def fullscreen2():
                    if fullscreenbutton2['text'] == '>':
                        c.geometry('2000x1500+0+0')
                        fullscreenbutton2['text'] = '<>'
                        deiconifybutton2.place(x=1850, y=0)
                        fullscreenbutton2.place(x=1870, y=0)
                    elif fullscreenbutton2['text'] == '<>':
                        c.geometry('500x500+0+0')
                        fullscreenbutton['text'] = '>'
                        deiconifybutton2.place(x=450, y=0)
                        fullscreenbutton2.place(x=470, y=0)

                c = Toplevel()
                c.title(name)
                menu2 = Menu(c)
                new_item2 = Menu(menu2, tearoff=0)
                new_item2.add_command(label='Закрыть', command=closeCreatedFolder)
                menu2.add_cascade(label='Меню', menu=new_item2)
                c.config(menu=menu2)
                c.geometry('500x500')
                deiconifybutton2 = Button(c, text='<', command=deiconfy2)
                deiconifybutton2.place(x=450, y=0)
                fullscreenbutton2 = Button(c, text='>', command=fullscreen2)
                fullscreenbutton2.place(x=470, y=0)
                c.mainloop()

            os.mkdir('C:\\win31\\%s' % o.get())
            name = os.path.basename('C:\\win31\\%s' % o.get())

            group = Button(programmng, image=forAccessories, command=opencreatedfolder)
            group.bind('<Button-3>', fileMenu)
            group.grid()
        except:
            playsound.playsound('CHORD.wav')
            messagebox.showerror('Невозможно', 'Невозможно сделать файл,проверте правильно ли введено имя файла')

    createTk = Toplevel()
    createTk.title('Свойства Группы программ')
    Label(createTk, text='Описание:').grid(row=0, column=0)
    Label(createTk, text='Файл группы:').grid(row=1, column=0)
    o = Entry(createTk)
    o.grid(row=0, column=1)
    f = Entry(createTk)
    f.grid(row=1, column=1)
    btn = Button(createTk, text='OK', state='disable', command=nextcreate)
    btn.grid(row=0, column=2)
    Button(createTk, text='Отменить', command=lambda: createTk.destroy()).grid(row=1, column=2)
    while True:
        createTk.update()
        createTk.update_idletasks()
        if o.get().rstrip() != '' and f.get().rstrip() != '' and '.GRP' in f.get():
            btn['state'] = 'normal'
        else:
            btn['state'] = 'disable'


def mainAccessories():
    def des():
        mainWindow.destroy()
        mainButton.grid()
        mainLbl.grid()

    def fullscreen2():
        if fullscreenbutton2['text'] == '>':
            mainWindow.geometry('2000x1500+0+0')
            fullscreenbutton2['text'] = '<>'
            deiconifybutton2.place(x=1850, y=0)
            fullscreenbutton2.place(x=1870, y=0)
        elif fullscreenbutton2['text'] == '<>':
            mainWindow.geometry('500x500+0+0')
            fullscreenbutton2['text'] = '>'
            deiconifybutton2.place(x=450, y=0)
            fullscreenbutton2.place(x=470, y=0)

    def deiconfy2():

        def iconfy():
            mainWindow.deiconify()
            mainButton2.grid_forget()
            mainLbl.grid_forget()

        mainWindow.iconify()
        mainButton2 = Button(programmng, image=forAccessories, command=iconfy)
        mainButton2.grid()
        mainLbl.grid()

    mainButton.grid_forget()
    mainLbl.grid_forget()
    mainWindow = Toplevel()
    mainWindow.geometry('500x500')
    mainWindow.title('Главный')
    deiconifybutton2 = Button(mainWindow, text='<', command=deiconfy2)
    deiconifybutton2.place(x=450, y=0)
    fullscreenbutton2 = Button(mainWindow, text='>', command=fullscreen2)
    fullscreenbutton2.place(x=470, y=0)
    filemng = Button(mainWindow, image=filemngImg, command=lambda: windows3_1_filemanager.main())
    filemng.grid()
    m = Menu(mainWindow, tearoff=False)
    ni3 = Menu(m)
    ni3.add_command(label='Выход', command=des)
    m.add_cascade(label='Закрыть', menu=ni3)
    mainWindow.config(menu=m)
    mainWindow.mainloop()


def fullscreen():
    if fullscreenbutton['text'] == '>':
        programmng.geometry('2000x1500+0+0')
        fullscreenbutton['text'] = '<>'
        deiconifybutton.place(x=1850, y=0)
        fullscreenbutton.place(x=1870, y=0)
    elif fullscreenbutton['text'] == '<>':
        programmng.geometry('500x500+0+0')
        fullscreenbutton['text'] = '>'
        deiconifybutton.place(x=450, y=0)
        fullscreenbutton.place(x=470, y=0)


def closed():
    closewindows = messagebox.askyesno('Конец сеанса', 'Вы действительно хотите завершить сеанс?')
    if closewindows == True:
        playsound.playsound('CHIMES.wav')
        sys.exit()
    else:
        pass


def deiconfy():
    def iconfy():
        programmng.deiconify()
        iconifyProgramManager.grid_forget()

    programmng.iconify()
    iconifyProgramManager = Button(desktop, image=IconProgramManager, command=iconfy)
    iconifyProgramManager.grid()


def run():
    windows3_1_run.startrun()


def about():
    aboutTk = Toplevel()
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
    searchTk = Toplevel()
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


def content():
    def autoarrange():
        tkk = Tk()
        tkk.title('Тут пусто,это тут не работает)')
        tkk.mainloop()

    contentTk = Toplevel()
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
mainButton = Button(programmng, image=forAccessories, command=mainAccessories)
mainButton.grid(row=0, column=0)
mainLbl = Label(programmng, text='Главный')
mainLbl.grid(row=0, column=1)
fullscreenbutton = Button(programmng, text='>', command=fullscreen)
fullscreenbutton.place(x=470, y=0)
programmng.title('Диспетчер программ')

menu = Menu(programmng)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Создать', command=create)
new_item.add_separator()
new_item.add_command(label='Выполнить', command=run)
new_item.add_separator()
new_item.add_command(label='Выход из Windows', command=closed)
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

programmng.protocol('WM_DELETE_WINDOW', closed)
desktop.geometry('2000x1500')
desktop.title('Windows 3.1!')
desktop['bg'] = 'light grey'
playsound.playsound('TADA.wav')
desktop.mainloop()
