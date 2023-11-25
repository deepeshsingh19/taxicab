from pprint import pprint 
import requests
from settings import sid, key, token
def connect_customer_to_agent(sid, key, token, agent_no, customer_no, callerid,timelimit=None, timeout=None, calltype='trans'):
    return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Calls/connect.jso n'.format(sid=sid),
                         auth=(key, token), data= {'From': agent_no, 'To': customer_no, 'CallerId': callerid, 'TimeLimit': timelimit, 'TimeOut': timeout, 'CallType': calltype
})
import os
from tkinter import * 
from tkinter import ttk 
window=Tk()
canvas=Canvas() 
canvas.pack(fill=X,side='top')
photo=PhotoImage(file='C:\\Users\\deepesh\Desktop\\cs\\—Pngtree—net taxi orange ad_958441.png')

canvas.create_image(100,100,image=photo)
import mysql.connector as mc 
demo=mc.connect(user='root',host='localhost',password='1234') 
cur=demo.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS PROJECT') 
cur.execute('USE PROJECT')
cur.execute('CREATE TABLE IF NOT EXISTS DRIVER(NAME VARCHAR(20),PHONE_NO BIGINT ,CAR_MODEL VARCHAR(15),CAR_TYPE VARCHAR(10),EXPERIENCE CHAR(5)) ')
cur.execute("INSERT INTO DRIVER VALUES('Chandra Prakash',8521216472,'INDICA GO','MINI','****')")
cur.execute("INSERT INTO DRIVER VALUES('Ashutosh',8521216472,'SWIFT','MICRO','***')") 
cur.execute("INSERT INTO DRIVER VALUES('Deepesh',8521216472,'SWIFT DESIRE','SEDAN','****')")
cur.execute("INSERT INTO DRIVER VALUES('Utkarsh',8521216472,'BMW 320D','LUX','*****')")
cur.execute("INSERT INTO DRIVER VALUES('Arbaz',8521216472,'INNOVA','SUV','****')")
demo.commit()
#creating a title
window.title('PROJECT')
label1=Label(canvas,text='WELCOME TO A-C-D CABS',font=('TIMES NEW ROMAN',40),fg='orange',bg='black')
label1.pack(pady=50,side='top')
#to open new windows when clicked the button
#book window 
def book_win():
    global txt,txt1,dis,combo,bookwin,l,combo1 
    bookwin = Toplevel(window)
 
    
    display = Label(bookwin,text='PICKUP LOCATION',fg='orange') 
    display.grid(column=0,row=0)
    txt=Entry(bookwin,width=20)
    txt.grid(column=1,row=0)
    display = Label(bookwin,text='DROP LOCATION',fg='orange') 
    display.grid(column=0,row=1) 
    txt1=Entry(bookwin,width=20)
    txt1.grid(column=1,row=1)
    a='''TYPE OF CAR (NOTE:-
        MINI : Rs.8/km
        MICRO : Rs.12/km SEDAN : Rs.16/km LUX :Rs.24/km SUV :Rs.20/km)'''
    display = Label(bookwin,text=a,fg='orange') 
    display.grid(column=0,row=2)
    combo=ttk.Combobox(bookwin,values=['MINI','MICRO','SEDAN','LUX','SUV '])
    combo.grid(column=1,row=2) 
    combo.current()
    display = Label(bookwin,text='PAYMENT METHOD',fg='orange') 
    display.grid(column=0,row=3) 
    combo1=ttk.Combobox(bookwin,values=['CASH','CARD','PHONEPAYMENT']) 
    combo1.grid(column=1,row=3) 
    combo1.current()
    display = Label(bookwin,text=' APPROX. DISTANCE',fg='orange') 
    display.grid(column=0,row=4)
    dis=Entry(bookwin,width=20)
    dis.grid(column=1,row=4)
    okbutton=Button(bookwin,text='CONFIRM BOOKING',command=cal,) 
    okbutton.grid(column=2,row=5)
 
    
    r = connect_customer_to_agent( 'acd5d1','cfc67913894c895126285dc831647824141b36189a09967f',
                                  'c38a28eed811931da1e09eeed2ccb2c5b1d909e7e8d18c47', 
                                  agent_no="8521216472",
                                  customer_no="8521216472",
                                  callerid="08047108609",
                                  timelimit="<time-in-seconds>", # This is optional 
                                  timeout="<time-in-seconds>", # This is also optional 
                                  calltype="trans" # Can be "trans" for transactional and "promo" for promotional content 
        )
    print (r.status_code) 
    pprint(r.json())
    
