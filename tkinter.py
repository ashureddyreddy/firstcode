#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from time import *
def update():
    time_string = strftime("%I:%M:%S %p")
    time_lable.config(text=time_string)
    
    day_string = strftime("%A")
    day_lable.config(text=day_string)
    
    date_string = strftime("%B %d, %Y")
    date_lable.config(text = date_string)
    
    window.after(1000,update)
 
window = Tk()
time_lable = Label(window, font=("arial", 50),fg="#00ff00", bg= "black")
time_lable.pack()
day_lable = Label(window, font=("italic", 25,"bold"))
day_lable.pack()
date_lable = Label(window, font=("em", 30,))
date_lable.pack()
update()

window,mainloop()


# In[ ]:




