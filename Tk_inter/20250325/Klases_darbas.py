import tkinter as tk
window = tk.Tk()
label = tk.Label(window, text="Labas pasauli!", bg="blue")

button = tk.Button(window,
    text="Paspausk mane",
    width=25,
    height=5
)
label.pack()
button.pack()
window.mainloop()
