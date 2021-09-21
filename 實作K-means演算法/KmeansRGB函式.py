def NP加座標(img_arr):
    # (輸入NP)
    # 輸出NP每個最後一位附上相素順序
    # 輸出(R,G,B,像素順序)初始設定
    import numpy as np
    from PIL import ImageColor, Image

    #img = img.convert("RGB")  # 轉RGB照片
    #img_arr = np.array(img) # Image轉numpy
    heightLen, widthLen, RGBLen = img_arr.shape #(高，寬，像素顏色)

    # 新增空陣列
    img_arrNew = np.zeros(shape=(heightLen, widthLen, RGBLen + 1)) #RGBLen+1最後一位，像素位址
    CoordinateNum = 0 #像素順序

    for y in range(heightLen):
        for x in range(widthLen):
            for Energy in range(RGBLen):
                img_arrNew[y][x][Energy] = img_arr[y][x][Energy]
                # print(img_arrNew[y][x][Energy])
                # print(img_arr[y][x][Energy])
            img_arrNew[y][x][Energy + 1] = CoordinateNum
            CoordinateNum += 1
    return img_arrNew

def NP加分群(img_arrNew):
    #輸入NP加座標，輸出加一位元判斷分群。
    #輸出(R,G,B,像素順序,群分類)初始設定
    import numpy as np
    heightLen, widthLen, RGBLen = img_arrNew.shape  # (高，寬，像素顏色)
    img_arrNew2 = np.zeros(shape=(heightLen, widthLen, RGBLen + 1))  # RGBLen+1最後一位分群
    for y in range(heightLen):
        for x in range(widthLen):
            for Energy in range(RGBLen):
                img_arrNew2[y][x][Energy] = img_arrNew[y][x][Energy]
                # print(img_arrNew[y][x][Energy])
                # print(img_arr[y][x][Energy])

    return img_arrNew2

def K群(k,img_arrNew2):
    #(K，NP加分群)
    # 開始分群
    #K抓第幾項速順序
    import numpy as np
    height, width, _ = img_arrNew2.shape
    Num = height * width  # 總共幾個像素
    K_means = np.random.choice(Num, size=k, replace=False)  # 取隨機像素位址，replace=False 不重複
    return K_means

def K在原作標位址(Num,img_arrNew2,K_means):
    #(K群號碼，NP加分群，K群)
    #K在原作標位址
    height, width, RGB = img_arrNew2.shape
    for y in range(height):
        for x in range(width):
            if img_arrNew2[y][x][3] == K_means[Num]:
                #print("y x  ", y, x)
                return y, x

def 兩點距離(img_arrNew2,y,x,ky,kx):
    #(NP加分群，座標1y,座標1x,座標2ky,座標2kx)
    return ((img_arrNew2[y][x][0]-img_arrNew2[ky][kx][0])**2 + \
           (img_arrNew2[y][x][1]-img_arrNew2[ky][kx][1])**2 + \
           (img_arrNew2[y][x][2] - img_arrNew2[ky][kx][2]) ** 2)**(1/2)

def 最小距離號碼(Lenadd):
    # 輸入 兩點距離 的矩陣，離輸出最小距離位址
    flag = 0
    LenNum = Lenadd[0]
    for i in range(len(Lenadd)):
        if LenNum > Lenadd[i]:
            LenNum = Lenadd[i]
            flag = i
    return flag

def 最小距離號碼改(Lenadd):
    # 輸入 距離 的矩陣，離輸出最小距離位址
    import numpy as np
    Lenadd = np.reshape(Lenadd, (-1, 2))
    LenNum = Lenadd[0][0]
    flag = Lenadd[0][1]
    for i in range(len(Lenadd)):
        if LenNum > Lenadd[i][0]:
            LenNum = Lenadd[i][0]
            flag = Lenadd[i][1]
    return flag

def 最小距離座標(average):
    #輸入距離陣列，輸出跟陣列最小的座標位址
    import numpy as np
    import KmeansRGB函式
    average = average.reshape(-1, 3)
    #print("average  ", average)
    Num = KmeansRGB函式.最小距離號碼(average[:, 0])
    #print("最小距離號碼 ", KmeansRGB函式.最小距離號碼(average[:, 0]))
    return average[Num][1],average[Num][2]

def 座標轉編號(K_meansNew,img_arrNew2):
    #(K_means座標，修改陣列)
    import numpy as np
    Num = np.array([])
    ky, kx = K_meansNew.shape
    for y in range(ky):
        for x in range(1):
            #print(img_arrNew2[int(K_meansNew[y][x])][int(K_meansNew[y][x + 1])][3])
            Num =np.append(Num, ((img_arrNew2[int(K_meansNew[y][x])][int(K_meansNew[y][x + 1])][3])))
            #print(Num)

    return Num

