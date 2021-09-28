import numpy as np
from PIL import ImageColor,Image
import DBSCAN函式

L = 3 #距離、半徑
Num = 5 #距離、半徑幾個容許值
for L in range(1,L+1):
    img = Image.open("input.jpg")  # 照片位址
    img_arr = np.array(img)  # Image轉numpy
    img_arrNew = DBSCAN函式.有像素的位址加入新陣列(img_arr)
    img_arrNew2 = DBSCAN函式.NP加判斷值2(img_arrNew)
    print("1")
    #L = 2 #距離、半徑
    #Num = 5 #距離、半徑幾個容許值
    #半徑 半徑內幾個點
    yNum,xNum = img_arrNew2.shape

    img_arrNew3 = np.array([])
    K = 1
    for y in range(yNum):
        if img_arrNew2[y][3] == 0: #判斷此點是否有掃描過
            img_arrNew2[y][3] = 1 #此點正在掃描
            img_arrNew3 = np.array([])
            for y2 in range(yNum): #與其他第二點距離
                if  DBSCAN函式.兩點距離(img_arrNew2,y,y2) <= L:
                    img_arrNew3= np.append(img_arrNew3,y2)
            if len(img_arrNew3) < Num : #少於指定數量
                img_arrNew2[y][2] =  -1 #此點上-1
            else:
                for y2 in range(len(img_arrNew3)): #大於指定數量，此陣列全部上分類
                    img_arrNew2 [int(img_arrNew3[y2])][2] =  K

                #print("img_arrNew3TEST  ",img_arrNew3)
                flag = 1 #持續掃瞄有沒有此點的分類
                while flag:
                    flag = 0
                    for y2 in range(yNum): #判斷之後K點其他範圍掃描
                        if img_arrNew2[y2][2] == K and img_arrNew2[y2][3] == 0:
                            flag = 1
                            img_arrNew2[y2][3] = 1 #此點正在掃描
                            img_arrNew3 = np.array([])
                            for y3 in range(yNum):  # 與其他第二點距離
                                if DBSCAN函式.兩點距離(img_arrNew2, y2, y3) <= L:
                                    img_arrNew3 = np.append(img_arrNew3, y3)
                            #print("img_arrNew3TEST2   ",img_arrNew3)

                            if len(img_arrNew3) >= Num:
                                for y2 in range(len(img_arrNew3)):  # 此陣列全部上分類
                                    img_arrNew2[int(img_arrNew3[y2])][2] = K
                    flag = 1 if flag == 1 else 0
                K += 1
                print(K)


    #print("img_arrNew3   ",img_arrNew3)
    #print("img_arrNew2   ",img_arrNew2)


    #建立放置新圖的空陣列
    Ly,Lx,Lb = img_arr.shape
    img_arrNew4 = np.zeros([Ly,Lx,Lb])
    img_arrNew4 = np.where(img_arrNew4,0,255)

    #讀取img_arrNew2大小
    Ly2,Lx2 = img_arrNew2.shape

    K = K-1 #減掉多算的一次
    print(K)
    for LK in range(K):
        LK += 1
        RGB = np.random.randint(0, 256, [3]) #上色
        for y in range(Ly2):
            if img_arrNew2[y][2] == LK:
                y2,x2 = int(img_arrNew2[y][0]),int(img_arrNew2[y][1])
                img_arrNew4[y2][x2][0] =  RGB[0]
                img_arrNew4[y2][x2][1] =  RGB[1]
                img_arrNew4[y2][x2][2] =  RGB[2]
        print(LK)

    img = Image.fromarray(np.uint8(img_arrNew4))  # numpy轉Image ，uint8轉編碼
    img = img.convert("RGB")  # 轉回RGB
    #img.show()
    img.save("C:/Users/home/Downloads/Python39/演算法/DBSCANPict/output_D" + str(L) +"_N"+ str(Num)+".jpg")









