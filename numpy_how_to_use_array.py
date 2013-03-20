#import numpy
import numpy as np
import matplotlib.pyplot as plt
pi = np.pi #numpyの中に円周率が用意されている
delta = 0.01*pi#刻み幅の設定
n = np.arange(401)#n=[0,1,2,...,399,400]
x = np.arange(0,4*pi+delta,delta)#x=[0,4*pi]
#n, xのデータ型の確認
print u"data type of x is "+str(n.dtype)
print u"data type of x is "+str(x.dtype)
'''
np.sin()やnp.exp()など関数を使う場合，入力データは#float64となることが望ましい
(CPUは整数演算よりも浮動小数点演算の性能が高いのでintよりもfloat64の方が高速になる)
'''
n = np.arange(401,dtype=np.float64)#データ型を指定することも可能
#nのデータ型の確認
print u"data type of n is "+str(n.dtype)
#任意の関数列は以下のように書ける
y = np.sin(x)*np.exp(-1.0*x)
#グラフ描画
plt.plot(x,y)
plt.show()
