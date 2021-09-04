import tkinter as tki
import tkinter.ttk as ttk
import tkinter.font as font
import logging
import logging.handlers
import subprocess
import sys
import copy


if (__name__ != '__main__'):
    print("pyBrowserSelection is not to be imported")
    print("Exiting...")
    exit(1)


# I would rather not have these hard coded
browser_dict = dict({
    'firefox':
        r'C:\Program Files\Mozilla Firefox\firefox.exe',
    'brave':
        r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe',
    'edge':
        r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
})


lgr = logging.getLogger()
lgr.setLevel(logging.INFO)
# lgr.addHandler(logging.handlers.RotatingFileHandler('log.log'))


argv = copy.copy(sys.argv)
lgr.info(argv)
if len(argv) >= 1:
    argv.pop(0)


tk = tki.Tk()
tk.title('')

# create your frame
style = ttk.Style()
style.theme_use('classic')
style.configure('TFrame', foreground='#888888', background='#101010')
style.configure(
    'C.TButton',
    relief='flat',
    foreground='#888888',
    background='#101010',
)


frame = ttk.Frame(tk)
frame.pack()

my_font = font.Font(size=14)


# wrapper for browser executables
def my_exec():
    try:
        lgr.info('about to execute' + str(lb.get(lb.curselection())))
        popen_arg = [browser_dict[lb.get(lb.curselection())]] + argv
        lgr.info(popen_arg)
        res = subprocess.Popen(
            popen_arg,
            close_fds=True)
        lgr.info(res.args)
    except(tki.TclError):
        lgr.info('tclerror')
    else:
        tk.destroy()
        exit(0)


# create and place listboxes
v = tki.StringVar(value=list(browser_dict.keys()))
lb = tki.Listbox(
    frame,
    listvariable=v,
    selectmode='single',
    font=my_font,
    bg='#101010',
    fg='#888888',
    bd='0',
    highlightcolor='#AA9966',
    relief='flat',
    height=4)
lb.grid(row=0, column=0)


# create and place buttons
button1 = ttk.Button(
    frame,
    text='OK',
    style='C.TButton',
    command=my_exec)
# button1 = tki.Button(
#     frame,
#     text='OK',
#     bg='#101010',
#     fg='#888888',
#     relief='solid',
#     command=my_exec)
button1.grid(row=1, column=0)


# callback for key_press events
def key_pressed(event):
    if event.keysym == 'Down' or event.keysym == 'j':
        if len(lb.curselection()) == 0:
            lb.selection_set(0)
        else:
            oldindex = lb.curselection()[0]
            lb.selection_clear(oldindex)
            lb.selection_set(oldindex + 1)

    elif event.keysym == 'Up' or event.keysym == 'k':
        if len(lb.curselection()) == 0:
            lb.selection_set(lb.size() - 1)
        else:
            oldindex = lb.curselection()[0]
            lb.selection_clear(oldindex)
            lb.selection_set(oldindex - 1)

    elif event.keysym == 'Return':
        my_exec()

    elif event.keysym == 'Escape':
        tk.destroy()

    else:
        return


# assign key press callback
tk.bind("<Key>", key_pressed)


# main loop
tk.mainloop()