l=[]
#under booking a cab window 
#details and bill
############################GAME############################ 
def game():
    # defining Tk from Tkinter
    root = Tk()
    root.title("Catch the ball Game") 
    root.resizable(False,False)
    # for defining the canvas
    canvas = Canvas(root, width=600, height=600) 
    canvas.pack()
    # variable for the vertical distance 
    # travelled by ball
    limit = 0
    # variable for horizontal distance 
    # of bar from x-axis
    
    dist=5
    # variable for score 
    score = 0
    # Class for the Creating and moving ball 
    class Ball:
        # for creation of ball on the canvas
        def __init__(self, canvas, x1, y1, x2, y2):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2 
            self.canvas = canvas
            # for creation of ball object
            self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2,fill = "red",tags = 'dot1')
        # for moving the ball 
        def move_ball(self):
            # defining offset 
            offset = 10 
            global limit
            # checking if ball lands ground or bar 
            if limit >= 510:
                global dist,score,next
                # checking that ball falls on the bar 
                if(dist - offset <= self.x1 and dist + 40 + offset >= self.x2):
                    # incrementing the score 
                    score+= 10
                    # dissappear the ball 
                    canvas.delete('dot1')
                    # calling the function for again 
                    # creation of ball object 
                    ball_set()
                else:
                    # dissappear the ball 
                    canvas.delete('dot1') 
                    bar.delete_bar(self)
                    # display the score
                    score_board() 
                return
            # incrementing the vertical distance 
            # travelled by ball by deltay
            limit += 1
            # moving the ball in vertical direction 
            # by taking x=0 and y=deltay 
            self.canvas.move(self.ball,0,1)
            # for continuous moving of ball again call move_ball 
            self.canvas.after(10,self.move_ball)
    # class for creating and moving bar 
    class bar:
        # method for creating bar
        def __init__(self,canvas,x1,y1,x2,y2):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2 
            self.canvas = canvas

            # for creating bar using create_rectangle 
            self.rod=canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,fill="yellow",tags='dot2')
        # method for moving the bar 
        def move_bar(self,num):
            global dist
            # checking the forward or backward button 
            if(num == 1):
                # moving the bar in forward direction by 
                # taking x-axis positive distance and
                # taking vertical distance y=0 
                self.canvas.move(self.rod,20,0)
                # incrementing the distance of bar from x-axis
                dist += 20 
            else:
                # moving the bar in backward direction by taking x-axis 
                # negative distance and taking vertical distance y=0 
                self.canvas.move(self.rod,-20,0)
                # decrementing the distance of bar from x-axis 
                dist-=20
        def delete_bar(self): 
            canvas.delete('dot2')
    # Function to define the dimensions of the ball 
    def ball_set():
        global limit 
        limit=0
        # for random x-axis distance from 
        # where the ball starts to fall
        value = randint(0,570)
        # define the dimensions of the ball
        ball1 = Ball(canvas,value,20,value+30,50)
        # call function for moving of the ball 
        ball1.move_ball()
    # Function for displaying the score 
    # after getting over of the game 
    def score_board():
        root2 = Tk()
        root2.title("Catch the ball Game") 
        root2.resizable(False,False)
        canvas2 = Canvas(root2,width=300,height=300) 
        canvas2.pack()
#       w = Label(canvas2,text="\nOOPS...GAME IS OVER\n\nYOUR SCORE =" + str(score) + "\n\n")
#       w.pack()
        button3 = Button(canvas2, text="PLAY AGAIN", bg="green", command=lambda:play_again(root2))
        button3.pack()
        button4 = Button(canvas2,text="EXIT",bg="green", command=lambda:exit_handler(root2))
        button4.pack()
    # Function for handling the play again request 
    def play_again(root2):
        root2.destroy() 
        main()
    # Function for handling exit request 
    def exit_handler(root2):
        value = randint(0,570)
        root2.destroy()
        root.destroy()
    # Main function 
    def main():
        global score,dist 
        score = 0 
        dist=0
        # defining the dimensions of bar 
        bar1=bar(canvas,5,560,45,575)
        # defining the text,colour of buttons and
        # also define the action after click on
        # the button by calling suitable methods
        button = Button(canvas,text="==>", bg="green",
                        command=lambda:bar1.move_bar(1))
        # placing the buttons at suitable location on the canvas 
        button.place(x=300,y=580)
        button2 = Button(canvas,text="<==",bg="green", command=lambda:bar1.move_bar(0))
        button2.place(x=260,y=580)
        # calling the function for defining 
        # the dimensions of ball 
        ball_set()
        root.mainloop()
    # Driver code 
    if(__name__=="__main__"):
        main()
