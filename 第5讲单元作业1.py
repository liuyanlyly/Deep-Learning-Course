import numpy as np
arr = np.random.seed(612)
arr = np.random.uniform(0, 1, 1000)
i = 1
n = int(input('请输入一个1-100之间的整数：'))
print('序号\t索引值\t随机数')
for x in range(n, 1000, n):
    print(i, x, arr[x], sep='\t')
    i += 1
