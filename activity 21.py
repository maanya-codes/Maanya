a = 1
b = 2
c = 3
d = 4
ans = b ** c + d / b * c  + a
print(ans)

n1 = int(input("Enter numerator:"))
n2 = int(input("Enter denominator:"))

if n1 % n2 == 0:
    print(str(n1), "is divisible by", str(n2))
else:
    print(str(n1), "is NOT divisible by", str(n2))