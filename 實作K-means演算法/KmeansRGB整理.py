import numpy as np
from PIL import ImageColor,Image
import KmeansRGB函式


#1到10群
for kNum in range(1,10):

    img = Image.open("20190415211416_31.jpg")  # 照片位址
    img_arr = np.array(img)  # Image轉numpy

    img_arrNew = KmeansRGB函式.NP加座標(img_arr) #(R,G,B,像素順序)初始設定

    img_arrNew2 =  KmeansRGB函式.NP加分群(img_arrNew) #(R,G,B,像素順序,群分類)初始設定

    height,width,RGB = img_arrNew2.shape

    K_means = KmeansRGB函式.K群(kNum,img_arrNew2) #總共幾分群

    img_arrNew2 = KmeansRGB函式.各K群分類改(K_means,img_arrNew2) #各K群分類
    print("各K群分類改完畢")
    CenK = K_means #現在中心點放在空陣列
    time = 0
    while 1:
        K_means = KmeansRGB函式.各群中心座標改(K_means,img_arrNew2)
        print("各群中心座標改完畢")
        img_arrNew2 = KmeansRGB函式.各K群分類改(K_means, img_arrNew2)
        print("各K群分類改完畢")
        #KmeansRGB函式.顏色更改及展示(K_means, img_arrNew2)
        #print("顏色更改及展示完畢")
        time += 1
        print("完畢次數: ",time)
        print("--------------------------")
        if (CenK == K_means).all(): #比對上次和現在中心點是否改變
            break
        else:
            CenK = K_means

    #儲存
    img_New = KmeansRGB函式.顏色更改及展示(K_means, img_arrNew2)
    #img_New.show()
    img_New.save("C:/Users/home/Downloads/Python39/演算法/KmeansPict/"+str(len(K_means))+".jpg")
