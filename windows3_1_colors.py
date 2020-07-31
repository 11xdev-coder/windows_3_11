from tkinter import *


def iconfy(root, iconifybutton):
    root.deiconify()
    iconifybutton.grid_forget()


def deiconfy(root, cp):
    root.iconify()
    iconfybutton = Button(cp, text='images/colors.png', command=lambda: iconfy(root, iconfybutton))
    iconfybutton.grid(row=0, column=0)


def fullscreen(root, ra, deiconifybutton, fullscreenbutton, screen_width):
    if fullscreenbutton['text'] == '>':
        root.geometry(ra + '+0+0')
        fullscreenbutton['text'] = '<>'
        deiconifybutton.place(x=screen_width - 65, y=0)
        fullscreenbutton.place(x=screen_width - 40, y=0)
    elif fullscreenbutton['text'] == '<>':
        root.geometry('500x500')
        fullscreenbutton['text'] = '>'
        deiconifybutton.place(x=450, y=0)
        fullscreenbutton.place(x=470, y=0)


def selectbg():
    root2 = Toplevel()

    root2.mainloop()


def main(colors, cp):
    bgImg = PhotoImage(file='images/background.png')

    def des(event):
        root.destroy()
        colors.grid(row=0, column=0)

    root = Toplevel()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    ra = '%sx%s' % (screen_width, screen_height)
    root.title('Цвета')
    root.geometry('500x500')
    bg = Button(root, image=bgImg, command=selectbg)
    deiconifybutton = Button(root, text='<', command=lambda: deiconfy(root, cp))
    deiconifybutton.place(x=450, y=0)
    fullscreenbutton = Button(root, text='>',
                              command=lambda: fullscreen(root, ra, deiconifybutton, fullscreenbutton, screen_width))
    fullscreenbutton.place(x=470, y=0)
    m = Menu(root, tearoff=0)
    ni3 = Menu(m)
    ni3.add_command(label='Выход', command=lambda: des(''))
    m.add_cascade(label='Закрыть', menu=ni3)
    root.config(menu=m)
    root.bind('<Control-F4>', des)
    root.mainloop()
