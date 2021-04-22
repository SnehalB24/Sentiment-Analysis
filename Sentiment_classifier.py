punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("Positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(parameter):
    c = 0
    parameter = strip_punctuation(parameter.lower())
    parameter=parameter.split()
    for i in parameter:
        for y in positive_words:
            if i == y:
                c+=1
    return c

negative_words = []
with open("Negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(parameter):
    c = 0
    parameter = strip_punctuation(parameter.lower())
    parameter=parameter.split()
    for i in parameter:
        for y in negative_words:
            if i == y:
                c+=1
    return c
def strip_punctuation(word):
    for i in punctuation_chars:
        word=word.replace(i,'')
    return word


word=open('Twitter_data.csv','r')
read=word.readlines()
num_retweet=[]
num_replies=[]
list_num_pos=[]
list_num_neg=[]
list_net_score=[]

for line in read[1:]:
    num_pos = get_pos(line)
    num_neg = get_neg(line)
    list_num_pos.append(num_pos)
    list_num_neg.append(num_neg)
    read1=line.split('\n')
    ww=''.join(read1)
    read2=ww.split(',')
    x=read2[1]  
    x1=read2[2]
    num_retweet.append(int(x))
    num_replies.append(int(x1))
    net_score=num_pos-num_neg
    list_net_score.append(net_score)

outfile=open('resulting_data.csv','w')
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
i=0
for vv in num_retweet:
    row_string = '{},{},{},{},{}'.format(num_retweet[i], num_replies[i], list_num_pos[i], list_num_neg[i], list_net_score[i])
    outfile.write(row_string)
    outfile.write('\n')
    i=i+1


 
