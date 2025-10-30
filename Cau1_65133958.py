
if(__name__=='__main__'):
    # Nhập 1 chuỗi ký tự từ bán phím
    s = input("Nhập chuỗi ký tự: ")

    # In chỗi theo thứ tự các từ đảo ngược
    words = s.split()
    re_str = ''.join(reversed(words))
    print(re_str)

    # Đếm số ký tự in hoa có trong chỗi
    count_s = sum(1 for ch in s if ch.isupper())
    print(count_s)

    # Xử lý chuẩn hóa chuỗi
    nor_s = ''.join(s.strip().split())
    print(nor_s)

    # In ra từ xuất hiện nhiều nhất
    words = s.split()
    # print(words)
    # Tạo từ điển chứa số lần xuất hiện của mỗi từ
    word_count = {}
    # Xét từng từ trong danh sách
    for w in words:
        # Kiểm tra nếu từ lần đầu xuất hiện trong từ điển
        # Thì bổ sung từ này vô từ điển & khởi tạo số lượng = 1
        if not w in word_count:
            word_count[w] = 1
        # Ngược lại, nếu từ đã có trong từ điển --> tăng số lượng thêm 1
        else:
            word_count[w] += 1

    # In kết quả
    for k, v in word_count.items():
        print(f"{k}: {v}")

    # Tìm từ xuất hiện nhiều nhất
    most_common_word = max(word_count.items(), key=lambda item: item[1])
    print(f"\nTừ xuất hiện nhiều nhất là: '{most_common_word[0]}' với số lần xuất hiện: {most_common_word[1]}")