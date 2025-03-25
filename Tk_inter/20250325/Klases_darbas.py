import tkinter as tk

window = tk.Tk()
window.title("Lango pavadinimas")
window.geometry("300x300+700+500")

label = tk.Label(window,
                 text="Labas pasauli!",
                 bg="blue",
                 width=50,
)

button = tk.Button(window,
    text="Paspausk mane",
    width=25,
    height=5
)
label.pack()
button.pack()
window.mainloop()
