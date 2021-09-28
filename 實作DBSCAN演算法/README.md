實作 DBSCAN 演算法

將非白色所有像素點的 ( x, y ) 座標。與其他像素點使用歐幾里得距離公式計算距離。輸入 DBSCAN演算法需要的參數：像素點合併容許最遠距離、每群構成群的最小數量。依據 DBSCAN 演算法進行分群。

輸入檔名為：input.bmp
為jpg屬性圖片

輸出檔名為： output_D"i"_N"j".jpg 其中 "i" 為輸入的容許最遠距離、 "j" 為輸入的集群最小構成數量
輸出圖片內容為分群後的結果，每個群使用不同顏色上色。離群座標不標示。
原圖

![0](https://user-images.githubusercontent.com/42996962/135078104-47c175ee-43db-4931-9e50-a950f192420e.jpg)

容許最遠距離 i = 1 集群最小構成數量 j = 5

![output_D1_N5](https://user-images.githubusercontent.com/42996962/135078288-1a8f8401-7ca0-4bfa-a9d1-b81b7839e30b.jpg)

容許最遠距離 i = 2
集群最小構成數量 j = 5

![output_D2_N5 jpg](https://user-images.githubusercontent.com/42996962/135078323-dac195b8-8ff2-4b03-904b-66c630ae9ddd.jpg)

容許最遠距離 i = 3
集群最小構成數量 j = 5

![output_D3_N5 jpg](https://user-images.githubusercontent.com/42996962/135078345-5d109cf0-6665-43f6-9fb4-f5da80372e5c.jpg)
