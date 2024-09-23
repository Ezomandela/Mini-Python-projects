def longest(s1,s2):
   if int(len(s1)) >= int(len(s2)):
      ezra = set(s1)
      sam = "".join(list(ezra))
      ez ="".join(sorted(sam))
      return ez
   else:
     ezra = set(s1)
     sam = "".join(list(ezra))
     ez = "".join(sorted(sam))
     return ez


longest("xyaabbbccccdefwwcdz", "xxxxyyyyabklmopq")

