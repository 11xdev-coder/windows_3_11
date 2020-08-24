from tkinter import *
import HoverInfo
import math


def iconfy(root, iconifybutton):
    root.deiconify()
    iconifybutton.grid_forget()


def deiconfy(root, cp):
    colorsimg = PhotoImage(file='images/colors.png')
    root.iconify()
    iconfybutton = Button(cp, image=colorsimg, command=lambda: iconfy(root, iconfybutton))
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


def takebg(MainCanvas, bgForCanvas, screen_width, screen_height):
    w = bgForCanvas.width()
    h = bgForCanvas.height()
    for x in range(math.floor(screen_width / 10)):
        for y in range(math.floor(screen_height / 10)):
            MainCanvas.create_image(x * w, y * h, image=bgForCanvas, anchor=NW)
    MainCanvas['bg'] = 'green'
    currentUser = open('.\\win31\\users\\currentUser.txt')
    currentBg = open('.\\win31\\users\\%s\\currentBg.txt' % currentUser.readline(), 'w')
    currentBg.write('bg1.png')
    currentBg.close()
    currentUser.close()
    MainCanvas.update()
    MainCanvas.update_idletasks()


def selectbg1(cnvs, screen_width, screen_height, bg1):
    bg1.grid_forget()
    def des(event):
        root2.destroy()
        bg1.grid(row=0, column=0)
    bg1img = PhotoImage(file='images/bg1.png')
    root2 = Toplevel()
    root2.title('Фон')
    Label(root2, text='Выберите фон').grid()
    btn1 = Button(root2, image=bg1img, command=lambda: takebg(cnvs, bg1img, screen_width, screen_height))
    btn1.grid(row=1)
    m2 = Menu(root2, tearoff=0)
    ni4 = Menu(m2)
    ni4.add_command(label='Выход', command=lambda: des(''))
    m2.add_cascade(label='Закрыть', menu=ni4)
    root2.config(menu=m2)
    root2.bind('<Control-F4>', des)
    root2.mainloop()


def main(colors, cp, canvas):
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
    bg1 = Button(root, image=bgImg, command=lambda: selectbg1(canvas, screen_width, screen_height,bg1))
    hover = HoverInfo.HoverInfo(bg1, 'Select a background')
    bg1.grid(row=0, column=0)
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
