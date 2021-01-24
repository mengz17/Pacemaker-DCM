import tkinter.messagebox
import tkinter as tk

def register_window():

    #Detect File
    try:
        with open('userdata.txt', 'r') as user_file:
            pass

    #If no file detected, create one
    except FileNotFoundError:
        user_file = open("userdata.txt", 'w')
    
    user_file.close()


    def user_signup():
        checkflag=1
        counter=0

        #Get name, password and confirmation from user
        newPswd = pswd_input.get()
        newPswdConfirm = confirm_input.get()
        newName = name_input.get()

        #Read File
        u_file = open('userdata.txt','r')
        readcont=u_file.readlines()
        u_file.close()
        rowc = []
        colc = []
        for x in readcont:
            rowc.append(x.split(','))
        while['\n'] in rowc:
            #counter=counter+1;
            rowc.remove(['\n'])
        for y in rowc:
            colc.append(y[0])
        for z in colc:
            counter=counter+1
            if z == newName:
                checkflag=0
                tkinter.messagebox.showerror('Error','Username is not permitted')

        if counter==10:
            checkflag=0
            tkinter.messagebox.showerror('Error','Sorry,the user list is full(maxium 10 users)')
            r_window.destroy()
        
        else:
            if (newName=='') or (newPswd==''):
                checkflag=0
                tkinter.messagebox.showerror('Error','User name/password cannot be blank')
                
            if newPswd!=newPswdConfirm:
                checkflag=0
                tkinter.messagebox.showerror('Error','Please check that you typed the same password twice')

            if checkflag==1:        
                file1 = open('userdata.txt','a')
                file1.write(newName)
                file1.write(',')
                file1.write(newPswd)
                file1.write(',')
                file1.write(newPswdConfirm)
                file1.write(',\n')
                file1.close()
                tkinter.messagebox.showinfo('Great','You have successfully registered')
                r_window.destroy()
                #print(counter)


    #User Name & Password Settings
    r_window = tk.Tk()
    r_window.geometry('400x250')
    r_window.title('New User Register')

    new_username = tk.StringVar()
    tk.Label(r_window, text='User name: ', font=("Times New Roman", 15)).place(x=17, y=30)
    name_input = tk.Entry(r_window, textvariable=new_username, font=("Times New Roman", 15))
    name_input.place(x=180, y=30)


    new_pswd = tk.StringVar()
    tk.Label(r_window, text='Password: ', font=("Times New Roman", 15)).place(x=17, y=70)
    pswd_input = tk.Entry(r_window, textvariable=new_pswd, font=("Times New Roman", 15), show='*')
    pswd_input.place(x=180, y=70)

    
    pswd_confirm = tk.StringVar()
    tk.Label(r_window, text='Confirm Password: ', font=("Times New Roman", 15)).place(x=17, y=110)
    confirm_input = tk.Entry(r_window, textvariable=pswd_confirm, font=("Times New Roman", 15), show='*')
    confirm_input.place(x=180, y=110)


    button_cancel = tk.Button(r_window,text="Cancel",command=lambda:[r_window.destroy()], width = 13)
    button_cancel.place(x=220, y=170)
    button_register = tk.Button(r_window,text="Sign Up",command=user_signup, width = 13)
    button_register.place(x=50, y=170)
