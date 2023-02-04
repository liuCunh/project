import csv

# 第一题
with open("7-1.txt", 'r', encoding="GBK") as f:
    data = f.read()
    print(data)

# 第三题
print("第三题：")
with open("animal.csv", 'r', encoding="utf-8") as f:
    data = csv.reader(f)
    for i in data:
        print(i)

# 第四题
print("\n第四题：")
with open("write.txt", 'w', encoding="utf-8") as f:
    f.write("Hello world!")
with open("write.txt") as f_write:
    print(f_write.read())

# 第二题
print('\n第二题：')
with open("9.txt", 'r', encoding="utf-8") as f:
    data = f.read()
    print(data)


# # 文件读操作
# with open("7-1.txt", 'r', encoding="GBK") as f:
#     data = f.read()
#     print(data)
#
# # 文件写操作
# with open("7-2.txt", "w", encoding="utf-8") as f:
#     f.write("Hello World!")
#
# # 读取csv文件
# with open(r"C:\Users\Administrator.DESKTOP-EUL9NJU\Desktop\Dir\CSV_file.csv", "r") as csv_f:
#     data = csv.reader(csv_f)  # 读取CSV文件操
#     print(data)
#     for i in data:
#         print(i)
