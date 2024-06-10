# import matplotlib.pyplot as plt
# import numpy as np
#
# # 定义函数
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
#
# def tanh(x):
#     return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
#
# def relu(x):
#     return np.maximum(0, x)
#
# def leaky_relu(x, alpha=0.1):
#     return np.maximum(alpha * x, x)
#
# # 定义 x 轴范围
# x = np.linspace(-5, 5, 100)
#
# # 创建子图
# fig, axs = plt.subplots(2, 2, figsize=(8, 6))
#
# # 绘制函数图像
# axs[0, 0].plot(x, sigmoid(x), label='Sigmoid')
# axs[0, 0].set_title('(a) Sigmoid')
#
# axs[0, 1].plot(x, tanh(x), label='Tanh')
# axs[0, 1].set_title('(b) Tanh')
#
# axs[1, 0].plot(x, relu(x), label='ReLU')
# axs[1, 0].set_title('(c) ReLU')
#
# axs[1, 1].plot(x, leaky_relu(x), label='Leaky ReLU')
# axs[1, 1].set_title('(d) Leaky ReLU')
#
# # 调整子图间距
# plt.tight_layout()
# plt.savefig('activation_functions.png', dpi=300)
#
# # 显示图像
# plt.show()


import matplotlib.pyplot as plt
import numpy as np


# 定义函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def leaky_relu(x, alpha=0.1):
    return np.maximum(alpha * x, x)


# 定义 x 轴范围
x = np.linspace(-5, 5, 100)

# 创建子图
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# 绘制函数图像
axs[0, 0].plot(x, sigmoid(x), label='Sigmoid')
axs[0, 0].set_title('Sigmoid')

axs[0, 1].plot(x, tanh(x), label='Tanh')
axs[0, 1].set_title('Tanh')

axs[1, 0].plot(x, relu(x), label='ReLU')
axs[1, 0].set_title('ReLU')

axs[1, 1].plot(x, leaky_relu(x), label='Leaky ReLU')
axs[1, 1].set_title('Leaky ReLU')

# 调整子图间距
plt.tight_layout()

# # 设置子图标题位置
# for ax in axs.flat:
#     ax.legend(loc='upper left')

plt.savefig('activation_functions.png', dpi=300)
# 显示图像
plt.show()
