class XeHoi:
    def __init__(self, maSP, tenModel, namSX, giaBan):
        self.maSP = maSP
        self.tenModel = tenModel
        self.namSX = namSX
        self.giaBan = giaBan

    def nhap_thong_tin():
        print('Nhập thông tin: ')
        maSP = input('Mã sản phẩm: ')
        tenModel = input('Tên model: ')
        namSX = int(input('Năm sản xuất: '))
        giaBan = float(input('Giá bán: '))
        return XeHoi(maSP, tenModel, namSX, giaBan)

    def in_thong_tin(self):
        print("Thông tin xe hơi: " +
              "\nMã sản phẩm: " + self.maSP +
              "\nTên model:  " + self.tenModel +
              "\nNăm sản xuất: " + self.namSX +
              "\nGiá bán: " + self.giaBan)

if __name__ == '__main__':
    # Nhap danh sach xe
    while True:
        n = int(input("Nhập danh sách xe(2 < n < 100): "))
        if 2 < n < 100:
            print(f"Bạn đã nhập đúng n = {n}")
            break
        else:
            print(f"n không thỏa mãn")

    # Tao 1 danh sach xe
    ds_xe = []
    for i in range(n):
        i = XeHoi.nhap_thong_tin()
        ds_xe.append(i)

    # In danh sach xe
    print("===Danh sách xe===")
    for i in ds_xe:
        i.in_thong_tin()

    # Xe ban gia cao nhat
    max_xe = max(ds_xe, key=lambda x: x.giaBan)
    print("==Xe có giá bán cao nhất==")
    print(max_xe.in_thong_tin())

    # Sap xep
    print("===Thông tin của danh sách xe sau khi sắp xếp===")
    ds_xe.sort(key=lambda x: x.namSX, reverse=True)
    for x in ds_xe:
        x.in_thong_tin()

