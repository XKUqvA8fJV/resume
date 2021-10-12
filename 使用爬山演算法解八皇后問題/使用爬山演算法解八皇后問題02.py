import numpy as np
import 使用爬山演算法解八皇后問題函式 as 八皇


while 1:
    queen = 10
    queen = np.zeros((queen,queen))
    #建立棋子亂數
    y = np.random.choice(len(queen),len(queen),replace=False).astype(int) #Y軸不重複
    x = np.random.choice(len(queen),len(queen)).astype(int) #X軸可以重複
    #print("repeat")

    coordinate =  np.zeros((len(y),2)) #放入陣列
    for i in range(len(queen)):
        coordinate[i][0] = y[i]
        coordinate[i][1] = x[i]

    #print("coordinate  \n",coordinate)

    for i in range(len(queen)): #放棋子
        queen[  int(coordinate[i][0])  ][  int(coordinate[i][1])  ] = 1
    #print("queen  \n",queen)


    #判斷衝突數，如果就算有衝突但沒進入flag判斷也會跳出去，因為此棋子已經是最低衝突數了不能移動
    flag = 1
    while flag:
        flag = 0 #沒改變退出
        eight = np.array([])
        for i in range(len(coordinate)):
            Aspect = 八皇.九位址衝突數(i,coordinate)
            origin =  Aspect[0][0] #起點原始衝突數
            eight = np.append(eight,origin) #放每個旗子的衝突數

            for y in range(1,len(Aspect)):
                if Aspect[y][0] < origin: #等於不用判斷等於，會進入無窮迴圈
                    origin = Aspect[y][0]
                    coordinate[i][0] = Aspect[y][1]
                    coordinate[i][1] = Aspect[y][2]
                    #print("coordinate改  \n", coordinate.flatten())
                    #print("run")
                    flag = 1 #有改變繼續


    #print("coordinate改  \n",coordinate)

    # 判斷最後全棋子有沒有衝突，如果就算有衝突但沒進入flag判斷也會跳出去，因為此棋子已經是最低衝突數了不能移動，進入死葫蘆，直接全部重新
    if not (eight > 0).any():
        break

queen = np.where(queen,0,0) #全部歸零，重製放棋子
for i in range(len(queen)): #放棋子
    queen[  int(coordinate[i][0])  ][  int(coordinate[i][1])  ] = 1
print("queen:",len(queen),"\n",queen)
#print("eight  \n",eight) #最後全部棋子衝突數確認





