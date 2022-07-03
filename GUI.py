from tkinter import *
import os
import runpy
root=Tk()
def myClick(a):
    #exec(open('SnakeGame.py').read())

    #runpy.run_path(path_name='SnakeGame.py')
    #execfile('SnakeGame.py')
    if a==1:
        os.system('python SnakeGame.py')
    if a==2:
        os.system('python main2.py')
    if a==3:
        os.system('python main.py')
    if a==4:
        os.system('python flappy.py')


root.geometry("1000x750")

myButton1=Button(root, text="Snake Game",height=5,width=50, command=lambda:myClick(1))
myButton2=Button(root, text="Off Road Racing",height=5,width=50, command=lambda:myClick(2))
myButton3=Button(root, text="Hill Climb Racing",height=5,width=50, command=lambda:myClick(3))
myButton4=Button(root, text="Flappy Bird",height=5,width=50, command=lambda:myClick(4))
myButton1.grid(row=1, column=3, pady=20, padx=300)
myButton2.grid(row=2, column=3, pady=20, padx=300)
myButton3.grid(row=3, column=3, pady=20, padx=300)
myButton4.grid(row=4, column=3, pady=20, padx=300)
Label(root, text= "Games", font= ('Helvetica 40 bold',20)).grid(row=0, column=3, padx= 25, pady= 25)

#myButton1.pack(row=0, column=3, pady=20)
#myButton2.pack(row=2, column=3, pady=20)
#myButton3.pack(row=3, column=3, pady=20)
#myButton4.pack(row=4, column=3, pady=20)
root.mainloop()
