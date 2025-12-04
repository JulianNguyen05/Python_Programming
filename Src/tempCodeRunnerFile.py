import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                             QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFormLayout)
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt

class BMIApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator - PyQt6")
        self.setGeometry(100, 100, 400, 350) # Tọa độ x, y, rộng, cao
        
        # Gọi hàm thiết lập giao diện
        self.setup_ui()

    def setup_ui(self):
        """Thiết lập các widget và layout"""
        
        # 1. Layout chính (xếp theo chiều dọc)
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # 2. Tiêu đề ứng dụng
        title_label = QLabel("TÍNH CHỈ SỐ BMI")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 10px;")
        main_layout.addWidget(title_label)

        # 3. Form nhập liệu (Dùng FormLayout cho đẹp: Nhãn - Ô nhập)
        input_layout = QFormLayout()
        
        # Font chữ chung
        font_content = QFont("Arial", 12)

        # Ô nhập chiều cao
        self.txt_height = QLineEdit()
        self.txt_height.setPlaceholderText("Ví dụ: 1.75")
        self.txt_height.setFont(font_content)
        lbl_height = QLabel("Chiều cao (m):")
        lbl_height.setFont(font_content)
        input_layout.addRow(lbl_height, self.txt_height)

        # Ô nhập cân nặng
        self.txt_weight = QLineEdit()
        self.txt_weight.setPlaceholderText("Ví dụ: 65")
        self.txt_weight.setFont(font_content)
        lbl_weight = QLabel("Cân nặng (kg):")
        lbl_weight.setFont(font_content)
        input_layout.addRow(lbl_weight, self.txt_weight)

        main_layout.addLayout(input_layout)

        # 4. Nút Calculate
        self.btn_calc = QPushButton("Calculate")
        self.btn_calc.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.btn_calc.setCursor(Qt.CursorShape.PointingHandCursor)
        # Style cho nút bấm (giống CSS web)
        self.btn_calc.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        # Gán sự kiện click
        self.btn_calc.clicked.connect(self.calculate_bmi)
        main_layout.addWidget(self.btn_calc)

        # 5. Label hiển thị kết quả
        self.lbl_result = QLabel("Kết quả sẽ hiện ở đây")
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_result.setFont(QFont("Arial", 14))
        self.lbl_result.setStyleSheet("background-color: #ecf0f1; border-radius: 5px; padding: 10px; color: #7f8c8d;")
        # Cho phép label tự động xuống dòng nếu text quá dài
        self.lbl_result.setWordWrap(True) 
        main_layout.addWidget(self.lbl_result)
        
        # Thêm khoảng trống co giãn ở dưới cùng để đẩy nội dung lên trên
        main_layout.addStretch()

        self.setLayout(main_layout)

    def calculate_bmi(self):
        """Xử lý logic tính toán"""
        try:
            h_text = self.txt_height.text().replace(',', '.')
            w_text = self.txt_weight.text().replace(',', '.')

            if not h_text or not w_text:
                self.lbl_result.setText("Vui lòng nhập đủ thông tin!")
                self.lbl_result.setStyleSheet("color: red; font-size: 14px;")
                return

            h = float(h_text)
            w = float(w_text)

            if h <= 0 or w <= 0:
                self.lbl_result.setText("Số liệu phải lớn hơn 0!")
                return

            # Tính toán
            bmi = w / (h ** 2)
            
            # Phân loại và chọn màu sắc
            category = ""
            color = ""
            
            if bmi < 18.5:
                category = "Gầy (Thiếu cân)"
                color = "#f39c12" # Cam
            elif 18.5 <= bmi < 24.9:
                category = "Bình thường (Tốt)"
                color = "#27ae60" # Xanh lá
            elif 25 <= bmi < 29.9:
                category = "Thừa cân"
                color = "#d35400" # Cam đậm
            else:
                category = "Béo phì"
                color = "#c0392b" # Đỏ

            # Hiển thị kết quả
            result_text = f"BMI: {bmi:.2f}\n{category}"
            self.lbl_result.setText(result_text)
            
            # Cập nhật style cho label kết quả (đổi màu chữ và làm đậm)
            self.lbl_result.setStyleSheet(f"""
                background-color: #ecf0f1; 
                border-radius: 5px; 
                padding: 10px; 
                color: {color}; 
                font-weight: bold; 
                font-size: 16px;
            """)

        except ValueError:
            QMessageBox.warning(self, "Lỗi nhập liệu", "Vui lòng chỉ nhập số (Ví dụ: 1.75)")

# --- Điểm khởi chạy ứng dụng ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BMIApp()
    window.show()
    sys.exit(app.exec())