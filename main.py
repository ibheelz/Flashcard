import tkinter as tk

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashcard")

PADDING_X = 200  # Extra width padding (wider window)
PADDING_Y = 100  # Height padding

WINE = "#220005"  # Deep, nearly black wine color

try:
    # Load and Resize Image
    img = tk.PhotoImage(file="images/card.png").subsample(3, 3)  # Adjust size
    window.img = img  # Prevent garbage collection

    # Get image dimensions
    img_width, img_height = img.width(), img.height()

    # New window size (extra width for wider look)
    new_width = img_width + (PADDING_X * 2)
    new_height = img_height + (PADDING_Y * 2)

    # Center the window on the screen
    x_pos = (window.winfo_screenwidth() - new_width) // 2
    y_pos = (window.winfo_screenheight() - new_height) // 2
    window.geometry(f"{new_width}x{new_height}+{x_pos}+{y_pos}")

    # Create a canvas with the new padded size
    canvas = tk.Canvas(window, width=new_width, height=new_height, bg=WINE, highlightthickness=0)
    canvas.pack()

    # Display image centered in the padded space
    canvas.create_image(new_width // 2, new_height // 2, image=img)

except tk.TclError:
    # Fallback in case image is missing
    window.geometry("800x400")  # Wider default window
    tk.Label(window, text="Image Missing", font=("Arial", 15, "bold"), bg=WINE, fg="white").pack(expand=True)

window.config(bg=WINE)
window.mainloop()
