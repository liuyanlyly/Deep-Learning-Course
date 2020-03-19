
x = [64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
y = [62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]
sumx = 0
for i in range(len(x)):
    sumx += x[i]
x1 = sumx / len(x)
sumy = 0
for j in range(len(y)):
    sumy / len(y)
y1 = sumy / len(y)
up = 0
down = 0
for i in range(10):
    up += (x[i] - x1) * (y[i] - y1)
    down += (x[i] - x1) * (x[i] - x1)
w = up / down
print(w)
b = y1 - w * x1
print(b)