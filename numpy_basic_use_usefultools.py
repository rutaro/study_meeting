import numpy as np
a = np.arange(25)#a=[0,1,2,...,23,24]（int）
A = a.reshape((5,5))#こんな風に行列に変換可能
print "a = "+str(a)
print "A = "+str(A)
#乱数生成はnp.random以下に関数がある
#random.normalは正規分布に基づく乱数を生成
B = np.random.normal(loc=0.0, scale=1.0,size=(5,5))
print "B = "+str(B)#Bの表示
#whereで配列中で任意の条件を満たす要素を抽出できる
print "row & col (B>1) is ["+str(np.where(B>1.0))+"]"
print "(B>1)"+str(B[np.where(B>1.0)])
print "% of B>1 is "+str(np.float(B[np.where(B>1.0)].size)/B.size)
