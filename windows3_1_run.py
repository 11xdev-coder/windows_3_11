from tkinter import *

def startrun():
    def running():
        if e.get() == 'winver':
            about = Toplevel()
            about.title('')
            Label(about,image=IconAboutWin).grid()
            Button(about,text='OK',width=50,command=lambda: about.destroy()).grid()
            about.mainloop()
    runTk = Toplevel()
    IconAboutWin = PhotoImage(file='IconAboutWin.png')
    runTk.title('Выполнить')
    Label(runTk,text='Командная строка').grid()
    e = Entry(runTk)
    e.grid()
    Label(runTk,text='                      ').grid(row=0,column=1)
    btn = Button(runTk,command=running,text='OK',state='disable')
    btn.grid(row=0,column=2)
    Button(runTk, command=lambda: runTk.destroy(), text='Отмена').grid(row=1, column=2)
    while True:
        runTk.update()
        runTk.update_idletasks()
        if e.get().rstrip() != '':
            btn['state'] = 'normal'
        else:
            btn['state'] = 'disable'
