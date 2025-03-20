# ---------------------------- IMPORT PACKAGES ------------------------------- #

import tkinter as tk

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Flashcard")
window.config(bg= "skyblue")

# Center the window
WINDOW_WIDTH, WINDOW_HEIGHT = 680, 440
x_pos = (window.winfo_screenwidth() - WINDOW_WIDTH) // 2
y_pos = (window.winfo_screenheight() - WINDOW_HEIGHT) // 2
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_pos}+{y_pos}")

# canvas = tk.Canvas(window, width= 400, height= 400, bg= "white")




window.mainloop()