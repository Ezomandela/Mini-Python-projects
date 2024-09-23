def revrese(str):
    stri=[s for s in str.split() ]
    stri=" ".join([l[::-1] if len(l)>5 else l for l in stri])
    print(stri)
revrese(" this is sparta ")