str1="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
str2="NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
message="ezra samson"
dic_tio={ str1[i]:str2[i] for i in range(len(str1))}
# you can use this code olso
#ez=str.maketrans(str1,str2)
ez=str.maketrans(dic_tio)
print(ez)
e=message.translate(ez)
print(e)



