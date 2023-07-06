input_number1 = int(input("整数を入力してください:"))
input_number2 = int(input("整数を入力してください:"))
input_number3 = int(input("整数を入力してください:"))


# 合計値
print(
    f"合計値:{input_number1 + input_number2 + input_number3}"
    )

# 最大値
number_list = [input_number1, input_number2, input_number3]
max_num = number_list[0]
for num in number_list:
    if num >= max_num:
       max_num = num

print(f"最大値:{max_num}")

# 最小値
number_list = [input_number1, input_number2, input_number3]
min_num = number_list[0] 
for num in number_list:
    if num < min_num:
       min_num = num

print(f"最小値:{min_num}")


# 平均値
number_list = [input_number1, input_number2, input_number3]
total = 0
for num in number_list:
    total += num

result = total / len(number_list)
print(f"平均値:{result}")
