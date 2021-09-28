實作 DBSCAN 演算法

將非白色所有像素點的 ( x, y ) 座標。與其他像素點使用歐幾里得距離公式計算距離。輸入 DBSCAN演算法需要的參數：像素點合併容許最遠距離、每群構成群的最小數量。依據 DBSCAN 演算法進行分群。

輸入檔名為：input.bmp
為jpg屬性圖片

輸出檔名為： output_D"i"_N"j".jpg 其中 "i" 為輸入的容許最遠距離、 "j" 為輸入的集群最小構成數量
輸出圖片內容為分群後的結果，每個群使用不同顏色上色。離群座標不標示。
原圖(圖案已等比放大，原始圖大小為 371 x 268 )

![99999](https://user-images.githubusercontent.com/42996962/135081305-459e5fec-37ca-4fae-93ec-2edc39ca0a5c.png)

容許最遠距離 i = 1 集群最小構成數量 j = 5

![5555](https://user-images.githubusercontent.com/42996962/135081139-c6841499-ff33-438f-861c-b79f60410369.png)

容許最遠距離 i = 2
集群最小構成數量 j = 5

![6666](https://user-images.githubusercontent.com/42996962/135081161-e4fbb567-d4a2-4e41-8073-4ca07ff81591.jpg)

容許最遠距離 i = 3
集群最小構成數量 j = 5

![777777](https://user-images.githubusercontent.com/42996962/135081170-1621150c-8adc-417a-b259-04f3dd589a59.png)

