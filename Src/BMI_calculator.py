import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def phan_loai_bmi(bmi):
    """Hàm trả về đánh giá và màu sắc dựa trên chỉ số BMI"""
    if bmi < 18.5:
        return "Thiếu cân (Gầy)", "#f1c40f" # Màu vàng cam
    elif 18.5 <= bmi < 24.9:
        return "Bình thường (Khỏe mạnh)", "#2ecc71" # Màu xanh lá
    elif 25 <= bmi < 29.9:
        return "Thừa cân", "#e67e22" # Màu cam
    else:
        return "Béo phì", "#e74c3c" # Màu đỏ

def xoa_form():
    """Xóa dữ liệu để nhập lại"""
    h_entry.delete(0, tk.END)
    w_entry.delete(0, tk.END)
    result_value_label.config(text="--", foreground="black")
    result_msg_label.config(text="", foreground="black")
    h_entry.focus()

def bmi_calculate(event=None):
    """Hàm tính toán chính"""
    try:
        # Lấy dữ liệu và xử lý trường hợp nhập dấu phẩy thay vì dấu chấm
        height_txt = h_entry.get().replace(',', '.')
        weight_txt = w_entry.get().replace(',', '.')
        
        if not height_txt or not weight_txt:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ chiều cao và cân nặng!")
            return

        height_cm = float(height_txt)
        weight = float(weight_txt)

        if height_cm <= 0 or weight <= 0:
             messagebox.showerror("Lỗi", "Số liệu phải lớn hơn 0!")
             return

        # Chuyển đổi cm sang m
        height_m = height_cm / 100
        
        # Tính BMI
        bmi = weight / (height_m ** 2)
        
        # Lấy đánh giá và màu sắc
        danh_gia, mau_sac = phan_loai_bmi(bmi)

        # Hiển thị kết quả
        result_value_label.config(text=f'{bmi:.2f}', foreground=mau_sac)
        result_msg_label.config(text=danh_gia, foreground=mau_sac)

    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng chỉ nhập số hợp lệ!")

# --- THIẾT LẬP GIAO DIỆN ---
root = tk.Tk()
root.title('BMI Calculator Pro')
root.geometry("400x450")
root.resizable(False, False)

# Sử dụng Style để giao diện đẹp hơn
style = ttk.Style()
style.theme_use('clam') # Chọn theme hiện đại hơn mặc định
style.configure("TLabel", font=('Segoe UI', 11))
style.configure("TButton", font=('Segoe UI', 11, 'bold'))

# Tạo Frame chính để căn giữa nội dung
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Tiêu đề
title_label = ttk.Label(main_frame, text="TÍNH CHỈ SỐ BMI", font=('Segoe UI', 20, 'bold'), foreground="#34495e")
title_label.pack(pady=(0, 20))

# Khu vực nhập liệu (Dùng Grid trong Frame con)
input_frame = ttk.Frame(main_frame)
input_frame.pack(pady=10)

# Chiều cao
ttk.Label(input_frame, text="Chiều cao (cm):").grid(row=0, column=0, padx=10, pady=10, sticky='e')
h_entry = ttk.Entry(input_frame, font=('Segoe UI', 12), width=10, justify='center')
h_entry.grid(row=0, column=1, padx=10, pady=10)
h_entry.focus() # Đặt con trỏ chuột vào đây khi mở app

# Cân nặng
ttk.Label(input_frame, text="Cân nặng (kg):").grid(row=1, column=0, padx=10, pady=10, sticky='e')
w_entry = ttk.Entry(input_frame, font=('Segoe UI', 12), width=10, justify='center')
w_entry.grid(row=1, column=1, padx=10, pady=10)

# Khu vực nút bấm
btn_frame = ttk.Frame(main_frame)
btn_frame.pack(pady=20)

calc_button = ttk.Button(btn_frame, text='TÍNH NGAY', command=bmi_calculate)
calc_button.pack(side=tk.LEFT, padx=5)

clear_button = ttk.Button(btn_frame, text='NHẬP LẠI', command=xoa_form)
clear_button.pack(side=tk.LEFT, padx=5)

# Khu vực hiển thị kết quả
result_frame = ttk.LabelFrame(main_frame, text="Kết quả của bạn", padding="20")
result_frame.pack(fill=tk.X, pady=10)

result_value_label = ttk.Label(result_frame, text="--", font=('Segoe UI', 24, 'bold'), anchor='center')
result_value_label.pack()

result_msg_label = ttk.Label(result_frame, text="...", font=('Segoe UI', 12, 'italic'), anchor='center')
result_msg_label.pack()

# Ràng buộc phím Enter để tính toán
root.bind('<Return>', bmi_calculate)

root.mainloop()