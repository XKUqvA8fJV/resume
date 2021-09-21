實作 K-means 演算法

將所有像素點的 RGB 數值當作是 ( x, y, z ) 立體座標。與其他像素點使用歐幾里得距離公式計算距離。輸入想要分的群數 K 後，依據 K-means 演算法作法進行分群。

輸入檔名為：input.jpg
為jpg屬性圖片

輸出檔案為 "i".jpg 其中 "i" 為手動輸入希望有多少個分群 ( K值 )。 輸出圖片內容為分群後的結果，每個分群顏色為各群顏色取平均。最後得到使用K種顏色上色的結果。

展示：
原圖

![input](https://user-images.githubusercontent.com/42996962/134174529-4884af84-1563-4f87-95fd-cd8d421ec08f.jpg)

分群各為 1 ~ 9 的輸出動圖：

![Webp net-gifmaker](https://user-images.githubusercontent.com/42996962/134174952-aaf3864b-f1e1-4759-a7e7-715e04128dbe.gif)

分群為 1 的輸出圖：

![1](https://user-images.githubusercontent.com/42996962/134175047-84392113-932f-4b59-9706-55f0dc94242b.jpg)

分群為 2 的輸出圖：

![2](https://user-images.githubusercontent.com/42996962/134175065-57b5405d-2280-4e6c-991a-8399495de227.jpg)

分群為 3 的輸出圖：

![3](https://user-images.githubusercontent.com/42996962/134175074-572235f1-23b6-4bcb-a7ac-352a5b17c0d9.jpg)

分群為 4 的輸出圖：

![4](https://user-images.githubusercontent.com/42996962/134175088-89a8381b-73f1-44e0-befe-4def9eeeb9b5.jpg)

分群為 5 的輸出圖：

![5](https://user-images.githubusercontent.com/42996962/134175104-23ab4249-28cd-4504-a79e-cad7edc702de.jpg)

分群為 6 的輸出圖：

![6](https://user-images.githubusercontent.com/42996962/134175119-0b080d76-5437-49d6-a672-2b28ba4f89ea.jpg)

分群為 7 的輸出圖：

![7](https://user-images.githubusercontent.com/42996962/134175149-932aad51-35dc-4fe5-b6a8-06fdf6169725.jpg)

分群為 8 的輸出圖：

![8](https://user-images.githubusercontent.com/42996962/134175162-ac47ee1b-92d1-41b6-b942-ac6c2b45618f.jpg)

分群為 9 的輸出圖：

![9](https://user-images.githubusercontent.com/42996962/134175174-e14b2d73-d206-4631-b82a-10c65fa0ad7a.jpg)


