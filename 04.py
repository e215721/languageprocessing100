text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
num = [1,5,6,7,8,9,15,16,19]
text1 = text.replace(".","")
#print(text1)
dic = {}
text2 = text1.split()
for i, v in enumerate(text2):
    if i + 1 in num:
        dic[v[0]] = i + 1
    else:
        dic[v[:2]] = i + 1
print(dic)
