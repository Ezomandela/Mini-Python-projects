def ezra(facing,turns):
   dir=["N","NE","E","SE","S","SW","W","NW"]
   turns=turns//45
   start=dir.index(facing)
   end=(start + turns) % len(dir)
   return dir[end]
print(ezra("N",500))



