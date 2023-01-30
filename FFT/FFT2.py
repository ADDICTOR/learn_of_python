import matplotlib.pyplot as plt
import numpy as np


Fs=1400;  #采样频率
Ts=1/Fs;  #采样区间
x=np.arange(0,1,Ts)  #时间向量，1400个

y=np.sin(2*np.pi*180*x)
y2=np.sin(np.pi*180*x+np.pi)

N=1400
frq=np.arange(N)            #频率数1400个数
half_x=frq[range(int(N/2))]  #取一半区间

fft_y=np.fft.fft(y)
fft_y2=np.fft.fft(y2)

abs_y=np.abs(fft_y)                # 取复数的绝对值，即复数的模(双边频谱)
angle_y=180*np.angle(fft_y)/np.pi   #取复数的弧度,并换算成角度
gui_y=abs_y/N                       #归一化处理（双边频谱）                              
gui_half_y = gui_y[range(int(N/2))] #由于对称性，只取一半区间（单边频谱）

abs_y2=np.abs(fft_y2)                # 取复数的绝对值，即复数的模(双边频谱)
angle_y2=180*np.angle(fft_y2)/np.pi   #取复数的弧度,并换算成角度
gui_y2=abs_y2/N                       #归一化处理（双边频谱）                              
gui_half_y2 = gui_y2[range(int(N/2))] #由于对称性，只取一半区间（单边频谱）


#画出原始波形的前50个点
plt.subplot(231)
plt.plot(frq[0:50],y[0:50])   
plt.title('Original waveform 1')

plt.subplot(234)
plt.plot(frq[0:50],y2[0:50])   
plt.title('Original waveform 2')

#画出双边相位谱
plt.subplot(233)
plt.plot(frq[0:50],angle_y[0:50],'violet')
plt.title('phase 1',fontsize=8,color='violet')

#画出双边振幅谱(归一化)
plt.subplot(232)
plt.plot(frq,gui_y,'g')
plt.title('amplitude 1',fontsize=8,color='green')

#画出双边相位谱
plt.subplot(236)
plt.plot(frq[0:50],angle_y2[0:50],'violet')
plt.title('phase 2',fontsize=8,color='violet')

#画出双边振幅谱(归一化)
plt.subplot(235)
plt.plot(frq,gui_y2,'g')
plt.title('amplitude 2',fontsize=8,color='green')

plt.show()
