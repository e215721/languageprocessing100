text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
text1 = text.replace(",","")

lis = []
for x in text1.split():
    lis.append(x)
    print(len(x))
len_l = [len(y) for y in lis]
print(len_l)
print(text1.split())