from tkinter import *


def running(e, IconAboutWin):
    if e.get() == 'winver':
        about = Toplevel()
        about.title('')
        Label(about, image=IconAboutWin).grid()
        Button(about, text='OK', width=50, command=lambda: about.destroy()).grid()
        about.mainloop()


def startrun():
    def des(event):
        runTk.destroy()

    runTk = Toplevel()
    IconAboutWin = PhotoImage(file='images/IconAboutWin.png')
    runTk.title('Выполнить')
    Label(runTk, text='Командная строка').grid()
    e = Entry(runTk)
    e.grid()
    Label(runTk, text='                      ').grid(row=0, column=1)
    btn = Button(runTk, command=lambda: running(e, IconAboutWin), text='OK', state='disable')
    btn.grid(row=0, column=2)
    Button(runTk, command=lambda: runTk.destroy(), text='Отмена').grid(row=1, column=2)
    runTk.bind('<Control-F4>', des)
    while True:
        runTk.update()
        runTk.update_idletasks()
        if e.get().rstrip() != '':
            btn['state'] = 'normal'
        else:
            btn['state'] = 'disable'
