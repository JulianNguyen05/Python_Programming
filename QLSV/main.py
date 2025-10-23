"""
Minh họa OOP
"""

# Định nghĩa lớp sinh viên
class Student:
    # Thuộc tính tĩnh chứa tổng số SV được tạo ra
    totalCount = 0
    # Phương thức khởi tạo
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
    # Pương thức in thông tin SV
    def DisplayInfo(self):
        print("Student ID:", self.id)
        print("Student Name:", self.name)
        print("Student Grade:", self.grade)
    # Nạp chồng phương thức
    @property
    def ToString(self):
        return (f"{self.id}\t{self.name}\t{self.grade}")

# Chương trình chính
if __name__ == '__main__':
    # Khởi tạo đô tượng sinh viên
    student1 = Student("65133958", "trongdepzai", 8.56)
    # student.DisplayInfo()
    print(student1.ToString)
    #
    student2 = Student("65123456", "Julian", 7.89)
    print(student2.ToString)
