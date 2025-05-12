import tkinter as tk
from datetime import datetime
import winsound

import pystray
from PIL import Image

def on_quit(icon, item):
    icon.stop()
    root.quit()

def show_icon():
    image = Image.open("icon.png")
    menu = (pystray.MenuItem('Quit', on_quit),)
    icon = pystray.Icon("MyApp", image, "My Application", menu)
    icon.run()
    

def play_sound():
    """Plays a notification sound."""
    winsound.Beep(2500, 500)

def update_timer():
    """Updates the timer and changes modes based on the current minute."""
    now = datetime.now()
    current_minute = now.minute
    current_second = now.second

    if current_minute % 30 < 25:
        mode = "Belajar"
        time_remaining = 25 * 60 - (current_minute % 30 * 60 + current_second)
        bg_color = "#FFC1C1"  # Light pink
    else:
        mode = "Istirahat"
        time_remaining = 30 * 60 - (current_minute % 30 * 60 + current_second)
        bg_color = "#C1FFC1"  # Light green

    # Play sound at the start of each mode
    if current_second == 0 and current_minute % 30 in (0, 25):
        play_sound()

    minutes = time_remaining // 60
    seconds = time_remaining % 60
    timer_text = f"{minutes:02}:{seconds:02}"

    # label_mode.config(text=mode, bg=bg_color)
    label_timer.config(text=timer_text, bg=bg_color)
    root.config(bg=bg_color)

    root.after(1000, update_timer)  # Update every second

# Create the main tkinter window
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("35x20")  # Default size
root.attributes("-topmost", True)  # Keep the window on top
root.overrideredirect(True)  # Make the window borderless
root.resizable(False, False)  # Disable resizing

# Center the window at the top
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - 17
root.geometry(f"35x20+{x}+0")

# Create widgets
# label_mode = tk.Label(root, text="", font=("Arial", 8, "bold"))
label_timer = tk.Label(root, text="", font=("Arial", 8))

# Pack widgets
# label_mode.grid(row=0, column=0, sticky="w")
label_timer.grid(row=0, column=1, sticky="e")


# Initialize the timer
update_timer()

if __name__ == "__main__":
    # Logika utama aplikasi Anda (mungkin berjalan di thread lain)
    print("Aplikasi berjalan...")
    show_icon() # Panggil fungsi yang membuat dan menjalankan ikon
    print("Aplikasi berhenti.")

# Run the tkinter event loop
root.mainloop()

