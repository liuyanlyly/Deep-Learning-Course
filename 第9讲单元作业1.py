# 使用9.5小节中的“商品房销售记录表”作为样本数据，编程实现一个房价预测系统。
# 要求：
# 1. 矩阵运算部分采用TensorFlow实现，数据加载、输入、输出等可以根据需要采用Python/NumPy来实现。
# 2. 提示用户输入商品房面积和房间数，并进行输入校验。合理的输入如下：
# 面积：20-500之间的实数
# 房间数：1-10之间的整数
# 如果输入正确，根据模型估计房价，并显示。
# 如果输入数据类型错误，或者输入数据范围不合理，根据错误类型提示，并等待用户重新输入。
# 提示：TensorFlow中矩阵求逆函数tf.linalg.inv(）
#
#
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

x1 = np.array(
    [137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26,
     86.21])
x2 = np.array([3, 2, 2, 3, 1, 2, 3, 2, 2, 3, 1, 1, 1, 1, 2, 2])
y = np.array(
    [145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00, 62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69,
     95.30])
x0 = np.ones(16)
X = np.stack((x0, x1, x2), axis=1)
Y = np.array(y).reshape(-1, 1)
Xt = np.transpose(X)
XtX_1 = np.linalg.inv(np.matmul(Xt, X))
XtX_1_Xt = np.matmul(XtX_1, Xt)
W = np.matmul(XtX_1_Xt, Y)
W = W.reshape(-1)

while 1:
    square = float(input("商品房面积（20-500）："))
    if square in range(20, 500):
        break
    else:
        print('（面积）输入数据范围不合理!请重新输入！')

while 1:
    rooms = float(input("房间数(1-10)："))
    if rooms in range(1, 10):
        break
    else:
        print('（房间数）输入数据范围不合理!请重新输入！')

price = square * W[1] + square * W[2] + W[0]
print("房价是：", np.round(price, 2))
