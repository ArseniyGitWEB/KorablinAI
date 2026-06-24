# -*- coding: utf-8 -*-
"""
Задание 11 – GitHub API + GUI.
Программа с графическим интерфейсом для получения данных пользователя GitHub.
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import json

def fetch_github_data():
    """Получает данные пользователя GitHub и отображает/сохраняет их."""
    username = entry_username.get().strip()
    if not username:
        messagebox.showerror("Ошибка", "Введите имя пользователя")
        return

    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            result = {
                "company": data.get("company"),
                "created_at": data.get("created_at"),
                "email": data.get("email"),
                "id": data.get("id"),
                "name": data.get("name"),
                "url": data.get("url")
            }
            
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, json.dumps(result, indent=2, ensure_ascii=False))

            filename = f"github_user_{username}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            messagebox.showinfo("Успех", f"Данные сохранены в файл {filename}")
        else:
            messagebox.showerror("Ошибка", f"Пользователь не найден (код {response.status_code})")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка сети", f"Не удалось подключиться: {e}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Что-то пошло не так: {e}")

root = tk.Tk()
root.title("GitHub User Info")
root.geometry("550x450")
root.resizable(False, False)

tk.Label(root, text="Введите имя пользователя GitHub:", font=("Arial", 12)).pack(pady=5)
entry_username = tk.Entry(root, width=40, font=("Arial", 12))
entry_username.pack(pady=5)

btn_fetch = tk.Button(root, text="Получить данные", command=fetch_github_data,
                      bg="#4CAF50", fg="white", font=("Arial", 12), width=20)
btn_fetch.pack(pady=10)

tk.Label(root, text="Результат (JSON):", font=("Arial", 12)).pack()
text_output = scrolledtext.ScrolledText(root, width=65, height=18,
                                        font=("Consolas", 10), wrap=tk.WORD)
text_output.pack(pady=5, padx=10)

root.mainloop()