def cal():
    if ((txt.get()).isalpha() and (txt1.get()).isalpha() and (dis.get()).isdigit() ):
        if(combo.get()=='' or combo1.get()==''):
            print('PLZ SELECT THE TYPE OF CAR OR METHOD OF PAYMENT CORRECTLY') 
        else:
            l.append((txt.get(),txt1.get()))
            print('YOUR PICKUP POINT IS : ',txt.get())
            print('YOUR DROP POINT IS : ',txt1.get())
            cur.execute("SELECT * FROM DRIVER WHERE CAR_TYPE = '%s'"%(combo.get())) 
            a=cur.fetchone()
            print('YOUR DRIVER DETAILS IS',a) 
            print('----------x----------x----------')
    else:
        print('PLZ ENTER CORRECT VALUES')
        okbutton=Button(bookwin,text='GENERATE BILL',command=gb) 
        okbutton.grid(column=2,row=6)
def exittop(): 
    thanks.quit() 
    thanks.destroy() 
    bookwin.quit() 
    bookwin.destroy()
def gb():
    global thanks 
    if(combo.get()=='MINI'):
        print('THE TOTAl FARE OF YOUR RIDE IS : Rs.',int(dis.get())*8) 
    elif(combo.get()=='MICRO'):
        print('THE TOTAl FARE OF YOUR RIDE IS : Rs.',int(dis.get())*12) 
    elif(combo.get()=='SEDAN'):
        print('THE TOTAl FARE OF YOUR RIDE IS : Rs.',int(dis.get())*16) 
    elif(combo.get()=='LUX'):
        print('THE TOTAl FARE OF YOUR RIDE IS : Rs.',int(dis.get())*24)
    elif(combo.get()=='MICRO'):
        print('THE TOTAl FARE OF YOUR RIDE IS : Rs.',int(dis.get())*20) 
    print('----------x----------x----------')
    
    thanks=Toplevel(window) 
    display=Label(thanks,text='THANKS FOR RIDING WITH A-C-D') 
    display.grid(column=5,row=1)
    display=Label(thanks,text='PLZ RATE YOUR RIDE ') 
    display.grid(column=5,row=2) 
    diplay=Radiobutton(thanks,text='') 
    diplay.grid(column=3,row=4) 
    diplay=Radiobutton(thanks,text='',value=2) 
    diplay.grid(column=4,row=4) 
    diplay=Radiobutton(thanks,text='',value=3) 
    diplay.grid(column=5,row=4) 
    diplay=Radiobutton(thanks,text='',value=4) 
    diplay.grid(column=6,row=4) 
    diplay=Radiobutton(thanks,text='',value=5) 
    diplay.grid(column=7,row=4)
okbutton=Button(thanks,text='SUBMIT',command=exittop).grid(column=5, row=6)
"""
a='''
##
NAME : Chandra Prakash PHONE_NUMBER : 8521216472 CAR_MODEL : INDICA GO CAR_TYPE : MINI
EXPERIENCE : **** ##'''
b='''
##
NAME : Ashutosh PHONE_NUMBER : 8521216472 CAR_MODEL : SWIFT
CAR_TYPE : MICRO
EXPERIENCE : ***
##'''
    
c='''
##
NAME : Deepesh PHONE_NUMBER : 8521216472 CAR_MODEL : SWIFT DESIRE CAR_TYPE : SEDAN
EXPERIENCE : ****
##'''
d='''##
NAME : Utkarsh PHONE_NUMBER : 8521216472 CAR_MODEL : VERNA CAR_TYPE : LUX
EXPERIENCE : *****
##'''
e='''
##
NAME : Arbaz PHONE_NUMBER : 8521216472 CAR_MODEL : INNOVA CAR_TYPE : SUV
EXPERIENCE : ****
##'''
"""
#ride history window
def ride_win():
    global l
    ridewin = Toplevel(window)
    display = Label(ridewin, text="YOUR RIDE HISTORY IS SHOWN AS BELOW",fg='orange') 
    display.grid(column=0,row=0)
    ## l.append((txt.get(),txt1.get())) 
    display = Label(ridewin, text=l) 
    display.grid(column=0,row=1) 
    print('HISTORY OF YOUR RIDES IS ',l)
    
    print('----------x----------x----------')
