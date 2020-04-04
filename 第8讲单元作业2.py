# 使用TensorFlow张量运算计算w和b，并输出结果。
# 已知：
# x=[ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
# y=[ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]
# 计算：
# 其中，是x中索引值为i的元素；是y中索引值为i的元素；n是张量中元素的个数。
# (3)分别输出W和b的结果。
import tensorflow as tf
x = tf.constant([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
sum_xy = tf.constant(0.)
sum_x = tf.constant(0.)
sum_y = tf.constant(0.)
sum_xx = tf.constant(0.)
for i in range(10):
    sum_xy += x[i]*y[i]
    sum_x += x[i]
    sum_y += y[i]
    sum_xx += x[i]*x[i]
w = tf.divide(sum_xy-sum_x*sum_y, sum_xx-sum_x*sum_x)
b = tf.divide(sum_y-w*sum_x, 10)
#将张量类型转换为ndarray输出
session = tf.Session()
w_ndarray = w.eval(session=session)
b_ndarray = b.eval(session=session)
print("w={}\nb={}".format(w_ndarray, b_ndarray))

