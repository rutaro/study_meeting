import numpy as np
#行列aを作成する
A = np.array([[5, 6, 4],
              [5, 8, 3],
              [3, 4, 6]],
             np.float64)
print A #Aの表示
invA = np.linalg.inv(A)#aの逆行列b
print invA#invAの表示
#行列及びベクトルの積はnumpy.dotを利用しなければならない
print A*invA#行列積ではないので単位行列とはならない
print np.dot(A,invA)#行列積であり，単位行列が返る
b = np.arange(1,4,1,dtype=np.float64)#ベクトル生成
print b#bの表示
print np.linalg.norm(b)#bのノルムの表示
x = np.linalg.solve(A,b)#Ax=bの解
print x
