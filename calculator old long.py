from tkinter import *
x=Tk()
y=Entry(x,border=6)
y.grid(row=0,columnspan=3,ipadx=120,ipady=12,sticky='w')

#To add all the writen numbers into one string
def z(x):
    h=y.get()
    h+=x
    y.delete(0,END)
    y.insert(0,h)

#to delete one character from end

def de():
    ro=y.get()
    ro=ro[0:len(ro)-1]
    y.delete(0,END)
    y.insert(0,ro)
    
#to clear the screen
def cl():
    y.delete(0,END)

#to equate
def tot(su):
    su=y.get()
    y.delete(0,END)
    x=round(eval(su),5)
    y.insert(0,str(x))

#all buttons

a1=Button(x,text='1',command=lambda:z('1'),border=4)
a1.grid(row=1,column=0,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

	
a2=Button(x,text='2',command=lambda:z('2'),border=5)
a2.grid(row=1,column=1,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

	
a3=Button(x,text='3',command=lambda:z('3'),border=5)
a3.grid(row=1,column=2,ipadx=40,ipady=25,columnspan=1,sticky='nsew')


	
a4=Button(x,text='4',command=lambda:z('4'),border=5)
a4.grid(row=2,column=0,ipadx=40,ipady=25,columnspan=1,sticky='nsew')


	
a5=Button(x,text='5',command=lambda:z('5'),border=5)
a5.grid(row=2,column=1,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

	
a6=Button(x,text='6',command=lambda:z('6'),border=5)
a6.grid(row=2,column=2,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

	
a7=Button(x,text='7',command=lambda:z('7'),border=5)
a7.grid(row=3,column=0,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

	
a8=Button(x,text='8',command=lambda:z('8'),border=5)
a8.grid(row=3,column=1,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

	
a9=Button(x,text='9',command=lambda:z('9'),border=5)
a9.grid(row=3,column=2,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

	
a0=Button(x,text='0',command=lambda:z('0'),border=5)
a0.grid(row=4,column=0,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

# . button
det=Button(x,text='.',command=lambda:z('.'),border=5)
det.grid(row=4,column=1,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

# + button	
ad=Button(x,text='+',command=lambda:z('+'),border=5)
ad.grid(row=4,column=2,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

# = button	
eq=Button(x,text='=',fg='blue',command=lambda:tot(y.get()),border=6)
eq.grid(row=5,column=2,ipadx=40,ipady=25,columnspan=1,rowspan=1,sticky='nsew')


# - button	
su=Button(x,text='-',command=lambda:z('-'),border=5)
su.grid(row=5,column=0,ipadx=40,ipady=25,columnspan=1,sticky='nsew')


# × button	
mu=Button(x,text='×',command=lambda:z('*'),border=5)
mu.grid(row=5,column=1,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

#  % button
re=Button(x,text='%',command=lambda:z('%'),border=5)
re.grid(row=6,column=0,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

# / button
di=Button(x,text='÷',command=lambda:z('/'),border=5)
di.grid(row=6,column=1,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

# <--- button
delet=Button(x,text='<--',command=lambda:de(),border=5)
delet.grid(row=6,column=2,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

#  ( button
p1=Button(x,text='(',command=lambda:z('('),border=5)
p1.grid(row=7,column=0,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

# ) button
p2=Button(x,text=')',command=lambda:z(')'),border=5)
p2.grid(row=7,column=1,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

# clear buttton
c1=Button(x,text='clear',border=5,command=lambda:cl(),fg='#00ffff')
c1.grid(row=7,column=2,ipadx=40,ipady=25,columnspan=1,sticky='nsew')

x.mainloop()
    
    
    