#settings window 
def setting_win():
    settingwin = Toplevel(window)
    display = Button(settingwin,text='HELP',font=('TIMES NEW ROMAN',15),fg='white',bg='black',command=help_win)
    display.grid(column=0,row=1)
    display = Button(settingwin,text='CONTACT US',font=('TIMES NEW ROMAN',15),fg='white',bg='black',command=contact_win)
    display.grid(column=0,row=2)
#under settings window 
#help window
def help_win():
    global label1
    helpwin=Toplevel(window)
    label=Label(helpwin,text="WHAT'S THE PORBLEM!",font=('TIMES NEW ROMAN',10),fg='orange')
    label.grid(column=0,row=0) 
    label1=Entry(helpwin,width=10) 
    label1.grid(column=5,row=0)
    display = Button(helpwin,text='SUBMIT',font=('TIMES NEW ROMAN',10),command=prihelp) 
    display.grid(column=0,row=2)
#to print help 
def prihelp():
    print('~SOS~ =>',label1.get(),'<= ~SOS~') 
#contact window
def contact_win():
    contactwin=Toplevel(window)
    label=Label(contactwin,text="CONTACT EMAIL ADDRESS : chandraprakashgarg0205@gmail.com",font=('TIMES NEW ROMAN',15),fg='orange')
    label.grid(column=0,row=0)

#about window 
def about_win():
    aboutwin = Toplevel(window)
    display = Label(aboutwin, text="-OUR MISSION-",font=('TIMES NEW ROMAN',30),fg='purple')
    display.pack()
    display = Label(aboutwin, text="To provide the most actionable booking app.",font=('TIMES NEW ROMAN',15))
    display.pack()
    display = Label(aboutwin, text="-OUR PROMISE-",font=('TIMES NEW ROMAN',30),fg='purple')
    display.pack()
    display = Label(aboutwin, text="We deliver safe,optimistic and diverse storytelling,experience through our booking application.",font=('TIMES NEW ROMAN',15))
    display.pack()
    display = Label(aboutwin, text="-OUR VIBE-",font=('TIMES NEW ROMAN',30),fg='purple')
    display.pack()
    display = Label(aboutwin, text="At , We make magic. We dream it, and then do it-together-every day reinventing what's possible. ",font=('TIMES NEW ROMAN',15))
    display.pack()
#close window 
def close_win():
    closewin=Toplevel(window)
    d=Label(closewin,text='THANK YOU FOR CHOOSING A-C- D',fg='black',bg='white').pack()
#creating buttons on the home page
label=Button(canvas,text='BOOK YOUR RIDE',font=('TIMES NEW ROMAN',20),fg='black',bg='orange',command=book_win) 
label.pack()
    
label=Button(canvas,text=' RIDE HISTORY',font=('TIMES NEW ROMAN',20),fg='black',bg='orange',command=ride_win) 
label.pack()
label=Button(canvas,text='PLAY GAME',font=('TIMES NEW ROMAN',20),fg='black',bg='orange',command=game) 
label.pack()
label=Button(canvas,text='SETTINGS',font=('TIMES NEW ROMAN',20),fg='black',bg='orange',command=setting_win) 
label.pack()
label=Button(canvas,text='ABOUT',font=('TIMES NEW ROMAN',20),fg='black',bg='orange',command=about_win) 
label.pack()
label=Button(canvas, text="QUIT", command=window.destroy,font=('TIMES NEW ROMAN',20),fg='black',bg='orange') 
label.pack()
label=Label(canvas,text='~THANK YOU FOR USING A-C-D ~' ,font=('TIMES NEW ROMAN',10),fg='orange',bg='black')
label.pack(pady=100)
window.mainloop()
##############################calling API######################
# Get your SID and token from https://my.exotel.com/apisettings/site#api- credentials
sid = 'xxxx' # <account sid>
key = 'xxxx' # <api key>
token = 'xxxx' # <api token>







