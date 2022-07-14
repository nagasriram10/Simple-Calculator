from tkinter import *
calc=Tk()
calc.title('Simple Calculator')
calc.configure(background='black')

try:
    calc.iconbitmap('logo.ico')
except:
    pass

calc_width=860
calc_height=500

screen_width=calc.winfo_screenwidth()
screen_height=calc.winfo_screenheight()

x=(screen_width/2)-(calc_width/2)
y=(screen_height/2)-(calc_height/2)

calc.geometry(f'{calc_width}x{calc_height}+{int(x)}+{int(y)}')


credit=Label(calc,text='Designed by Naga Sriram',fg='white',bg='black')

entry_input=Entry(calc,width=59,borderwidth=10,fg='white',bg='black')
exit_input=Entry(calc,width=59,borderwidth=10,fg='white',bg='black')

exit_input.insert(0,'Result: 0')

def click(key):
    entry_input.insert(END,key)
def clear():
    entry_input.delete(0,END)
    exit_input.delete(0,END)
    exit_input.insert(0,'Result: 0')
def backspace():
    text=str(entry_input.get())
    new_text=text[:-1]
    if len(text)==1:
        clear()
    else:
        entry_input.delete(0,END)
        entry_input.insert(0,new_text)
def equal():
    final_entry=entry_input.get()
    final=final_entry.replace('x','*')
    try:
        result='Result: '+str(eval(final))
    except ZeroDivisionError:
        result="Error: Number can't be divided by zero"
    except Exception:
        result='Error: Please enter valid expression'
    finally:
        exit_input.delete(0,END)
        exit_input.insert(0,result)   
        
button_0=Button(calc,text='0',padx=68,pady=10,fg='white',bg='black',command= lambda:click('0'))

button_1=Button(calc,text='1',padx=68,pady=10,fg='white',bg='black',command=lambda:click('1'))
button_2=Button(calc,text='2',padx=75,pady=10,fg='white',bg='black',command=lambda:click('2'))
button_3=Button(calc,text='3',padx=75,pady=10,fg='white',bg='black',command=lambda:click('3'))

button_4=Button(calc,text='4',padx=68,pady=10,fg='white',bg='black',command=lambda:click('4'))
button_5=Button(calc,text='5',padx=75,pady=10,fg='white',bg='black',command=lambda:click('5'))
button_6=Button(calc,text='6',padx=75,pady=10,fg='white',bg='black',command=lambda:click('6'))

button_7=Button(calc,text='7',padx=68,pady=10,fg='white',bg='black',command=lambda:click('7'))
button_8=Button(calc,text='8',padx=75,pady=10,fg='white',bg='black',command=lambda:click('8'))
button_9=Button(calc,text='9',padx=75,pady=10,fg='white',bg='black',command=lambda:click('9'))

button_add=Button(calc,text='+',padx=62,pady=10,fg='orange',bg='black',command=lambda:click('+'))
button_sub=Button(calc,text='-',padx=64,pady=10,fg='orange',bg='black',command=lambda:click('-'))
button_mul=Button(calc,text='x',padx=75,pady=10,fg='orange',bg='black',command=lambda:click('x'))
button_div=Button(calc,text='/',padx=65,pady=10,fg='orange',bg='black',command=lambda:click('/'))

button_equal=Button(calc,text='=',padx=62,pady=10,fg='white',bg='orange',command=equal)
button_decimal=Button(calc,text='.',padx=65,pady=10,fg='orange',bg='black',command=lambda:click('.'))
button_clear=Button(calc,text='Clear',padx=50,pady=10,fg='orange',bg='black',command=clear)
button_backspace=Button(calc,text='<',padx=75,pady=10,fg='orange',bg='black',command=backspace)

button_leftbracket=Button(calc,text='(',padx=77,pady=10,fg='white',bg='black',command=lambda:click('('))
button_rightbracket=Button(calc,text=')',padx=77,pady=10,fg='white',bg='black',command=lambda:click(')'))


for i in range(8):
    Grid.rowconfigure(calc, index=i, weight=1)

for i in range(4):
    Grid.columnconfigure(calc, index=i, weight=1)


credit.grid(row=7,column=0,columnspan=5,sticky='nsew')
entry_input.grid(row=0,column=0,columnspan=4,sticky='nsew')
exit_input.grid(row=6,column=0,columnspan=4,sticky='nsew')

button_0.grid(row=5,column=0,sticky='nsew')

button_1.grid(row=4,column=0,sticky='nsew')
button_2.grid(row=4,column=1,sticky='nsew')
button_3.grid(row=4,column=2,sticky='nsew')

button_4.grid(row=3,column=0,sticky='nsew')
button_5.grid(row=3,column=1,sticky='nsew')
button_6.grid(row=3,column=2,sticky='nsew')

button_7.grid(row=2,column=0,sticky='nsew')
button_8.grid(row=2,column=1,sticky='nsew')
button_9.grid(row=2,column=2,sticky='nsew')

button_add.grid(row=2,column=3,sticky='nsew')
button_sub.grid(row=1,column=3,sticky='nsew')
button_mul.grid(row=1,column=2,sticky='nsew')
button_div.grid(row=3,column=3,sticky='nsew')

button_equal.grid(row=5,column=3,sticky='nsew')
button_decimal.grid(row=4,column=3,sticky='nsew')
button_clear.grid(row=1,column=0,sticky='nsew')
button_backspace.grid(row=1,column=1,sticky='nsew')

button_leftbracket.grid(row=5,column=1,sticky='nsew')
button_rightbracket.grid(row=5,column=2,sticky='nsew')

l=[credit,entry_input,exit_input,button_0,button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_add,button_mul,button_sub,button_div,button_equal,button_decimal,button_clear,button_backspace,button_leftbracket,button_rightbracket]

def resize(e):
    wid=e.width
    button_newsize=int((16*wid)/(900))
    for i in l:
        i.config(font=('Arial',button_newsize))


calc.bind('<Configure>',resize)


calc.mainloop()
