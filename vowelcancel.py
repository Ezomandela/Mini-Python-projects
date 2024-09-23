def disemvowel(string_):
    vo = "aeiou"
    for i in vo:
        string_ = string_.replace(i, "")
        string_=string_.replace(i.upper(),"")
    return string_
print(disemvowel("This website is for losers LOL!"))
print(disemvowel("No offense but,\nYour writing is among the worst I've ever read"))
print(disemvowel("What are you, a communist?"))