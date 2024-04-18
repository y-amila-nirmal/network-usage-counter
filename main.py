import tkinter
import customtkinter
import ctypes

import psutil
import time

app_window = tkinter.Tk()
app_window.geometry("260x50")
app_window.iconbitmap("icon.ico")
app_window.resizable(False, False)
app_window.title("NET Usage")

app_id = "MOG.NET Usage.null.1.0.0"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

__UPDATING__TIME__ = 10000 # seconds
__TEXT_PLACE_Y_POSTION__ = 10

def get_size(bytes):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}B"
        bytes /= factor


def show_data():
    data:tuple = psutil.net_io_counters(pernic=True)['Wi-Fi']
    send_data = get_size(data[0])
    resive_data = get_size(data[1])
    customtkinter.CTkLabel(app_window, text=send_data, font=("JetBrains Mono", 12)).place(x=61, y=__TEXT_PLACE_Y_POSTION__ )
    customtkinter.CTkLabel(app_window, text=resive_data, font=("JetBrains Mono", 12)).place(x=198 , y=__TEXT_PLACE_Y_POSTION__ )

    print(send_data, resive_data)
    app_window.after(__UPDATING__TIME__, show_data)

customtkinter.CTkLabel(app_window, text="Sending:", font=("JetBrains Mono", 12)).place(x=12, y=__TEXT_PLACE_Y_POSTION__ )
customtkinter.CTkLabel(app_window, text="Receiving:", font=("JetBrains Mono", 12)).place(x=140 , y=__TEXT_PLACE_Y_POSTION__ )

show_data()
app_window.mainloop()
