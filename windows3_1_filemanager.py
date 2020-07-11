from tkinter import *
from tkinter import messagebox
import os

DRIVE_LETTER_C = 'C:\\'
DRIVE_LETTER_D = 'D:\\'

def main():
    def detectfiles(event):
        try:
            files2 = DRIVE_LETTER_C + event.widget.cget('text')
            files2 = os.listdir(files2)
            for d in range(len(files2)):
                btn2 = Button(filemng, text=files2[d],
                              command=lambda: messagebox.showerror('', 'Не удалось открыть файл'))
                btn2.grid()
        except:
            messagebox.showerror('', 'Отказано в доступе')

    filemng = Toplevel()
    filemng.title('Диспетчер Файлов')
    files = os.listdir('C:\\')
    for i in range(len(files)):
        btn = Button(filemng, text=files[i])
        btn.grid()
        btn.bind('<Button-1>', detectfiles)
    Label(filemng, text='----------------------------------------------------------').grid()
    m = Menu(filemng,tearoff=False)
    ni3 = Menu(m)
    ni3.add_command(label='Выход', command=lambda: filemng.destroy())
    m.add_cascade(label='Закрыть', menu=ni3)
    filemng.config(menu=m)
    filemng.mainloop()
