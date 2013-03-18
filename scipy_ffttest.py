# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:33:11 2013
Scipyを用いたFFTと逆FFTによるノイズ除去
@author: ryu
"""

import numpy as np
from scipy import fftpack #for fft
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['figure.autolayout']=True #グラフのはみ出しを回避するためのコマンド
mpl.rcParams['axes.grid']=True

#データ点数
num = 1000
#時間の最小値と最大値
tscale = (0.0, 4.0)

#x = 0, 001, 0.02, ..., 4.99, 5.00
t = np.linspace(tscale[0],tscale[1], num)
#元のデータ：今回は正弦波
y = np.sin(np.pi*t)
#ノイズの入ったデータ．実際のデータにはノイズが乗ることが多い
yn = y + np.random.normal(scale=1,size=num)

#元データとノイズの乗ったデータをプロットする．
plt.subplot(311)#今回3つのグラフを立てに並べるのでサブプロットを使う
plt.plot(t,yn, color='b', linewidth=2, label="raw")
plt.plot(t,y, color='r', linewidth=1, label='ideal')
plt.xlabel("time [s]")
plt.ylabel("Value")
plt.legend(loc=1,fancybox=True)

#上記のデータをFFTしたもの
freq = fftpack.fftfreq(num, ((tscale[1]-tscale[0])/num))
fftY = fftpack.fft(y)
fftYN = fftpack.fft(yn)
plt.subplot(312)
plt.plot(freq[np.where(freq>=0)],np.abs(fftYN)[np.where(freq>=0)],\
         color='b', linewidth=2, label="raw")
plt.plot(freq[np.where(freq>=0)],np.abs(fftY)[np.where(freq>=0)],\
         color='r', linewidth=1, label="ideal")
plt.xlabel("Freq [Hz]")
plt.xlim(0,128)
plt.legend(loc=1,fancybox=True)

#2Hz以上をカットして逆FFT
fftYN[np.where(freq>=1.)] = 0
fftYN[np.where(freq<-1.)] = 0
yn = fftpack.ifft(fftYN)
plt.subplot(313)
plt.plot(t,yn, color='b', linewidth=2, label="ifft")
plt.plot(t,y, color='r', linewidth=1, label='ideal')

plt.xlabel("time [s]")
plt.ylabel("Value")
plt.legend(loc=1,fancybox=True)
plt.savefig("scipyffttest.png", dpi=300)
plt.show()
