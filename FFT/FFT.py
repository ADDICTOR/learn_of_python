import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft

x = np.linspace(0, 2*np.pi, 160)
y1 = np.sin(x)
y2 = np.sin(x+np.pi/3)

#################
yf1 = fft(y1)
yreal1 = yf1.real
yimag1 = yf1.imag

yf1_abs = abs(yf1) # 取绝对值
yf1_unif = abs(yf1)/len(y1) # 归一化处理
yf1_half = yf1_unif[range(int(len(y1)/2))] # 由于对称性，只取一半区间

xf1 = np.arange(len(y1)) # 频率
xf1_half = xf1[range(int(len(y1)/2))] # 取一半区间

#################
yf2 = fft(y2)
yreal2 = yf2.real
yimag2 = yf2.imag

yf2_abs = abs(yf2) # 取绝对值
yf2_unif = abs(yf2)/len(y2) # 归一化处理
yf2_half = yf2_unif[range(int(len(y2)/2))] # 由于对称性，只取一半区间

xf2 = np.arange(len(y2)) # 频率
xf2_half = xf2[range(int(len(y2)/2))] # 取一半区间

################
angle1 = []
angle2 = []

for i in range(len(yreal1)):
    angle1.append(np.rad2deg(math.atan(yimag1[i]/yreal1[i])))

for i in range(len(yreal2)):
    angle2.append(np.rad2deg(math.atan(yimag2[i]/yreal2[i])))

###############
plt.subplot(221)
plt.plot(x,y1,'r')
plt.title('y1',fontsize=7,color='#7A378B')

plt.subplot(222)
plt.plot(x,y2,'g')
plt.title('y2',fontsize=7,color='#7A378B')

# plt.subplot(223)
# plt.plot(xf1_half,yf1_half)

# plt.subplot(224)
# plt.plot(xf2_half,yf2_half)

plt.subplot(223)
plt.plot(angle1)
plt.title('y1 angle',fontsize=7,color='#7A378B')

plt.subplot(224)
plt.plot(angle2)
plt.title('y2 angle',fontsize=7,color='#7A378B')

plt.show()