from matplotlib import pyplot as plt
import numpy as np

def sigmoid(x):
    return 1. / (1 + np.exp(-x))

def relu(x):
    return np.where(x<0,0,x)

def plot_sigmoid():
    x=np.linspace(-6,6,1000)  #这个表示在-5到5之间生成1000个x值
    y = sigmoid(x)
    plt.xlim((-5, 5))
    plt.ylim((0.00, 1.00))
    plt.yticks([0, 0.5, 1.0], [0, 0.5, 1.0])  # 设置y轴显示的刻度
    plt.plot(x, y, label='sigmoid', color='darkblue')  # 用上述生成的1000个xy值对生成1000个点
    ax = plt.gca()
    ax.spines['right'].set_color('none')  # 删除右边框设为无
    ax.spines['top'].set_color('none')  # 删除上边框设为无
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))  # 调整x轴位置
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))  # 调整y轴位置
    plt.legend(['sigmoid'])
    plt.show()

def plot_relu():
    x = np.linspace(-10, 10)
    y=relu(x)
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111)

    ax = plt.gca()  # 获得当前axis坐标轴对象
    ax.spines['right'].set_color('none')  # 去除右边界线
    ax.spines['top'].set_color('none')  # 去除上边界线

    ax.xaxis.set_ticks_position('bottom')  # 指定下边的边作为x轴
    ax.yaxis.set_ticks_position('left')  # 指定左边的边为y轴

    ax.spines['bottom'].set_position(('data', 0))  # 指定data 设置的bottom（也就是指定的x轴）绑定到y轴的0这个点上
    ax.spines['left'].set_position(('data', 0))  # 指定y轴绑定到x轴的0这个点上

    plt.plot(x, y, label='ReLU', linestyle='-', color='blue')
    plt.legend(['ReLU'])
    plt.show()
if __name__=="__main__":
    plot_sigmoid()
    plot_relu()




