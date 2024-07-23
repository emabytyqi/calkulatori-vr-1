import tkinter as tk

root = tk.Tk()

#vendosja e hapsires window, titulli i aplikacionit
root.geometry("500x500")

#me label e kena vendos titullin
label = tk.Label(root, text="Miresevini ne kalkulator", font=("arial", 18))
#me .pack() e kena vendos qat sen n window
label.pack(padx = 20, pady = 20)

#e ka kriju nje imput prej metodes .Text()
textbox = tk.Text(root, height=3)
#me .pack() e kena vendos qat sen ne window
textbox.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight = 1)
buttonframe.columnconfigure(1,weight = 1)
buttonframe.columnconfigure(2,weight = 1)

#krijimi i butonave
btn1 = tk.Button(buttonframe, text ="1", font=("arial", 18) )
btn1.grid(row = 0, column = 0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=("arial", 18) )
btn2.grid(row = 0, column = 1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text ="3", font=("arial", 18) )
btn3.grid(row = 0, column = 2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text ="4", font=("arial", 18) )
btn4.grid(row = 1, column = 0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text ="5", font=("arial", 18) )
btn5.grid(row = 1, column = 1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text ="6", font=("arial", 18) )
btn6.grid(row = 1, column = 2, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text ="7", font=("arial", 18) )
btn7.grid(row = 2, column = 0, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text ="8", font=("arial", 18) )
btn8.grid(row = 2, column = 1, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe, text ="9", font=("arial", 18) )
btn9.grid(row = 2, column = 2, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")

root.mainloop()

