def ezra(cam):
  return len([l for l in set(cam.lower()) if cam.lower().count(l)>1])

print(ezra("ezraezra"))

