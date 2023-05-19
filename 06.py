def n_gram(text, n):   #関数n_gramを定義する。引数として"text" and "n"n-gramのn
    res = []           #空のリストresを作成する。
    if len(text) < n:  #textの長さがnより小さいの場合空リストを返す。
        return res
    for i in range(len(text) - n + 1):  #'i'を'0'からtextの長さ-n+1までの範囲で繰り返し、代入する。
        res.append(text[i:i+n])         #textのi番目からi+n番目までの要素をスライスしてリストに代入する。
    return res                          #代入されリストを返す。

text1 = "paraparaparadise"
text2 = "paragraph"
X = set(n_gram(text1,2))    #set型：重複する要素が除外されて生成される。
Y = set(n_gram(text2, 2))
print('X: ', X)
print('Y: ', Y)
print('和集合: ', X | Y)
print('積集合: ', X & Y)
print('差集合: ', X - Y)
print("'se'がXに含まれるか？: ", 'se' in X)
print("'se'がYに含まれるか？: ", 'se' in Y)