
### 問題(Debug)

あなたは分析ツールの保守を任されました。\
このツールは「商品のカテゴリごとの平均価格と、最も高価な商品」を求めることを目的としています。\
※不正な価格を持つ商品は、統計から除外してください。

しかし、コードには複数のバグが存在し、正しく動作しません。

以下のファイル群を修正して、指定された出力が得られるようにしてください。

```
    Q2
    ├── main.py
    ├── analysis/statistics.py
    ├── utils/formatter.py
```

### 使用データ
- data/product_data.py
  - 編集不可

### 実行方法:
```
python main.py
```

### 想定出力:
```
    Category Averages:
    Stationary: 675.0
    Electronics: 50250.0

    Most Expensive Product:
    Laptop (Electronics) - 98000円
```

END