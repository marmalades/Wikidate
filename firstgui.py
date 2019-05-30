import tkinter as tk

HEIGHT = 300
WIDTH = 400

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

button = tk.Button(root, text="Test button!", bg = 'gray')
button.pack()



root.mainloop()