def 兩點求中心點座標(img_arrNew2,MaxNumY,MaxNumX,MaxNumY2,MaxNumX2):
    #輸入(原始陣列，最遠座標一，最遠座標二)
    #輸出最遠兩點，中心最座標RGB  ex[148.5  86.  155. ]
    import numpy as np
    R = (img_arrNew2[MaxNumY][MaxNumX][0] + img_arrNew2[MaxNumY2][MaxNumX2][0]) / 2
    G = (img_arrNew2[MaxNumY][MaxNumX][1] + img_arrNew2[MaxNumY2][MaxNumX2][1]) / 2
    B = (img_arrNew2[MaxNumY][MaxNumX][2] + img_arrNew2[MaxNumY2][MaxNumX2][2]) / 2
    Center = np.array([])
    Center = np.append(G,B)
    Center = np.append(R,Center)
    return Center

def 各群中心座標改(K_means,img_arrNew2):
    import KmeansRGB函式
    import numpy as np
    height, width, RGB = img_arrNew2.shape
    k_meansNew2 = np.array([])
    for k in range(len(K_means)):
        SumR = 0
        SumG = 0
        SumB = 0
        Cent = 0
        MinLen = 0
        SumMin = np.array([])
        flag = 0
        for y in range(height):
            for x in range(width):
                if img_arrNew2[y][x][RGB - 1] == k:
                    flag += 1
                    SumR = SumR + img_arrNew2[y][x][0]
                    SumG = SumG + img_arrNew2[y][x][1]
                    SumB = SumB + img_arrNew2[y][x][2]
        if flag == 0:
            flag = 1
        SumR = SumR / flag
        SumG = SumG / flag
        SumB = SumB / flag
        # print("SumR,SumG, SumB   ",SumR,SumG, SumB)
        SumG = np.append(SumG, SumB)
        Cent = np.append(SumR, SumG)
        # print(Cent) #近似中心點
        for y in range(height):
            for x in range(width):
                if img_arrNew2[y][x][RGB - 1] == k:
                    MinLen = ((Cent[0] - img_arrNew2[y][x][0]) ** 2 +
                              (Cent[1] - img_arrNew2[y][x][1]) ** 2 +
                              (Cent[2] - img_arrNew2[y][x][2]) ** 2) ** (1 / 2)
                    Num = np.array([[y, x]])
                    Num = KmeansRGB函式.座標轉編號(Num, img_arrNew2)
                    MinLen = np.append(MinLen, Num)
                    SumMin = np.append(SumMin, MinLen)
                    # print(SumMin)
        k_meansNew = KmeansRGB函式.最小距離號碼改(SumMin)
        k_meansNew2 = np.append(k_meansNew2,k_meansNew)
    return  k_meansNew2

def 各K群分類改(K_means,img_arrNew2):
    #(NP加分群，K群)
    import numpy as np
    import KmeansRGB函式

    height, width, RGB = img_arrNew2.shape

    ky = np.array([])
    kx = np.array([])
    for k in range(len(K_means)):  # 此點對每個K點算距離
        ky2, kx2 = KmeansRGB函式.K在原作標位址(k, img_arrNew2, K_means)
        ky = np.append(ky,ky2)
        kx = np.append(kx, kx2)
    #print(ky)
    #print(kx)
    for y in range(height):
        for x in range(width):
            Lenadd = np.array([])
            for k in range(len(K_means)):  # 此點對每個K點算距離
                #ky, kx = KmeansRGB函式.K在原作標位址(k, img_arrNew2, K_means)
                kyy = int(ky[k])
                kxx = int(kx[k])
                Len = KmeansRGB函式.兩點距離(img_arrNew2, y, x, kyy, kxx)
                Lenadd = np.append(Lenadd, Len)
            # 最小
            MineNum = KmeansRGB函式.最小距離號碼(Lenadd)
            img_arrNew2[y][x][RGB - 1] = MineNum
    return img_arrNew2

