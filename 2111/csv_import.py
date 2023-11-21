import csv
# csvモジュールをインポートします。これによりCSVファイルを読み書きするための便利な機能にアクセスできます。

line_count = 0
# 行数をカウントするための変数`line_count`を0で初期化します。

with open('test.csv') as csv_file:
    # 'test.csv'という名前のCSVファイルを開き、`csv_file`という変数に関連付けます。
    csv_reader = csv.reader(csv_file, delimiter=',')
    # csv_fileを読み込むためのCSVリーダーオブジェクトを作成します。区切り文字としてカンマ（`,`）を指定します。

    for row in csv_reader:
        # CSVファイルを1行ずつ読み込み、各行を`行`という変数でループ処理します。
        if line_count == 0:
            # もしこれが最初の行（ヘッダー行）ならば以下を実行します。
            print(f'Column names are {", ".join(row)}')
            # ヘッダー行に含まれる列名を取得して出力します。列名はカンマで結合されています。
            line_count += 1
        else:
            # それが最初の行（ヘッダー行）ではないならば以下を実行します。
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            # それぞれの行から第一列、第二列、第三列の値を取り出して、整形された文字列を出力します。この例では、各行は個人が所属している部門と生まれた年を示しています。
            line_count += 1

print(f'Processed {line_count} lines.')
# 処理した行数を出力します。