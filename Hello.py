
import math
a = float(input('请输入 a  '))
b = float(input('请输入 b  '))
c = float(input('请输入 c  '))
if a == 0:
    print("a不能为0，不是一元二次方程")
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("无实数解")
    elif delta == 0:
        print("有一个实数解", end=":")
        result = (-b+math.sqrt(delta))/(2*a)
        print(result)
    else:
        print("有两个实数解", end=":")
        result1 = (-b + math.sqrt(delta)) / (2 * a)
        result2 = (-b - math.sqrt(delta)) / (2 * a)
        print(result1, result2)

