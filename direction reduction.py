def dir_reduc(arr):
    change=True
    arr=" ".join(arr)
    while change:
        change=False
        old=arr
        arr=arr.replace("NORTH SOUTH", "")
        arr=arr.replace("EAST WEST", "")
        arr=arr.replace("SOUTH NORTH", "")
        arr=arr.replace("WEST EAST", "")
        arr = arr.replace("  ", " ")
        if arr.startswith(" "):
              arr=arr[1:]
        if arr.endswith(" "):
              arr=arr[:-1]
        if old==arr:
            if arr=='':
                arr=[]
                return arr
            else: 
                return arr.split(" ")
        else:
            change = True

print(dir_reduc(['']))