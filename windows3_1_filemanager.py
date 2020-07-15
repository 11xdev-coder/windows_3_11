from tkinter import *
from tkinter import messagebox
import os
import ctypes

DRIVE_LETTER_C = 'C:\\'
DRIVE_LETTER_D = 'D:\\'
labelText = ''
tk = Tk()
screen_width = tk.winfo_screenwidth()
screen_height = tk.winfo_screenheight()
ra = '%sx%s' % (screen_width, screen_height)
tk.destroy()


def _has_hidden_attribute(filepath):
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(filepath)
        assert attrs != -1
        result = bool(attrs & 2)
    except (AttributeError, AssertionError):
        result = False
    return result


def fullscreen(fullscreenbutton2, deiconifybutton2, filemng3):
    if fullscreenbutton2['text'] == '>':
        filemng3.geometry('%s+0+0' % ra)
        fullscreenbutton2['text'] = '<>'
        deiconifybutton2.place(x=screen_width - 65, y=0)
        fullscreenbutton2.place(x=screen_width - 40, y=0)
    elif fullscreenbutton2['text'] == '<>':
        filemng3.geometry('500x500+0+0')
        fullscreenbutton2['text'] = '>'
        deiconifybutton2.place(x=450, y=0)
        fullscreenbutton2.place(x=470, y=0)


def deiconfy(filemng3, root, imageFilemng):
    def iconfy():
        filemng3.deiconify()
        filemngBtn.grid_forget()

    filemng3.iconify()
    filemngBtn = Button(root, command=iconfy, image=imageFilemng)
    filemngBtn.grid()


def main(root, btn):
    filemngImg = PhotoImage(file='images/filemng.png')

    filemng2 = Toplevel()
    filemng2.geometry('500x500')
    filemng2.title('Диспетчер Файлов')
    deiconifybutton = Button(filemng2, text='<', command=lambda: deiconfy(filemng2, root, filemngImg))
    deiconifybutton.place(x=450, y=0)
    fullscreenbutton = Button(filemng2, text='>',
                              command=lambda: fullscreen(fullscreenbutton, deiconifybutton, filemng2))
    fullscreenbutton.place(x=470, y=0)

    def с(btn2):
        def des():
            btn2.grid()
            filemng2.destroy()

        def detectfiles(event):
            global labelText
            labelText = ''
            try:
                files2 = DRIVE_LETTER_C + event.widget.cget('text')
                files2 = os.listdir(files2)
                for d in range(len(files2)):
                    labelText += files2[d] + '\n'
                detectfiles2 = Toplevel()
                m2 = Menu(detectfiles2, tearoff=0)
                ni32 = Menu(m2)
                ni32.add_command(label='Выход', command=lambda: detectfiles2.destroy())
                m2.add_cascade(label='Закрыть', menu=ni32)
                detectfiles2.config(menu=m2)
                detectfiles2.title(DRIVE_LETTER_C + event.widget.cget('text'))
                detectfiles2.pack_propagate(False)
                vscrollbar = Scrollbar(detectfiles2, orient=VERTICAL)
                hscrollbar = Scrollbar(detectfiles2, orient=HORIZONTAL)
                vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
                hscrollbar.pack(fill=X, side=BOTTOM, expand=FALSE)
                canvas = Canvas(detectfiles2, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set, width=2000,
                                height=1200)
                canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
                canvas.config(scrollregion="0 0 2000 1200")
                canvas.create_text(100, 50, text=labelText)
                vscrollbar.config(command=canvas.yview)
                hscrollbar.config(command=canvas.xview)
            except:
                messagebox.showerror('', 'Отказано в доступе')

        files = os.listdir(DRIVE_LETTER_C)
        for i in range(len(files)):
            if _has_hidden_attribute(DRIVE_LETTER_C + files[i]):
                continue
            btn = Button(filemng2, text=files[i])
            btn.grid()
            btn.bind('<Button-1>', detectfiles)
        m = Menu(filemng2, tearoff=0)
        ni3 = Menu(m)
        ni3.add_command(label='Выход', command=des)
        m.add_cascade(label='Закрыть', menu=ni3)
        filemng2.config(menu=m)
        filemng2.mainloop()

    с(btn)
