2024.05/05

import matplotlib.pyplot as plt

x_values = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']
y_values = [100, 130, 80, 150, 140, 130]

plt.bar(x_values, y_values)
plt.plot()

plt.show()

10 ** 3は、10を3回かける意味
だからAnswerは1000になる。

3/2は1.5だけど
3//2は整数除数をしてくれるので小数点を切り捨てて１になる。

3.0 // 2.0  
は1.0とfloat型になる。

これだと比率を出してくれる
1/2みたいな感じで
data = 0.5
data.as_integer_ratio()

アルファベットの方が大きい
'111' < 'a'

lowercase letter の方が大きい
数字よりも
'111' < 'a'

string = input("文字列を入力してください：")
if string.isdecimal():
  print(string, "は数字です。")
elif string.isalpha:
  print(string, "は数字ではないです。文字")
else: 
  print("nothing")

  else ifの時はelif


ANDは&&
ORは||って感じ

def　関数名():
で関数の宣言ができる

否定の時
Reactなら！だったけどPythonはnotと記載する。

whileで途中で抜ける場合は
breakをおく

def func(arg1, arg2, arg3):
  print("argは”, arg1, arg2, arg3, "です。"）
func(1,2,3)みたいな感じで引数に値を入れたけど（位置引数）

以下のように引数を指定するときはキーワード引数という。
func(arg1="引数1", arg2="引数２", arg3="引数3")

Array, List
values = [1, 2, 3, 4]

for value in values:
    print("valueは", value, "value*valueは", value*value)
# ここはコメント

辞書オブジェクト
english_words = {"apple": "りんご", "orange": "みかん", "peach": "もも"}
print(english_words["orange"])
