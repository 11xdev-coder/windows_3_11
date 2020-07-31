from tkinter import *
import windows3_1_colors


def iconfy(root, cpButton):
    root.deiconify()
    cpButton.grid_forget()


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


def deiconfy(root, mainWindow):
    root.iconify()
    cpButton = Button(mainWindow, command=lambda: iconfy(root, cpButton), text='images/control_panel.png')
    cpButton.grid(row=0, column=1)


def des(cp, root):
    root.destroy()
    cp.grid(row=0, column=1)


def colorsstart(colors, cp):
    colors.grid_forget()
    windows3_1_colors.main(colors, cp)


def main(cp, mainWindow):
    def des2(event):
        root.destroy()
        cp.grid(row=0, column=1)

    root = Toplevel()
    root.title('Панель задач')
    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()
    ra = '%sx%s' % (screen_width, screen_height)
    root.geometry('500x500')
    deiconifybutton = Button(root, text='<', command=lambda: deiconfy(root, mainWindow))
    deiconifybutton.place(x=450, y=0)
    fullscreenbutton = Button(root, text='>',
                              command=lambda: fullscreen(root, ra, deiconifybutton, fullscreenbutton, screen_width))
    fullscreenbutton.place(x=470, y=0)
    colors = Button(root, text='images/colors.png', command=lambda: colorsstart(colors, root))
    colors.grid(row=0, column=0)
    m = Menu(root, tearoff=0)
    ni3 = Menu(m)
    ni3.add_command(label='Выход', command=lambda: des(cp, root))
    m.add_cascade(label='Закрыть', menu=ni3)
    root.config(menu=m)
    root.bind('<Control-F4>', des2)
    root.mainloop()
