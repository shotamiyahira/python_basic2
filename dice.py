import random
from typing import List

def roll_dice_sided_n(side: int, times: int) -> List[int]:
    result = []

    for _ in range(times):
        dice = random.randint(1, side)
        result.append(dice)

    return result

if __name__ == "__main__":
    n = int(input("サイコロの面の数は？:"))
    m = int(input("何回振りますか？:"))

print(roll_dice_sided_n(side=n, times=m))
