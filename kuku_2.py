num_1 = int(input("行数を入力してください:"))
num_2 = int(input("列数を入力してください:"))


for i in range(1, num_1 + 1):
    for j in range(1, num_2 + 1):
        print(i * j, end=" ")
    print()
