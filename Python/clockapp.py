#eventually want it to display the date, weather, and as time passes a little sunrise
#sunset, with a moonrise and moonset, maybe even in that display it takes in the 
#weather information to change the sunset/sunrise animation
from tkinter import *
from tkinter.ttk import *
import time
from time import strftime 
import datetime
#creatin the window
root = Tk()
root.title('Clock')


#function used to display time on the label
def time():
    string = strftime('%H:%M:%S %p'+'%Y:%M:%D:')
    lbl.config(text=string)
    lbl.after(1000, time)

#styling the label, gotta make it look more clock like
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='lavender',
            foreground='black')
""""" still figuring out how to display the date
#putting in the date
date = (currentdate, font=('calibri', 40,'bold'),
        background='lavender',
        foreground='black')
"""

#trying to make it display the date
 
#putting the clock in the center
lbl.pack(anchor='center')
time()
#positioning the date
mainloop()