f = open('hello.txt', 'w')
f.write('welcome to Python\n')
lines=["aaaa\n", "1111\n" , "222222\n", "# 発音メモ \nAppendのことをエッペンドって先生は言ってる。。"]

f.writelines(lines)
f.close()

# 発音メモ
# Appendのことをエッペンドって先生は言ってる。。