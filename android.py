def order(sentence):
  ezra=sentence.split(" ")
  num=[]
  for i in range(0, len(ezra) +1):
       for j in ezra:
              if str(i) in j:
                num.append(j)
  return " ".join(num)

print(order("Thi1s is2 3a"))

