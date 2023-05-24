#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog

def create_new_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            # ファイルに初期内容を書き込む場合はここで行う
            pass
        print("新規ファイルが作成されました:", file_path)

# ウィンドウの作成
window = tk.Tk()
window.title("新規ファイル作成")

# 新規作成ボタンの作成
create_button = tk.Button(window, text="新規作成", command=create_new_file)
create_button.pack()

# ウィンドウのメインループ
window.mainloop()