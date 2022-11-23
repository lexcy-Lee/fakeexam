def f(x):
    y = -1 * x ** 2 + 3 * x - 2
    return y

temp = 1
while temp <= 2.05:
    print(f"When x = {round(temp,4)} => f(x) = {round(f(temp),4)}")
    temp += 0.05

first1 = f(1)
last1 = f(2)
middle_sum = 0
s = 1.05
while s <= 2.00:
    middle_sum += f(s)
    s += 0.05
h1 = 0.05
total1 = h1 * (first1 + last1 + 2 * middle_sum) / 2
error_percentage = (total1 - 1/6) / total1 * 100

print("First Height:", first1)
print("Last Height:", last1)
print("Middle Sum:", middle_sum)
print("Integration is approximately", total1)
print("True value of integration is 1/6")
print("Therefore the error is", round(abs(error_percentage), 2), "%")

a = int(input("Input real value a: "))
b = int(input("Input real value b: "))
n = int(input("Input non-zero integer n: "))


first2 = f(a)
last2 = f(b)
h = (b - a) / n
sum2 = 0
m = a
while m <= (b + h):
    sum2 += f(m)
    m += h
total2 = h * (first2 + last2 + 2 * sum2) / 2

print(f"Integration from {a} to {b} is approximately {total2}")

quit()