"""
def NP加順序(img_arr):
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

def NP加判斷值(img_arrNew):
    #輸入NP加順序，輸出加一位元判斷分群。
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

def NP加堆疊(img_arrNew):
    #輸入NP加分群，輸出加一位元判斷堆疊。
    #輸出(R,G,B,像素順序,群分類,堆疊)初始設定
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

def 兩點距離(img_arrNew2,y,x,ky,kx):
    #(NP加分群，座標1y,座標1x,座標2ky,座標2kx)
    return ((img_arrNew2[y][x][0]-img_arrNew2[ky][kx][0])**2 + \
           (img_arrNew2[y][x][1]-img_arrNew2[ky][kx][1])**2 + \
           (img_arrNew2[y][x][2] - img_arrNew2[ky][kx][2]) ** 2)**(1/2)
    """
"""
def 向下(yold,xold):
    #向下移動傳入移動座標
    yold, xold = yold + 1, xold
    return yold, xold

def 向右(yold,xold):
    #向右移動傳入移動座標
    yold, xold = yold, xold+1
    return yold, xold

def 向上(yold,xold):
    #向上移動傳入移動座標
    yold, xold = yold -1, xold
    return yold, xold

def 向左(yold,xold):
    #向下移動傳入移動座標
    yold, xold = yold, xold-1
    return yold, xold

def 上色測試(img_arrNew,yold, xold):
    img_arrNew[yold][xold][0] = 100
    img_arrNew[yold][xold][1] = 100
    img_arrNew[yold][xold][2] = 100
    return img_arrNew

def 範圍掃描(img_arrNew,yold, xold):
    import DBSCAN函式
    for i in range(0, 4):
        # 向下
        yold, xold = DBSCAN函式.向下(yold, xold)
        DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
        # 向右
        if i == 0:
            yold, xold = DBSCAN函式.向右(yold, xold)
            DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
        else:
            for right in range(2 * i + 1):
                yold, xold = DBSCAN函式.向右(yold, xold)
                DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
        # 向上
        if i == 0:
            for up in range(2):
                yold, xold = DBSCAN函式.向上(yold, xold)
                DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
        else:
            for up in range(2 * i + 2):
                yold, xold = DBSCAN函式.向上(yold, xold)
                DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
        # 向左
        if i == 0:
            for up in range(2):
                yold, xold = DBSCAN函式.向左(yold, xold)
                DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
        else:
            for up in range(2 * i + 2):
                yold, xold = DBSCAN函式.向左(yold, xold)
                DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
        # 向下
        if i == 0:
            for up in range(2):
                yold, xold = DBSCAN函式.向下(yold, xold)
                DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
        else:
            for up in range(2 * i + 2):
                yold, xold = DBSCAN函式.向下(yold, xold)
                DBSCAN函式.是否有顏色(img_arrNew, yold, xold)

def 範圍掃描改(img_arrNew,yold, xold,RangeS=1):
    import DBSCAN函式
    height, width, RGB = img_arrNew.shape

    for i in range(0, RangeS):
        # 向下
        if yold + 1 < 0 or yold + 1 >= height or xold >= width or xold < 0:
            yold, xold = yold + 1, xold
        else:
            yold, xold = DBSCAN函式.向下(yold, xold)
            DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
            img_arrNew = DBSCAN函式.上色測試(img_arrNew, yold, xold)
        #print("yold,xold     ", yold, xold)
        # 向右
        if i == 0:
            if yold < 0 or yold >= height or xold + 1 >= width or xold + 1 < 0:
                yold, xold = yold, xold + 1
            else:
                yold, xold = DBSCAN函式.向右(yold, xold)
                DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
                img_arrNew = DBSCAN函式.上色測試(img_arrNew, yold, xold)
        else:
            for right in range(2 * i + 1):
                if yold < 0 or yold >= height or xold + 1 >= width or xold < 0:
                    yold, xold = yold, xold + 1
                else:
                    yold, xold = DBSCAN函式.向右(yold, xold)
                    DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
                    img_arrNew = DBSCAN函式.上色測試(img_arrNew, yold, xold)
        #print("yold,xold     ", yold, xold)
        # 向上
        if i == 0:
            for up in range(2):
                if yold - 1 < 0 or yold - 1 >= height or xold >= width or xold < 0:
                    yold, xold = yold - 1, xold
                else:
                    yold, xold = DBSCAN函式.向上(yold, xold)
                    DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
                    img_arrNew = DBSCAN函式.上色測試(img_arrNew, yold, xold)
        else:
            for up in range(2 * i + 2):
                if yold - 1 < 0 or yold - 1 >= height or xold >= width or xold < 0:
                    yold, xold = yold - 1, xold
                else:
                    yold, xold = DBSCAN函式.向上(yold, xold)
                    DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
                    img_arrNew = DBSCAN函式.上色測試(img_arrNew, yold, xold)
        #print("yold,xold     ", yold, xold)
        # 向左
        if i == 0:
            for up in range(2):
                if yold < 0 or yold >= height or xold - 1 >= width or xold - 1 < 0:
                    yold, xold = yold, xold - 1
                else:
                    yold, xold = DBSCAN函式.向左(yold, xold)
                    DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
                    img_arrNew = DBSCAN函式.上色測試(img_arrNew, yold, xold)
        else:
            for up in range(2 * i + 2):
                if yold < 0 or yold >= height or xold - 1 >= width or xold - 1 < 0:
                    yold, xold = yold, xold - 1
                else:
                    yold, xold = DBSCAN函式.向左(yold, xold)
                    DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
                    img_arrNew = DBSCAN函式.上色測試(img_arrNew, yold, xold)
        #print("yold,xold     ", yold, xold)
        # 向下
        if i == 0:
            for up in range(2):
                if yold + 1 < 0 or yold + 1 >= height or xold >= width or xold < 0:
                    yold, xold = yold + 1, xold
                else:
                    yold, xold = DBSCAN函式.向下(yold, xold)
                    DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
                    img_arrNew = DBSCAN函式.上色測試(img_arrNew, yold, xold)
        else:
            for up in range(2 * i + 2):
                if yold + 1 < 0 or yold + 1 >= height or xold >= width or xold < 0:
                    yold, xold = yold + 1, xold
                else:
                    yold, xold = DBSCAN函式.向下(yold, xold)
                    DBSCAN函式.是否有顏色(img_arrNew, yold, xold)
                    img_arrNew = DBSCAN函式.上色測試(img_arrNew, yold, xold)
    return img_arrNew
"""
def 是否有顏色(img_arrNew,y,x,ranges = 200):
    #該點是否有顏色
    #rnges多少以下到表有顏色，0暗 255白透
    if img_arrNew[y][x][0] < ranges or img_arrNew[y][x][1] < ranges or img_arrNew[y][x][2] < ranges:
        return 1
    else:
        return 0

def NP加判斷值2(img_arrNew):

    import numpy as np

    img_arrNew = np.reshape(img_arrNew, (-1, 2))
    heightLen, widthLen = img_arrNew.shape
    img_arrNew2 = np.zeros(shape=(heightLen, widthLen + 2))
    for y in range(heightLen):
        for x in range(widthLen):
            img_arrNew2[y][x] = img_arrNew[y][x]
    return img_arrNew2

def 有像素的位址加入新陣列(img_arr):
    #將有像素的座標位址加入到新陣列裡面
    import numpy as np
    import DBSCAN函式
    height, width, RGB = img_arr.shape
    img_arrNew = np.array([])
    for y in range(height):
        for x in range(width):
            if DBSCAN函式.是否有顏色(img_arr, y, x):
                #print("y x     ", y, x)
                img_arrNew = np.append(img_arrNew, y)
                img_arrNew = np.append(img_arrNew, x)
    return img_arrNew

def 兩點距離(img_arrNew2,y,y2):
    return ((img_arrNew2[y][0] - img_arrNew2[y2][0]) ** 2 +
            (img_arrNew2[y][1] - img_arrNew2[y2][1]) ** 2) ** (1 / 2)
