import tkinter.messagebox
import tkinter as tk
from registerPage import register_window
from modePage import Ui_ModeWindow

def UI_window():
    global window
    global username
    global username_input
    global password
    global password_input
    #Window Settings
    window = tk.Tk()
    window.title("Pacemaker User Interface")
    window.geometry('400x400')

    #Background Settings
    background = tk.Canvas(window, width = 400, height = 400, bg = 'white')
    image_file = tk.PhotoImage(file = 'heart.gif')
    background.create_image(200,45,anchor='n',image = image_file)
    background.pack(side='top')
    tk.Label(window, text="Welcome",bg='white',font=("Times New Roman",20)).place(x=140,y=180)

    # User Name & Password Settings
    tk.Label(window, text="User Name :", bg='white', font=("Times New Roman", 15)).place(x=40, y=240)
    tk.Label(window, text="Password :", bg='white', font=("Times New Roman", 15)).place(x=40, y=280)
    button_login = tk.Button(window, text="Log In", command=user_login,width = 13).place(x=80,y=330)
    button_signup = tk.Button(window, text="Sign up",command=register_window, width = 13).place(x=220,y=330)

    username = tk.StringVar()
    username_input = tk.Entry(window, textvariable = username, font=("Times New Roman", 15), show=None)
    username_input.place(x=165, y=240)
    password = tk.StringVar()
    password_input = tk.Entry(window, textvariable = password, font=("Times New Roman", 15), show="*")
    password_input.place(x=165,y=280)

    window.mainloop()

    
def user_login():
    global u_name

    checkflag=0
    u_name = username_input.get()
    u_pswd = password_input.get()
    try:
	    file2 = open('userdata.txt','r')
	    readcont2 = file2.readlines()
	    file2.close()
	    rowc2=[]
	    list_name=[]
	    list_pswd=[]
	    for x in readcont2:
	        rowc2.append(x.split(','))
	    while['\n'] in rowc2:
	        rowc2.remove(['\n'])
	    for y in rowc2:
	        list_name.append(y[0])
	    for z in rowc2:
	        list_pswd.append(z[1])

	    for a in list_name:
	        if (u_name=='') or (u_pswd==''):
	            tkinter.messagebox.showerror('Error','User name/password cannot be blank')
	            checkflag=1
	            break
	        elif u_name==a:
	            if list_pswd[list_name.index(u_name)] == u_pswd:
	                checkflag=1
	                window.destroy()
	                Ui_ModeWindow()
	                break
	            else:
	                tkinter.messagebox.showerror('Error','Invalid Username/Password')
	                checkflag=1
	                break
	    if checkflag==0:       
	        tkinter.messagebox.showerror('Error','Invalid Username/Password')
    except:
	    tkinter.messagebox.showerror('Error', 'Pleas Sign up first')

UI_window()


    

