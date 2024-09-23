def permute(data, i, length):

    print(data,"data after permutation")
    if i==length:
        print(i,length,"equal")
        print(''.join(data))
    else:
        for j in range(i,length):
            print(j,"this is j")
            print(i,"this is i")
            print(data[i],"before")
            print(data[j],"before")
            data[i], data[j] = data[j], data[i]
            print(data[i],"after")
            print((data[j],"after"))
            permute(data, i+1, length)
            print(i,"afer permutation ")
            print(j,"after permtaion")
            print(data,"data of the array")
            print("permtuation")
            print(data[i]," middle")
            print(data[j]," middle")
            print(i,"middle")
            print(j,"middle")
            data[i], data[j] = data[j], data[i]
            print(data[i],"final")
            print((data[j], "final"))
            print(i,"final i")
            print(j,"final j")


string = "ABCd"
n = len(string)
data = list(string)
permute(data, 0, n)









