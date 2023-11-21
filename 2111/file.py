file = open("text.txt", "w")
file.write("Hello World \n")
file.write("This is our new text file \n")
file.write("and this is another line \n")

file.close()

file = open("text.txt", "r")

# ファイルの全内容を出力
print(file.read())

# ファイル読み取り位置をファイルの始めに戻す
file.seek(0)

# ファイルから最初の5文字を読み込む
print(file.read(5))

# 各ラインを表示
print(file.readlines())

file.close()



