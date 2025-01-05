def sum(num):
    if num == 1:
        return num
    else:
        num += sum(num-1)
    return num

print(sum(999))