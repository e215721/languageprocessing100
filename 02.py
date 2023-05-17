text1 = "パトカー"
text2 = "タクシー"
#text3 = (text1+text2)[0::4]
#text4 = (text1+text2)[1::4]
#text5 = (text1+text2)[2::4]
#text6 = (text1+text2)[3::4]
#print(text3+text4+text5+text6)
text3 = ""
for i in range(0,4):
    text3 += (text1+text2)[i::4]
print(text3)