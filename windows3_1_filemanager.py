from tkinter import *
from tkinter import messagebox
import os


def main():
    def des(event):
        filemng.destroy()
    messagebox.showinfo('','Нажмите F4 чтобы выйти из приложения')

    def detectfiles(event):
        try:
            files2 = 'C:\\' + event.widget.cget('text')
            files2 = os.listdir(files2)
            for d in range(len(files2)):
                btn2 = Button(filemng,text=files2[d],command=lambda: messagebox.showerror('','Не удалось открыть файл'))
                btn2.grid()
        except:
            messagebox.showerror('','Отказано в доступе')
    filemng = Toplevel()
    filemng.title('Диспетчер Файлов')
    files = os.listdir('C:\\')
    for i in range(len(files)):
        btn = Button(filemng,text=files[i])
        btn.grid()
        btn.bind('<Button-1>',detectfiles)
    Label(filemng,text='----------------------------------------------------------').grid()
    filemng.bind('<F4>',des)
    filemng.mainloop()