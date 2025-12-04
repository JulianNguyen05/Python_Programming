# Khai báo lớp tkinter 
import tkinter as tk
# Tạo cửa sổ
window = tk.Tk()
# Thêm nhãn chứa câu 'Hello Python GUI from Tkinter'
greeting = tk.Label(text="Hello, Tkinter")
# Đưa nhãn vào window:
greeting.pack()
# Chạy Tkinter event loop
window.mainloop()