# import everything from tkinter module
from tkinter import *
import sqlite3
from PIL import Image , ImageTk

root = Tk()
root.title('Space')
root.geometry("1000x500")
root.resizable(False, False)


#push

def push():
	

	#connect
	conn = sqlite3.connect('Login_first_data.db')

	#cursour 
	c = conn.cursor()

	#execute the cursor 
	c.execute ("INSERT INTO addresses VALUES(:User_name , :Password)",
	{
		'User_name' : Username_entry.get(),
		'Password' : Password_entry.get()
	}

	)

	#commit
	conn.commit()
	#close
	conn.close()

	#clear the text box
	Username_entry.delete(0,END)
	Password_entry.delete(0,END)

#fetch
def fetch():
	top = Toplevel()
	def delete():
			conn = sqlite3.connect('Login_first_data.db')
			c= conn.cursor()
			c.execute('DELETE from addresses WHERE oid = ' + Id_number.get())
			
			Id_number.delete(0,END)

				#connec
	
			c.execute('SELECT * , oid from addresses')
			Info_user = c.fetchall()
			print(Info_user)


			record_base = ''
			for record in Info_user:
				record_base +=  str(record[0]) + " " +"\t" + str(record[1]) + " " + "\t" + str(record[2]) + '\n'
			
			
			
			result = Label(top , text= record_base  )
			result.grid(row=3 , column= 1 )
			conn.commit()
			conn.close()


		#connect
	conn = sqlite3.connect('Login_first_data.db')

	#cursour 
	c = conn.cursor()
	c.execute('SELECT * , oid from addresses')
	Info_user = c.fetchall()
	print(Info_user)


	record_base = ''
	for record in Info_user:
		record_base +=  str(record[0]) + " " +"\t" + str(record[1]) + " " + "\t" + str(record[2]) + '\n'
	
	
	
	result = Label(top , text= record_base  )
	result.grid(row=3 , column= 1 )
	
	Label(top,text = 'ID' ).grid(row = 0, column = 0)
	Id_number = Entry(top, width = 10 )
	Id_number.grid(row =0 , column = 1)


	


	Delete_button = Button(top , text = "Delete_acc" ,command= delete )
	Delete_button.grid(row = 0 , column = 2  )

	
	
	#commit
	conn.commit()
	#close
	conn.close()

	
	top.mainloop()


#new_window 
def login_function():
	conn = sqlite3.connect('Login_first_data.db')
	c = conn.cursor()
	c.execute('SELECT * FROM addresses')
	User_Info = c.fetchall()
	conn.commit()
	conn.close()

	for tuple_ in User_Info:
		for name in tuple_:
			if name == Username_entry.get():
				valid_tuple =tuple_
				print(valid_tuple)
				if valid_tuple[1] == Password_entry.get():
					print('Accessed')
					print(valid_tuple)
					my_canvas.destroy()
				else:
					print('Incorrect password')
				
			
def logout_function():
	pass


Login_background = ImageTk.PhotoImage(Image.open( "image/reso.jpg"))

#Creating Canvas to write over the image for root
my_canvas = Canvas(root, width= 1000 , height = 500 , highlightthickness= 0 )
my_canvas.pack(fill='both' , expand= TRUE)
my_canvas.create_image(0,0,image = Login_background , anchor = 'nw' )



#text
my_canvas.create_text(350,120 , text="Username",  font=("Times" , 12), fill= "white" , anchor='nw')
my_canvas.create_text(350,220 , text="Password",  font=("Times" , 12), fill= "white" , anchor='nw')



#label
loginButton =  Button(my_canvas, padx=10, pady= 5 , text="Login" , command = login_function) 
loginButton.place(x= 450,y= 300)

signupButton = Button(my_canvas, text = 'Sign Up? ' , command= push)
signupButton.place(x = 350, y= 300)

temp_show_account= Button(my_canvas, padx=10, pady= 5 , text="i" , command = fetch ) 
temp_show_account.place(x = 0, y= 0)


#Entry
user = StringVar()
Username_entry = Entry(root, textvariable = user , font=("Courier" , 15) , width = 25 ,fg='black', bg =  "#336d92", bd = 0  ,
highlightbackground= "black", highlightthickness=0  )
password = StringVar()
Password_entry = Entry(root,textvariable= password, show = '*' ,font=("Courier" , 15) , width = 25 ,fg='black', bg =  "#336d92", bd = 0  ,
highlightbackground= "black", highlightthickness=0  )



#Window Creation to place the widget on the window and then the window in the canvas
Username_window = my_canvas.create_window(350 , 150 , anchor= 'nw', window= Username_entry ) 
Username_password = my_canvas.create_window(350 , 250 , anchor= 'nw', window= Password_entry ) 


#text

root.mainloop()
