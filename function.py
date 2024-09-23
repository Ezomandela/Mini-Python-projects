s = input("do you want encryption press 'E' or decryption 'D': ").lower()
arr=[]
ar=[]
e=len(s)
p = input("please enter the word:")
q = int(input("please add the number you want: "))
def pl(d, sec, arr1):
    for ch in range(sec):
        cha = ord(arr1[ch])
        cha -= q
        jo = chr(cha)
        ar.append(jo)
    a = "".join(ar)
    print(f"congradulation your original word is {a}")
def janny(p,q):
      e = len(p)
      for char in range(e):
        char = ord(p[char])
        char += q
        jok = chr(char)
        arr.append(jok)
      arr1 = "".join(arr)
      print(f"the encyyption word is {arr1}")
      sec = len(arr1)
      d = input("do you want to see decryption press'D': ").lower()
      if d == 'd':
          pl(d, sec, arr1)
      else:
          print("no way you are out of the domain ")
if s=='e':
    print(janny(p, q))
else:
    print("please first insert enryption before decryption")



