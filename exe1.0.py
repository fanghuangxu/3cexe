import tkinter as tk
main_window = tk.Tk()
main_window.geometry('{}x{}+{}+{}'.format(800, 600, 100, 100))
global text_index
text_index = tk.Text(main_window,height=1,width=10)
text_index.pack()
def cint():
    cint_window = tk.Tk()
    cint_window.geometry('{}x{}+{}+{}'.format(400, 300, 100, 100))
    
def cput():
    cput_window = tk.Tk()
    cput_window.geometry('{}x{}+{}+{}'.format(400, 300, 100, 100))
def index():
    global text_index
    text = str(text_index.get(1.0,'1.end'))
    if text != None:
        try:
            exec(text+'()')
        except Exception:
            from tkinter import messagebox as mbox
            mbox.showerror('3Cexe文档error','没有这个代码')
    else:
        mbox.showerror('3Cexe文档error','不能为空')
button_index = tk.Button(main_window,text='搜索',command=index)
button_index.pack()
main_window.mainloop()
