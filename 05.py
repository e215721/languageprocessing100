text = "I am an NLPer"
def n_gram(text, n):   #関数n_gramを定義する。引数として"text" and "n"n-gramのn
    res = []           #空のリストresを作成する。
    if len(text) < n:  #textの長さがnより小さいの場合空リストを返す。
        return res
    for i in range(len(text) - n + 1):  #'i'を'0'からtextの長さ-n+1までの範囲で繰り返し、代入する。
        res.append(text[i:i+n])         #textのi番目からi+n番目までの要素をスライスしてリストに代入する。
    return res                          #代入されリストを返す。
print('文字bi-gram:', n_gram(text, 2))
print('単語bi-gram:', n_gram(text.split(), 2))