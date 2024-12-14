from tkinter import*
from tkinter.ttk import*
import time
root=Tk()
progressbar=Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
progressbar.pack(pady=50)
def bar():
  progressbar['value']=1
  root.update_idletasks()
  time.sleep(1) 

  progressbar['value']=20
  root.update_idletasks()
  time.sleep(1) 

  progressbar['value']=48
  root.update_idletasks()
  time.sleep(1) 

  progressbar['value']=67
  root.update_idletasks()
  time.sleep(1)
  
  progressbar['value']=78
  root.update_idletasks()
  time.sleep(1)

  progressbar['value']=95
  root.update_idletasks()
  time.sleep(1)

  progressbar['value']=99
  root.update_idletasks()
  time.sleep(1)

  progressbar['value']=100
  root.update_idletasks()
  time.sleep(1)
Button(root,text='Start',command=bar).pack()
 
root.mainloop()
