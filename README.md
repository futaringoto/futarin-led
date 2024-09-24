# furtarin-led
## ディレクトリ構成
```shell
futarin_led/
├app/
  └futarin_led.py
  └main.py
├README.md
├pyproject.toml
├uv.lock
```
## git clone  
1.リポジトリをクローンする  
```shell
git clone https://github.com/futaringoto/futarin-led.git
```
## ライブラリのインストール  
これらのライブラリを使用します。また、仮想環境を必要とします。  
rpi_ws281x->https://github.com/rpi-ws281x/rpi-ws281x-python.git  
flask->https://github.com/pallets/flask  
uv->https://docs.astral.sh/uv/#getting-started  

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
uv add rpi_ws281x
uv add Flask
```
## 実行方法  
```shell
cd futarin_led
uvpath=$(which uv)  
sudo ${uvpath} run app/main.py  
```
  
# futarin_led.py  
このコードは光り方の関数を記述しています。  
## 関数の意味
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

# main.py  
flaskを利用しサーバーを立てています。
## 各エンドポイントの説明
## wifi/  
### wifi/high  
Wifi接続が強い時。  
青点灯  
### wifi/middle  
wifi接続が中程度の時  
黄点灯  
### wifi/low  
wifi接続が弱い時
橙点灯
### wifi/disconnect 
wifi未接続時
赤点灯
## audio/    
### audio/listening  
聞き取り中
青点滅
### audio/thinking  
処理中
青回転
### audio/res-success  
応答成功
青点灯
### audio/res-fail  
応答失敗
赤点灯

