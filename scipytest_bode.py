# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:10:14 2013
scipy.signalを利用したボード線図の描画
ここで使用する関数はscipyのversion 0.11.0以降で利用可能
@author: ***
"""

from scipy import signal#scipy.signalのインポート
import matplotlib.pyplot as plt#pyplotのインポート
import matplotlib as mpl

mpl.rcParams['axes.grid']=True

#伝達関数の設定にはsignal.ltiを利用する
#1つ目の要素が伝達関数の分子，2つ目が分母になる．
#分母分子に複数の要素があると先頭が最大次数になる．
s1 = signal.lti([100], [1,100])
#伝達関数を元に周波数とマグニチュード(dB)と角度（deg）を返す
w, mag, phase = s1.bode()

#グラフ描画
plt.figure()
plt.subplot(211)
plt.semilogx(w, mag)
plt.subplot(212)
plt.semilogx(w, phase)
