import tkinter as tk

def increase():
    value=int(label['text'])
    label['text'] = f"{value + 1}"

def decrease():
    value=int(label['text'])
    label['text']=f"{value-1}"

window = tk.Tk()
window.title("+/-")
window.geometry("800x300+400+200")

label = tk.Label(window,
                 text=f"100",
                 font="Arial, 25",
                 bg="blue",
                 width=20,
                 height=2
)

button_1 = tk.Button(window,
    text="+",
    font="Arial, 25",
    bg="green",
    width=10,
    height=2,
    command=increase
)

button_2 = tk.Button(window,
    text="-",
    font="Arial, 25",
    bg="red",
    width=10,
    height=2,
    command=decrease
)

button_1.pack(side=tk.LEFT)
label.pack(side=tk.LEFT)
button_2.pack(side=tk.LEFT)

window.mainloop()
