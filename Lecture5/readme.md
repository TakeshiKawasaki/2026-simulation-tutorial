## 第5回講義動画（NUSSリンク） <bf>
[https://nuss.nagoya-u.ac.jp/s/w5LaEG3ARL52Lyc](https://www.dropbox.com/scl/fi/nxfj84hoaggu2vaoo10mg/0520_3-_-5.mp4?rlkey=8l9081longtsw7a5v7bk2jthw&dl=0)
  
## 第５回アンケートQ&A集 <bf>
https://irradiated-pot-667.notion.site/6-Q-A-37c976766d334f43b73eb0ce0f9b94a6?pvs=4

## コードについての補足：
#### BM.h:
Box Muller法による分散1の正規乱数 `gaussian rand()` を生成する関数が格納されたヘッダファイル．次のlangevin.cppの冒頭で宣言している．
`#include "BM.h"`
#### langevin.cpp: 
ランジュバン方程式を解くプログラム．デフォルトでは時刻10までの軌跡を1000アンサンブル生成する．パラメータtempは冒頭に定義．適宜変えること．
以下の作図プログラムを用いる際は，`temp=1.0,0.1,0,0.01` の計算を行い軌道・速度データを生成する必要がある．

#### analyze.cpp: 
平均二乗変位と速度相関関数の解析プログラム．langevin.cppとtempのパラメータを揃える必要がある点に注意．以下の作図プログラムをそのまま使う場合は，，`temp=1.0,0.1,0,0.01`  の解析を行う必要がある．

#### msd.py，corr_vel.py: 
作図プログラム．`temp=1.0,0.1,0,0.01`  の解析結果(平均二乗変位と速度相関関数)を用意する必要がある．

