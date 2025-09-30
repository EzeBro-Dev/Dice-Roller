import tkinter as tk
import random


root = tk.Tk()
root.title("Dice Roller")
root.geometry("400x300")


title_label = tk.Label(root, text="Dice Roller", font=("Arial", 18))
title_label.pack(pady=10)


result_label = tk.Label(root, text="🎲 ?", font=("Arial", 30))
result_label.pack(pady=20)


def roll_dice():
    dice_value = random.randint(1, 6)
    result_label.config(text=f"🎲 {dice_value}")


roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 14), command=roll_dice)
roll_button.pack(pady=10)


root.mainloop()