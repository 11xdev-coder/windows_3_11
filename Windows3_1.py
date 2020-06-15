from tkinter import *
import time
import sys
import os
import playsound
from tkinter import messagebox
from windows31 import Windows3_1_setup
from windows31 import windows3_1_run

Windows3_1_setup.setup()
if not os.path.exists('C:\\win31\\windowsSetupEnds'):
    messagebox.showerror('','Не удалось установить Windows. Попробуйте перезапустить установку Windows')
    sys.exit()

root = Tk()
root.title('Starting...')
root.geometry('2000x1500')
startIcon = PhotoImage(file='startIcon.png')
Label(root,image=startIcon).place(x=500,y=375)
for r in range(15):
    root.update()
    root.update_idletasks()
    time.sleep(0.1)
playsound.playsound('CHORD.wav')
messagebox.showerror('Не поддерживается драйвер ShowNamesOfCreatedFolders','Не поддерживается драйвер ShowNamesOfCreatedFolders и поэтому имена папок которые вы сделали не будут показываться!')
root.destroy()
desktop = Tk()
programmng = Toplevel()
programmng.geometry('500x500')
IconProgramManager = PhotoImage(file='IconProgramManager.png')
forAccessories = PhotoImage(file='IconForAccessories.png')


def create():
    def nextcreate():
        try:
            def fileMenu(event):

                def movebutton():
                    
                    def movebutton2(event):
                        group.place(x=event.x,y=event.y)
                    programmng.bind('<Motion>',movebutton2)
                menuOffile = Toplevel()
                moveBtn = Button(menuOffile,text='Переместить',command=movebutton)
                moveBtn.grid()
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
                        iconifyCreatedFolder.grid_forget()

                    c.iconify()
                    iconifyCreatedFolder = Button(programmng, image=forAccessories, command=iconfy)
                    iconifyCreatedFolder.grid()

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

            group = Button(programmng,image=forAccessories,command=opencreatedfolder)
            group.bind('<Button-3>',fileMenu)
            group.grid()
        except:
            playsound.playsound('CHORD.wav')
            messagebox.showerror('Невозможно','Невозможно сделать файл,проверте правильно ли введено имя файла')
    createTk = Toplevel()
    createTk.title('Свойства Группы программ')
    Label(createTk,text='Описание:').grid(row=0,column=0)
    Label(createTk,text='Файл группы:').grid(row=1,column=0)
    o = Entry(createTk)
    o.grid(row=0,column=1)
    f = Entry(createTk)
    f.grid(row=1,column=1)
    btn = Button(createTk,text='OK',state='disable',command=nextcreate)
    btn.grid(row=0,column=2)
    Button(createTk,text='Отменить',command=lambda: createTk.destroy()).grid(row=1,column=2)
    while True:
        createTk.update()
        createTk.update_idletasks()
        if o.get().rstrip() != '' and f.get().rstrip() != '' and '.GRP' in f.get():
            btn['state'] = 'normal'
        else:
            btn['state'] = 'disable'

def mainAccessories():
    mainWindow = Toplevel()
    mainWindow.mainloop()


def fullscreen():
    if fullscreenbutton['text'] == '>':
        programmng.geometry('2000x1500+0+0')
        fullscreenbutton['text'] = '<>'
        deiconifybutton.place(x=1850,y=0)
        fullscreenbutton.place(x=1870,y=0)
    elif fullscreenbutton['text'] == '<>':
        programmng.geometry('500x500+0+0')
        fullscreenbutton['text'] = '>'
        deiconifybutton.place(x=450, y=0)
        fullscreenbutton.place(x=470, y=0)


def closed():
    closewindows = messagebox.askyesno('Конец сеанса','Вы действительно хотите завершить сеанс?')
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
    iconifyProgramManager = Button(desktop,image=IconProgramManager,command=iconfy)
    iconifyProgramManager.grid()

def run():
    windows3_1_run.startrun()


deiconifybutton = Button(programmng,text='<',command=deiconfy)
deiconifybutton.place(x=450,y=0)
mainButton = Button(programmng,image=forAccessories,command=mainAccessories)
mainButton.grid(row=0,column=0)
Label(programmng,text='Главный').grid(row=0,column=1)
fullscreenbutton = Button(programmng,text='>',command=fullscreen)
fullscreenbutton.place(x=470,y=0)
programmng.title('Диспетчер программ')

menu = Menu(programmng)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Создать', command=create)
new_item.add_separator()
new_item.add_command(label='Выполнить', command=run)
menu.add_cascade(label='Файл', menu=new_item)
programmng.config(menu=menu)

programmng.protocol('WM_DELETE_WINDOW',closed)
desktop.geometry('2000x1500')
desktop.title('Windows 3.1!')
desktop['bg'] = 'light grey'
playsound.playsound('TADA.wav')
desktop.mainloop()