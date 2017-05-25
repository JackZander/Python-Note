secredcode = input("请输入暗码：")
for q in secredcode:
    if ord("a") <= ord(q) <= ord("z"):
        print(chr(ord("a") + (ord(q) - ord("a") - 3) % 26), end='')
    else:
        print(q, end='')