import random

list_nums = [str(round(random.random() * random.randint(-10000, 10000), 2))  for i in range(1000)]
with open("h-w1", "w") as f:
    f.write(";".join(list_nums))

with open("h-w1", "r") as f:

    list_nums1 = []
    for i in list_nums:
        i = round(float(i), 2)
        list_nums1.append(i)
    sum = sum((list_nums1))
    print(sum)