# This software is licensed under the Python Software Foundation License.
# See the LICENSE file for more details.
# Copyright (c) [2024] [Kosuke Muramatsu]
import tkinter as tk
import os
import sys
import subprocess

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def click_on():
    root.destroy()
    subprocess.run(["python", resource_path("pu_000.py")])

root = tk.Tk()

gazou = tk.PhotoImage(file=resource_path("images/button.png"))
gazou2 = tk.PhotoImage(file=resource_path("images/title.png"))

label = tk.Label(image=gazou2)
label.pack()

button_main = tk.Button(root, image=gazou, command=click_on)
button_main.pack()
root.mainloop()
