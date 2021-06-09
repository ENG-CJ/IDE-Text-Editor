
#  Import
from tkinter import *
from tkinter import messagebox, Menu
import webbrowser as web
from PIL import Image,ImageTk
import time
from  tkinter import  ttk
from tkinter import filedialog
import subprocess
# import pyttsx3
file_Path=''
# functions
def java():
    messagebox.askokcancel('JAVA','This is not currently Working')
def cplus():
    messagebox.askokcancel('C++', 'This is not currently Working')
def fblog():
    web.open('https://www.facebook.com/abdulrahman.haaji.1')
def gitlog():
    web.open('https://github.com/ENG-CJ')
def twit():
    messagebox.showerror('ENG-CJ|403','Not found This URL')
def EXIT():
    ans=messagebox.askyesno('Confirm','Are You Sure To EXIT\U0001F643?')
    if (ans)==1:
        root.destroy()
# Second Window
def pyscript():
   root.destroy()

def main_window():
    global root
    #  Main Window ---
    root=Tk()
    root.state('zoomed')
    root.title('IDE TEXT EDITOR APP | Developed By ENG-CJ')
    root.resizable(0,0)
    root.iconbitmap('icon.ico')
    root.config(bg='#34495E')
    #________________________________________________________________________
    # Frame
    frame=Frame(root,width=1200,height=900,bd=20,relief='ridge',bg='#2d3436')
    frame.pack(pady=150)

    # Vector Icon
    vector=Image.open('vector.png')
    vec_resize=vector.resize((450,450),Image.ANTIALIAS)
    vec_new=ImageTk.PhotoImage(vec_resize)
    vec_label=Label(frame,image=vec_new,bg='#2d3436')
    vec_label.place(x=700,y=20)

    # Text Labels
    #_______________________________________________________________________
    Label(frame,text='HI! USER\U0001F600',bg='#2d3436',fg='white',
          font=('Verdana',8,'bold')).place(x=810,y=390)

    Label(frame,text='This is text editor (IDE) That Allows You',bg='#2d3436',fg='white',
          font=('Verdana',8,'bold')).place(x=810,y=410)

    Label(frame,text='To Write Code [Python,Java,C++]',bg='#2d3436',fg='white',
          font=('Verdana',8,'bold')).place(x=810,y=430)

    Label(frame,text='Now It Only Works For Python \U0001F644',bg='#2d3436',fg='white',
          font=('Verdana',8,'bold')).place(x=810,y=450)

    Label(frame,text='DEVELOPER: ENG-CJ',bg='#2d3436',fg='yellow',
          font=('Verdana',8,)).place(x=840,y=470)
    #______________________________________________________________________________

    Label(frame,text='IDE TEXT EDITOR SOFTWARE',bg='#2d3436',fg='white',
          font=('Verdana',36,"bold",'underline')).place(x=140,y=25)
    image=Image.open('Images/bulb.png')
    resize=image.resize((100,100),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(resize)
    Label(frame,image=new,bg='#2d3436',bd=2).place(x=1,y=1)

    # Images
    #______________________________________________________________________________________
    # Java Image And Label
    Java=Image.open('java.png')
    resize1=Java.resize((250,250),Image.ANTIALIAS)
    new2=ImageTk.PhotoImage(resize1)
    jav_btn=Button(frame,image=new2,bg='#2d3436',bd=0,activebackground='#2d3436',command=java)
    jav_btn.place(x=320,y=100)

    Jav_Label=Label(frame,text='JAVA',bg='blue',fg='white',font=('Verdana',15,'bold'),
                    bd=3,relief='ridge',width=5)
    Jav_Label.place(x=400,y=310)

    # Python Images And Label

    python=Image.open('python.png')
    resize=python.resize((200,200),Image.ANTIALIAS)
    new1=ImageTk.PhotoImage(resize)
    Py_btn=Button(frame,image=new1,bg='#2d3436',bd=0,command=pyscript,activebackground='#2d3436')
    Py_btn.place(x=170,y=130)

    Python_Label=Label(frame,text='Python',bg='red',fg='white',font=('Verdana',15,'bold'),
                    bd=3,relief='ridge',width=5)
    Python_Label.place(x=230,y=310)

    # C++ Image And Label
    Cplus=Image.open('unnamed (1).png')
    resize2=Cplus.resize((140,140),Image.ANTIALIAS)
    new3=ImageTk.PhotoImage(resize2)
    c_btn=Button(frame,image=new3,bg='#2d3436',bd=0,activebackground='#2d3436',command=cplus)
    c_btn.place(x=570,y=170)

    Cplus_lable=Label(frame,text='C++',bg='#003E53',fg='white',font=('Verdana',15,'bold'),
                    bd=3,relief='ridge',width=5)
    Cplus_lable.place(x=600,y=320)
    Label(frame,text='You Can Use For Free',bg='#2d3436',fg='yellow',
          font=('Verdana',18)).place(x=400,y=90)
    #___________________________________________________________________________
    # Info Label
    Note=Label(frame,text='NOTE',bg='#2d3436',fg='yellow',font=('Verdana',15,'bold','underline'),).place(x=6,y=400)

    Label(frame,text='This is free software '
                          'you can use it to write code to'
                          'run those languages',bg='#2d3436',fg='red',font=('Verdana',12),).place(x=6,y=425)

    Label(frame,text='DEVELOPED BY: Abdulrahman Haaji | ENG-CJ |',bg='#2d3436',fg='white',font=('Verdana',12),).place(x=6,y=445)
    #____________________________________
    # Buttons

    help=Button(root,text='HELP',bg='black',fg='white',
                font=('Verdana',16,'bold'),bd=5,relief='ridge',activebackground='yellow',
                activeforeground='black')
    help.place(x=476,y=710)

    About=Button(root,text='DEV',bg='#0000a0',fg='white',
                font=('Verdana',16,'bold'),bd=5,relief='ridge',activebackground='red',
                activeforeground='white')
    About.place(x=600,y=710)

    Exit=Button(root,text='EXIT',bg='red',fg='white',
                font=('Verdana',16,'bold'),bd=5,relief='ridge',activebackground='white',
                activeforeground='red',command=EXIT)
    Exit.place(x=710,y=710)

    Label(root,text='POWERED BY: ENG-CJ',bg='#34495E',fg='white',
                font=('Verdana',10)).place(x=620,y=820)
    #__________________________________________________________________________________

    # Links

    Link_Label=Label(root,text='Links',bg='#34495E',fg='white',font=('Courier',15,'bold'))
    Link_Label.place(x=1390,y=155)

    # facebook Image
    facebook=Image.open('facebook.png')
    fb_resize=facebook.resize((40,40),Image.ANTIALIAS)
    new_fb=ImageTk.PhotoImage(fb_resize)
    Button(root,image=new_fb,bg='#34495E',bd=0,activebackground='blue',activeforeground='white',
           command=fblog).place(x=1387,y=180)

    github=Image.open('GitHub-Mark-removebg-preview.png')
    github_resize=github.resize((40,40),Image.ANTIALIAS)
    new_git=ImageTk.PhotoImage(github_resize)
    Button(root,image=new_git,bg='#34495E',bd=0,activebackground='white',activeforeground='white',
           command=gitlog).place(x=1387,y=220)

    twitter=Image.open('twitter.png')
    twitter_resize=twitter.resize((40,40),Image.ANTIALIAS)
    new_twit=ImageTk.PhotoImage(twitter_resize)
    Button(root,image=new_twit,bg='#34495E',bd=0,activebackground='white',activeforeground='white',
           command=twit).place(x=1387,y=270)

    mainloop()

main_window()
# Second Window downloading
def download():
    # Progress Value
    s = ttk.Style()
    s.configure("TProgressbar", foreground="red", background="red", thickness=20)
    progr = ttk.Progressbar(window, style="TProgressbar", length=400, mode="determinate")
    progr.place(x=530, y=560)
    for i in range(1, 102, 1):
        progr['value'] = i
        window.update_idletasks()
        l1.config(text=str(i) + '%')
        time.sleep(0.05)
    progr['value'] = 100
    l1.config(text='Downloaded')
    window.after(2000)
    window.destroy()
# Third Window
def second_window():
    global window,download,l1,btn
    window=Tk()
    window.state('zoomed')
    window.title('Download%Missing Files % Virtual Downloading')
    window.iconbitmap('icon.ico')
    window.resizable(0,0)
    window.config(bg='white')
    # Download Button
    download_btn = Image.open('down_icon.png')
    reszie_download = download_btn.resize((200, 200))
    new_down = ImageTk.PhotoImage(reszie_download)
    btn=Button(window, image=new_down, bg='white',activebackground='white', bd=0,
           command=download)
    btn.place(x=590, y=430)
    l1 = Label(window, text='', bg='white',fg='black',font=('Verdana',14,'bold'))
    l1.place(x=640, y=590)
    # Info label
    Label(window, text='Download All Missing %Files --> 202MB',fg='red').place(x=590, y=420)
    Label(window, text='Install And Download From My %Packages').place(x=590, y=450)
    Label(window, text='This Is Open Source Text Editor').place(x=590, y=480)

    Label(window, text='POWERED BY: ENG-CJ',bg='white',fg='blue',
          font=('Verdana',15,'bold')).place(x=580, y=750)

    # Downloading -btn- section
    download=Image.open('down-arrow.png')
    resize_arr=download.resize((300,300),Image.ANTIALIAS)
    new_arr=ImageTk.PhotoImage(resize_arr)
    Label(window,image=new_arr,bg='white').place(x=540,y=100)
    mainloop()

second_window()
# Function --> IDE Editor ()
def run():
    command=f'python {file_Path}'
    process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output,err=process.communicate()
    code_output.insert('1.0',output)

def set_file_path(path):
    global file_Path
    file_Path=path

def open_file():
   path=filedialog.askopenfilename(filetypes=[('Python Files','*.py')])
   with open(path,'r') as file:
       code=file.read()
       editor.delete('1.0',END)
       editor.insert('1.0',code)
       set_file_path(path)

def save_as():
    if file_Path=='':
        path=filedialog.asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path=file_Path
    with open(path,'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_file_path(path)





def terminate():
    message=messagebox.askyesno('Confirm','Are You Sure To Exit?')
    if (message)==1:
        IDE.destroy()
    else:
        pass

#  Third Window
def IDE_EDITOR():
    global editor,IDE,code_output
    IDE=Tk()
    # IDE.config(bg='white')
    # IDE.resizable(0,0)
    IDE.iconbitmap('icon.ico')

    IDE.title('Hack-thon Text Editor')
    # IDE.state('zoomed')
    # Menus
    menu_bar: Menu=Menu(IDE)

    # File Menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Open',command=open_file)
    file_menu.add_command(label='Save',command=save_as)
    file_menu.add_command(label='Save As',command=save_as)
    file_menu.add_separator()
    file_menu.add_command(label='Exit',command=terminate)
    menu_bar.add_cascade(label='File', menu=file_menu)
    IDE.config(menu=menu_bar)

    # Run Menu
    run_bar=Menu(menu_bar,tearoff=0)
    run_bar.add_command(label='Run',command=run)
    menu_bar.add_cascade(label='Run',menu=run_bar)
    IDE.config(menu=menu_bar)

    # Help Menu
    Help_menu = Menu(menu_bar, tearoff=0)
    Help_menu.add_command(label='About')
    Help_menu.add_command(label='Dev')
    menu_bar.add_cascade(label='Help', menu=Help_menu)
    IDE.config(menu=menu_bar)

    editor=Text(font=('Verdana',16))
    editor.pack()

    # output
    code_output=Text(height=5,font=('Verdana',16))
    code_output.pack()



    mainloop()
IDE_EDITOR()
