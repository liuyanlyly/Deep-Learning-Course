# 使用TensorFlow张量运算计算w和b，并输出结果。
# 已知：
# x=[ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
# y=[ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]
# 计算：
# 其中和分别为x和y的均值，是x中索引值为i的元素，是y中索引值为i的元素。
# (3)分别输出W和b的结果。
# 提示：
# 正确的输出结果为
# w= 0.83215......
# b= 10.2340.......

import tensorflow as tf
x = tf.constant([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
x1 = tf.reduce_mean(x)
y1 = tf.reduce_mean(y)
upper = tf.constant(0.)
downer = tf.constant(0.)
for i in range(10):
    upper += (x[i] - x1) * (y[i] - y1)
    downer += (x[i] - x1) * (x[i] - x1)
w = tf.divide(upper, downer)
b = y1 - w * x1
#将张量类型转换为ndarray输出
session = tf.Session()
w_ndarray = w.eval(session=session)
b_ndarray = b.eval(session=session)
print("w={}\nb={}".format(w_ndarray, b_ndarray))
