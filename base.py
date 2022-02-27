# 使用图形化页面库
import tkinter as tk
# base64转换库
import base64

# 显示程序名称和制作者
window = tk.Tk()
window.title('base64转换器-面包amd牛奶')
# 页面长宽度
window.geometry('400x250')
var = tk.StringVar()

# 设置输入框；如果是密码形式设置show='#'
e = tk.Entry(window,show=None)
e.pack()

# base64转图片
def b64topic(var):
    with open(var, "rb") as f:
        picdata = base64.b64decode(f.read())
        pic = open("base64.png", "wb")
        pic.write(picdata)
        pic.close()
        var = input()
        b64topic(var)

#图片转base64
def pictob64(var):
    with open(var, "rb") as f:
        b64 = base64.b64encode(f.read())
        print(str(b64, "utf8"))
        t = open("picto.txt", "wt")
        t.write(str(b64, "utf8"))
        t.close()
        var = input()
        pictob64(var)

#Base64转rar
def b64decode(var):
    r=base64.b64decode(var)
    #打包
    test_file=open("flag.rar","wb")
    test_file.write(r)
    test_file.close()


# 设置页面按钮，base64转图片
def ba64topic():
    global t
    var = e.get()
    b64topic(var)
#页面布局设置；bg是颜色，width是宽度，height是高度，pady是y轴间距，font字体参数,来控制控件上显示的字体,大小和样式
b1 = tk.Button(window, text='base64转图片', bg="grey",font=('Arial',12),width=15,height=2,pady=2,command=ba64topic)
b1.pack()

# 设置页面按钮，图片转base64
def pictoba64():
    global t
    var = e.get()
    pictob64(var)
#页面布局设置；bg是颜色，width是宽度，height是高度，pady是y轴间距，font字体参数,来控制控件上显示的字体,大小和样式
b2 = tk.Button(window, text='图片转base64',bg="grey",font=('Arial',12),width=15,height=2,pady=2,command=pictoba64)
b2.pack()

# 设置页面按钮b64转.rar(压缩包)
def ba64decode():
    global t
    var = e.get()
    b64decode(var)
#页面布局设置；bg是颜色，width是宽度，height是高度，pady是y轴间距，font字体参数,来控制控件上显示的字体,大小和样式
b3 = tk.Button(window, text='base64转.rar',bg="grey",font=('Arial',12),width=15,height=2,pady=2,command=ba64decode)
b3.pack()

#循环使程序运行后产生图形化页面（如果运行后没出现页面，可以看看加没加这句话）
window.mainloop()
