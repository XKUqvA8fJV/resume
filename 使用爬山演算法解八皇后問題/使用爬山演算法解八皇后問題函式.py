def 衝突數(coordinate_2,coordinate):
    #輸入座標一(coordinate_2), 其他棋盤座標(coordinate)
    #輸出0 ~ 棋子個數-1
    conflict = 0  # 衝突數目
    for i in range(len(coordinate)):
        #print("i", i)
        if coordinate_2[0] == coordinate[i][0]: #同橫
            conflict += 1
            #print("AA ",coordinate_2[0],coordinate[i][0],coordinate[i][1])
        if coordinate_2[1] == coordinate[i][1]: #同直
            #print("AE ",coordinate_2[1],coordinate[i][0],coordinate[i][1])
            conflict += 1
            #以下斜角等於斜率1或-1
        elif (coordinate[i][0] - coordinate_2[0]) / (coordinate[i][1] - coordinate_2[1]) == 1 or \
                (coordinate[i][0] - coordinate_2[0]) / (coordinate[i][1] - coordinate_2[1]) == -1:
            conflict += 1

    conflict -= 2 #扣掉自己
    return conflict

def 九位址衝突數(w,coordinate):
    # w指定coordinate其中一個棋子移動,其他coordinate棋子陣列
    #w移動時與其他的數目重疊或超出介面直接最大棋子各數輸出
    #輸出順序
    # 	     衝突數目，Y軸，X軸
    # 原點    [ 2.  0.  3.]
    # 東	 [ 4.  0.  4.]
    # 東北	 [ 4. -1.  4.]
    # 北 	 [ 4. -1.  3.]
    # 西北    [ 4. -1.  2.]
    # 西 	 [ 2.  0.  2.]
    # 西南    [ 4.  1.  2.]
    # 南	 [ 1.  1.  3.]
    # 東南	 [ 4.  1.  4.]
    import numpy as np
    import 使用爬山演算法解八皇后問題函式 as 八皇
    import copy
    nine = np.array([])  # 放置方向出衝突數的地方
    coordinate2 = copy.deepcopy(coordinate)  # 複製
    # 原始位址
    yx = np.array([coordinate2[w][0], coordinate2[w][1]])
    nine = np.append(nine, 八皇.衝突數(yx, coordinate2))
    nine = np.append(nine, coordinate2[w][0])
    nine = np.append(nine, coordinate2[w][1])
    # 八個方向位址
    for i in range(8):
        Angle = i * 45  # 0度、45度、90度....
        coordinate2 = copy.deepcopy(coordinate)  # 還原原位址
        if 0 <= Angle < 90 or 270 < Angle <= 360:
            coordinate2[w][1] += 1
        if 90 < Angle < 270:
            coordinate2[w][1] -= 1
        if 180 < Angle < 360:
            coordinate2[w][0] += 1
        if 0 < Angle < 180:
            coordinate2[w][0] -= 1
        yx = np.array([coordinate2[w][0], coordinate2[w][1]])
        # 是否有與其他重疊
        flag = 0
        if len([flag for t2 in range(len(coordinate2)) if (coordinate2[t2] == yx).all()]) >= 2:
            flag = 1
        # 判斷超出邊界和其他重疊
        if yx[0] < 0 or yx[0] > (len(coordinate) - 1) or yx[1] < 0 or yx[1] > (len(coordinate) - 1) or flag:
            nine = np.append(nine, len(coordinate))
            nine = np.append(nine, coordinate2[w][0])
            nine = np.append(nine, coordinate2[w][1])
        else:
            nine = np.append(nine, 八皇.衝突數(yx, coordinate2))
            nine = np.append(nine, coordinate2[w][0])
            nine = np.append(nine, coordinate2[w][1])
    return nine.reshape((-1,3))