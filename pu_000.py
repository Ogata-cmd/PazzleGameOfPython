# This software is licensed under the Python Software Foundation License.
# See the LICENSE file for more details.
# Copyright (c) [2024] [Kosuke Muramatsu]

import tkinter as tk
import subprocess
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# ドラッグ開始時の位置を記録
def start_drag(event):
    global drag_data
    drag_data["x"] = event.x
    drag_data["y"] = event.y

# ドラッグ中の画像移動
def drag(event):
    global label_displayed  # ラベル表示状態を管理するフラグ

    dx = event.x - drag_data["x"]
    dy = event.y - drag_data["y"]

    # 現在の画像位置を取得して更新
    canvas.move(image_id, dx, dy)
    drag_data["x"] = event.x
    drag_data["y"] = event.y

    # 画像の現在位置を確認
    coords = canvas.coords(image_id)
    #print(f"現在の座標: x={coords[0]}, y={coords[1]}")

    # 画像が特定の位置に来たら1回だけラベルを表示
    if 10 <= coords[0] <= 20 and 10 <= coords[1] <= 25 and not label_displayed:
        canvas.create_image(0, 0, image=image2, anchor="nw")
        label = tk.Label(root, text="おめでとう")
        label.pack()
        label_displayed = True  # ラベルを表示済みにする    
    # other_script.py を実行
        root.destroy()
        subprocess.run(["python", resource_path("pu_001.py")])


# メインウィンドウの設定
root = tk.Tk()
root.title("ドラッグ＆ドロップ")

# Canvasの作成
canvas = tk.Canvas(root, width=560, height=420, bg="white")
canvas.pack(fill="both", expand=True)

# 画像のロード
img_path = resource_path("images/gazou1.png")  # 画像ファイルのパスを指定
image = tk.PhotoImage(file=img_path)
image2 = tk.PhotoImage(file=resource_path("images/gazou3.png"))
image3 = tk.PhotoImage(file=resource_path("images/gazou2.png"))

# 背景画像をCanvasに配置
bg_image_id = canvas.create_image(0, 0, image=image3, anchor="nw")
canvas.tag_lower(bg_image_id)  # 背景画像を最背面に配置

# ドラッグ可能な画像をCanvasに配置
image_id = canvas.create_image(100, 100, image=image, anchor="nw")

# ドラッグ情報を保存する辞書
drag_data = {"x": 0, "y": 0}

# ラベル表示フラグ
label_displayed = False

# Canvasにドラッグイベントをバインド
canvas.tag_bind(image_id, "<ButtonPress-1>", start_drag)
canvas.tag_bind(image_id, "<B1-Motion>", drag)

# メインループ
root.mainloop()
