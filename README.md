# futarin-led  
## git clone  
1.リポジトリをクローンする  
```shell
git clone https://github.com/futaringoto/futarin-led.git
```
## ライブラリのインストール  
```shell
pip install rpi_ws281x
```
## 実行方法  
```shell
cd futarin_led
sudo python futarin_led
```
また、コマンドの最後に -c　をつけることで^cで停止した時、光を消灯できます。  
## 機能　　
### cycle  
光が回転します。  


・wait_ms=x  
xに任意の数字を入力し、一周する時間(ms)を定められます  
  
### turn_on  
点灯します 
  
・wait_ms=x  
xに任意の実数を入力し、一周する時間(ms)を定められます。  
  
・iterations=ｘ  
turn_on関数に関しては１とします。  
  
### flash  
点滅します。  
  
・wait_ms=x  
xに任意の実数を入力し、一周する時間(ms)を定められます。 
・iterations=x
xに任意の実数を入力し、点滅の回数を定められます。
