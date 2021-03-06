使用爬山演算法解八皇后問題

八皇后問題指的是一種特殊的棋盤擺法，每一行、每一列同一時間只能有一個棋子。同時每條橫線上也只能有一個棋子。

爬山演算法為一種優化演算法，如同字面上的 "爬山"，它藉由每一次觀察它目前可到路徑哪一條路線可以爬到最高海拔，來試圖爬到最高的山頂去。

而在八皇后問題應用方式為，隨機丟入八顆棋子，並且試圖移動每一個棋子到北、東北、東、東南、南、西南、西、西北，八個方位移動一格。如果移動後棋子與棋子間存在在同一行、列、斜線上的數量減少。就當作正確的方向移動棋子。直到最後八顆棋子都移到正確位置，衝突數為 0 為止。

如果發現無法優化至衝突數為 0。就重新隨機丟入八顆棋子開始優化。

輸入數值 queen：
意義為產生 queen 皇后的解

輸出內容：
為 queen 皇后的其中一組解

展示：

queen = 8

![8](https://user-images.githubusercontent.com/42996962/136897778-8c0aad0c-cfb1-4057-8501-f3ff89bdd0d5.PNG)

queen = 9

![9](https://user-images.githubusercontent.com/42996962/136897807-922113ed-b481-4fc9-bb97-715513132f24.PNG)

queen = 10

![10](https://user-images.githubusercontent.com/42996962/136897828-f916adbd-03b7-449d-8b8b-973016fecd5f.PNG)
