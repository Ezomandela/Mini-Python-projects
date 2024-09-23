with open("ezra.txt","r") as f:
    story=f.read()
words=set()
start_word=-1
target_start="<"
target_end=">"
for i,char in enumerate(story):
    if char==target_start:
        start_word=i
    if char==target_end and start_word!=-1:
         word=story[start_word:i+1]
         words.add(word)
         start_word = -1
answer={}

for wo in words:
    answ=input("enter the word" + wo + "enter your :")
    answer[wo]=answ

for wo in words:
    print(answer[wo])
    story=story.replace(wo,answer[wo])
print(story)









