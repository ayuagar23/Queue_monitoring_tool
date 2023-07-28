import re
import os

with open("rabbitmq.txt",'w+') as myfile:
    myfile.truncate(0)


os.system('docker exec -ti rabbitmq rabbitmqctl list_queues > rabbitmq.txt')

mylines = []
mylines1 = []
with open ('rabbitmq.txt', 'rt') as myfile:
    for myline in myfile:
       mylines.append(myline)  
       if myline == 'name\tmessages\n':
           mylines.clear()
        

words=[]
for myline in mylines:
    word = re.split('_',myline)
    words.append(word)




for word in words:
    for i in range (len(word)):
        if word[i] >='0' and word[i]<= '9':
            if len(word[i])==1:
                word[i] = 'n'
            else:
                word[i] ='n'+word[i][1:]



for i in range (len(words)):
    words[i]='_'.join(words[i])



mylines =words
words= []
for myline in mylines:
    word = re.split('-',myline)
    words.append(word)


for word in words:
    for i in range (len(word)):
        if word[i] >='0' and word[i]<= '9':
            word[i]='n'



for i in range (len(words)):
    words[i]='-'.join(words[i])



map = {}
new_words=[]
for word in (words):
    new_word= re.split('\t',word)
    if(len(new_word[len(new_word)-1]) > 1):
        length = len(new_word[len(new_word)-1])
        new_word[len(new_word) - 1] = new_word[len(new_word)-1].rstrip(new_word[len(new_word)-1][-1])
    if map.get(new_word[0]):
        map[new_word[0]] = str(int(map[new_word[0]])+int(new_word[len(new_word)-1]))
    else:
        map[new_word[0]]= new_word[len(new_word)-1]

    new_words.append(new_word[0])


print("\nQueues with non-zero messages : \n")

for j in map.keys():
    if int(map[j])>0:
        print(j + " : " + str(map[j]))


dict = {}
for wd in new_words:
    if dict.get(wd):
        dict[wd]=dict[wd]+1
    else:
        dict[wd]= 1



file1 = open('output.txt', 'w')

for i in dict :
    val = str(i)
    val1 = str(dict[i])
    st = val + " , " + val1+"\n"
    file1.write(st)



file1.close()
myfile.close()
