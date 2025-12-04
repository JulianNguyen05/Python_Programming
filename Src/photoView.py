import sys
import os
import time
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, 
                             QLabel, QFileDialog, QMessageBox, QFrame)
from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6.QtCore import Qt

class ImageViewerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ứng dụng Xem Ảnh - PyQt6")
        self.resize(800, 600) # Kích thước mặc định của cửa sổ
        
        # Khởi tạo giao diện
        self.init_ui()

    def init_ui(self):
        """Thiết lập các widget và layout"""
        
        # Tạo layout chính theo chiều dọc
        layout = QVBoxLayout()

        # 1. Hộp (Nút) Open để mở file ảnh
        self.btn_open = QPushButton("Mở File Ảnh")
        self.btn_open.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_open.setStyleSheet("padding: 10px; font-size: 14px; font-weight: bold;")
        self.btn_open.clicked.connect(self.open_image)
        layout.addWidget(self.btn_open)

        # 2. Hộp Image để hiển thị ảnh
        # Sử dụng QLabel để chứa ảnh
        self.lbl_image = QLabel("Chưa có ảnh nào được chọn")
        self.lbl_image.setAlignment(Qt.AlignmentFlag.AlignCenter) # Căn giữa
        self.lbl_image.setStyleSheet("border: 2px dashed #aaa; background-color: #f0f0f0;")
        self.lbl_image.setMinimumHeight(400) # Chiều cao tối thiểu cho vùng xem ảnh
        layout.addWidget(self.lbl_image)

        # 3. Hộp Label để hiển thị thông tin ảnh
        self.lbl_info = QLabel("Thông tin ảnh: Trống")
        self.lbl_info.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)
        self.lbl_info.setWordWrap(True) # Tự động xuống dòng nếu text quá dài
        self.lbl_info.setStyleSheet("padding: 10px; color: #333;")
        layout.addWidget(self.lbl_info)

        # 4. Nút lệnh Close để đóng app
        self.btn_close = QPushButton("Đóng Ứng dụng")
        self.btn_close.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_close.setStyleSheet("""
            QPushButton {
                background-color: #ff4d4d; 
                color: white; 
                padding: 10px; 
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #cc0000;
            }
        """)
        self.btn_close.clicked.connect(self.close)
        layout.addWidget(self.btn_close)

        # Thiết lập layout cho cửa sổ chính
        self.setLayout(layout)

    def open_image(self):
        """Xử lý sự kiện mở file"""
        file_filter = "Image Files (*.png *.jpg *.jpeg *.bmp *.gif *.webp)"
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Chọn file ảnh", 
            "", 
            file_filter
        )

        if file_path:
            self.load_image(file_path)

    def load_image(self, file_path):
        """Hiển thị ảnh và lấy thông tin metadata"""
        try:
            # Tạo đối tượng QPixmap từ đường dẫn file
            pixmap = QPixmap(file_path)

            if pixmap.isNull():
                QMessageBox.warning(self, "Lỗi", "Không thể đọc file ảnh này!")
                return

            # --- Xử lý hiển thị ảnh ---
            # Scale ảnh cho vừa với khung label (giữ tỷ lệ khung hình)
            # Trừ đi một chút padding để không bị tràn
            w = self.width() - 40 
            h = self.lbl_image.height()
            
            scaled_pixmap = pixmap.scaled(
                w, h,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.lbl_image.setPixmap(scaled_pixmap)
            
            # --- Xử lý thông tin ảnh ---
            file_info = self.get_file_metadata(file_path, pixmap)
            self.lbl_info.setText(file_info)

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {str(e)}")

    def get_file_metadata(self, file_path, pixmap):
        """Lấy thông tin chi tiết của file"""
        # Lấy stats từ hệ điều hành
        file_stats = os.stat(file_path)
        
        # 1. Tên file
        file_name = os.path.basename(file_path)
        
        # 2. Kích thước file (đổi sang KB hoặc MB)
        file_size_bytes = file_stats.st_size
        if file_size_bytes < 1024 * 1024:
            file_size_str = f"{file_size_bytes / 1024:.2f} KB"
        else:
            file_size_str = f"{file_size_bytes / (1024 * 1024):.2f} MB"

        # 3. Ngày tạo (Trên Windows là creation time, Unix là change time)
        created_time = time.strftime(
            '%d/%m/%Y %H:%M:%S', 
            time.localtime(file_stats.st_ctime)
        )

        # 4. Độ phân giải thực của ảnh
        resolution = f"{pixmap.width()} x {pixmap.height()} px"

        # Format chuỗi hiển thị
        info_text = (
            f"<b>Tên file:</b> {file_name}<br>"
            f"<b>Độ phân giải:</b> {resolution}<br>"
            f"<b>Dung lượng:</b> {file_size_str}<br>"
            f"<b>Ngày tạo/sửa đổi:</b> {created_time}<br>"
            f"<b>Đường dẫn:</b> {file_path}"
        )
        return info_text

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Thiết lập font chữ chung cho ứng dụng
    font = QFont("Arial", 10)
    app.setFont(font)
    
    window = ImageViewerApp()
    window.show()
    
    sys.exit(app.exec())