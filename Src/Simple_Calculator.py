import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QVBoxLayout, QGridLayout, QPushButton, QLineEdit)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Cài đặt tiêu đề và kích thước cửa sổ
        self.setWindowTitle("Máy Tính PyQt6")
        self.setGeometry(100, 100, 300, 400) # x, y, width, height
        self.setFixedSize(300, 400) # Cố định kích thước để không bị vỡ giao diện

        # Widget chính chứa toàn bộ giao diện
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout chính (xếp theo chiều dọc)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # --- PHẦN 1: MÀN HÌNH HIỂN THỊ ---
        self.display = QLineEdit()
        self.display.setFixedHeight(50) # Chiều cao màn hình
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight) # Căn phải chữ
        self.display.setReadOnly(True) # Chỉ cho phép nhập qua nút bấm, không gõ phím
        
        # Font chữ to, rõ ràng
        font = QFont("Arial", 20)
        self.display.setFont(font)
        
        self.main_layout.addWidget(self.display)

        # --- PHẦN 2: CÁC NÚT BẤM (GRID LAYOUT) ---
        self.buttons_layout = QGridLayout()
        self.buttons_layout.setSpacing(5) # Khoảng cách giữa các nút
        self.main_layout.addLayout(self.buttons_layout)

        # Danh sách các nút và vị trí của chúng trong lưới (row, col)
        # Cấu trúc: [Ký tự, Hàng, Cột, Số hàng chiếm (tùy chọn), Số cột chiếm (tùy chọn)]
        buttons = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0, 1, 2), # Số 0 chiếm 2 cột
            ('.', 4, 2), 
            ('=', 4, 3)
        ]

        # Tạo style (CSS) cho các nút để đẹp hơn
        button_style = """
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """
        
        # Style riêng cho nút '=' và 'C'
        special_style = """
            QPushButton {
                background-color: #ff9f43; 
                color: white; 
                font-weight: bold;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover { background-color: #ffb166; }
        """

        # Vòng lặp tạo các nút
        for config in buttons:
            text = config[0]
            row = config[1]
            col = config[2]
            
            # Kiểm tra xem nút có chiếm nhiều ô không (rowspan, colspan)
            row_span = config[3] if len(config) > 3 else 1
            col_span = config[4] if len(config) > 4 else 1

            button = QPushButton(text)
            button.setFont(QFont("Arial", 14))
            
            # Áp dụng màu sắc
            if text in ['=', 'C']:
                button.setStyleSheet(special_style)
            else:
                button.setStyleSheet(button_style)

            # Kết nối sự kiện click
            # Sử dụng lambda để truyền tham số text vào hàm xử lý
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))

            # Thêm nút vào lưới
            self.buttons_layout.addWidget(button, row, col, row_span, col_span)

    def on_button_click(self, text):
        """Hàm xử lý logic khi người dùng bấm nút"""
        current_text = self.display.text()

        if text == 'C':
            # Xóa màn hình
            self.display.clear()
        
        elif text == '=':
            # Tính toán kết quả
            try:
                # Hàm eval() của Python sẽ tính toán chuỗi phép tính (VD: "2+2")
                # Lưu ý: eval() chỉ nên dùng cho app đơn giản như này
                result = str(eval(current_text))
                self.display.setText(result)
            except ZeroDivisionError:
                self.display.setText("Lỗi chia 0")
            except SyntaxError:
                self.display.setText("Lỗi cú pháp")
            except Exception:
                self.display.setText("Lỗi")
        
        else:
            # Thêm ký tự vừa bấm vào màn hình
            # Nếu màn hình đang báo lỗi, xóa đi rồi mới nhập số mới
            if "Lỗi" in current_text:
                self.display.setText(text)
            else:
                self.display.setText(current_text + text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())