## 第７回講義動画 <br>
[https://nuss.nagoya-u.ac.jp/s/3Rt8ZcwdjPCZxgZ](https://www.dropbox.com/scl/fi/2ji2x05j9grihazqdl9uq/0610_3-_-_.mp4?rlkey=jpvjjpzrbap6ia5i00cjs7e9a&dl=0)
## 第７回Q&A集
https://irradiated-pot-667.notion.site/7-Q-A-8b1443826c514dafbdec7f055e9b621f
## 各種プログラムの説明　<br>

** movie.py:**<br>
各温度で粒子配置の動画を作るプログラム
mp4形式が作れないときは，以下をインストール
```
brew install ffmpeg
```
**langevin_many.cpp:**<br>
自主課題6の主計算サンプルプログラム<br>

**many_particle.py:**<br>
自主課題６の作図サンプルプログラム<br>
４枚の粒子図を並べる．<br>
これを形成するためには，温度T=0.2,0.4,0.6,1.0の粒子の配置データが必要．<br>
粒子の配置データは**langevin_many.cpp**で生成(tempを手動で変える)．<br>

**md.cpp:**<br>
自主課題7の主計算サンプルプログラム<br>
平衡化はlangevinダイナミクス<br>
本計算は速度ベルレ法

**energy.py:**<br>
md.cppの結果の作図（力学的エネルギー等）