def 顏色更改及展示(K_means,img_arrNew2):

    import numpy as np
    from PIL import ImageColor, Image
    import KmeansRGB函式
    height, width, RGB = img_arrNew2.shape
    ky = np.array([])
    kx = np.array([])
    for k in range(len(K_means)):
        ky2, kx2 = KmeansRGB函式.K在原作標位址(k, img_arrNew2, K_means)
        ky = np.append(ky, ky2)
        kx = np.append(kx, kx2)
        # print(ky2,kx2)
    # print(ky,kx)

    img_arrNew3 = img_arrNew2
    # print("img_arrNew3  ",img_arrNew3)

    for k in range(len(K_means)):
        kyy = int(ky[k])
        kxx = int(kx[k])
        for y in range(height):
            for x in range(width):
                if img_arrNew2[y][x][RGB - 1] == k:
                    for c in range(RGB - 2):
                        # print(img_arrNew3[y][x][c],end=" ")
                        img_arrNew3[y][x][c] = img_arrNew2[kyy][kxx][c]
                # print(" ")
    img_arrNew4 = img_arrNew3[:, :, :3]
    img = Image.fromarray(np.uint8(img_arrNew4))  # numpy轉Image ，uint8轉編碼
    img = img.convert("RGB")  # 轉回RGB
    #img.show()
    return img
"""
def 各K群分類(K_means,img_arrNew2):
    #(NP加分群，K群)
    import numpy as np
    import KmeansRGB函式

    height, width, RGB = img_arrNew2.shape

    for y in range(height):
        for x in range(width):
            for z in range(RGB - 2):
                Lenadd = np.array([])
                for k in range(len(K_means)):  # 此點對每個K點算距離
                    ky, kx = KmeansRGB函式.K在原作標位址(k, img_arrNew2, K_means)
                    Len = KmeansRGB函式.兩點距離(img_arrNew2, y, x, ky, kx)
                    Lenadd = np.append(Lenadd, Len)
                # 最小
                MineNum = KmeansRGB函式.最小距離號碼(Lenadd)
                img_arrNew2[y][x][RGB - 1] = MineNum

    #print("---------------------------------")
    #print(Lenadd)
    #print(MineNum)
    #print("---------------------------------")
    return img_arrNew2
"""

"""
def 中心點距離兩點距離(img_arrNew2, TwoCenter, y, x):
    #(NP加分群，兩點求中心點座標,座標x,座標y)
    #輸出一個數 距離
    return ((TwoCenter[0] - img_arrNew2[y][x][0]) ** 2 + \
            (TwoCenter[1] - img_arrNew2[y][x][1]) ** 2 + \
            (TwoCenter[2] - img_arrNew2[y][x][2]) ** 2) ** (1 / 2)
"""

"""
def 距離最大的編號(AllLen):
    #AllLen傳入的會是 偶數距離0開始，基數對應編號 ，兩兩配對

    import numpy as np
    AllLen = np.reshape(AllLen, (-1, 2))
    #print(AllLen)
    Ally,Allx = AllLen.shape
    #print("Ally  ", Ally)
    if Ally==1: #只有一個的時候
        return AllLen[0][1]

    Max = AllLen[0][0]
    #print("Max ",Max)
    Num = np.array([])
    flag = 0
    for y in range(Ally):
        if Max < AllLen[y][0]:
            Max = AllLen[y][0]
            Num = AllLen[y][1]
            flag = 1
    if flag == 0: #判斷一開始最大距離的時候的時候
        return AllLen[0][1]
    return Num
"""

"""
def 各群中心座標(K_means,img_arrNew2):
    # 判斷各群的最小中心
    import numpy as np
    import KmeansRGB函式

    height, width, RGB = img_arrNew2.shape
    Len = np.array([])  # 兩點距離
    average = np.array([])  # 此群的全部頻均距離
    K_meansNew = np.array([])

    for k in range(len(K_means)):
        for y in range(height):
            for x in range(width):
                sumLen = 0  # 此點距離總和
                averageNum = 0  # 此群總共幾個值

                if img_arrNew2[y][x][RGB - 1] == k:

                    for y2 in range(height):
                        for x2 in range(width):
                            if img_arrNew2[y2][x2][RGB - 1] == k:
                                Len = KmeansRGB函式.兩點距離(img_arrNew2, y, x, y2, x2)
                                sumLen = sumLen + Len
                                averageNum += 1
                    if averageNum == 1:
                        average = np.append(average, sumLen / averageNum)  # 群唯一一個的時候
                        coordinate = np.array([y, x])  # 附上此距離的座標
                        average = np.append(average, coordinate)  # 附上此距離的座標
                    else:
                        average = np.append(average, sumLen / averageNum - 1)  # 扣掉自己
                        coordinate = np.array([y, x])  # 附上此距離的座標
                        average = np.append(average, coordinate)  # 附上此距離的座標

        K_meansNew = np.append(K_meansNew, KmeansRGB函式.最小距離座標(average))
        #print(KmeansRGB函式.最小距離座標(average))
        average = np.array([])  # 此群的全部頻均距離，清空

    # print(K_meansNew.reshape(-1, 2))
    return K_meansNew.reshape(-1,2)
"""