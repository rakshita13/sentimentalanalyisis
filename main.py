# cleaning text steps
# read data from text file,convert all letters into lower case and remove the punctuations
from collections import Counter
import string
text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()
# aketrans function,takes 3 parameter strings,str1=list of characters need to be replaced,str2=list of characters with
#  ich str1 characters are getting replaced,str3=list of character that need to be deleted
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
# okenizattion=breaking sentence into different words and storing them in list
tokenized_words = cleaned_text.split()
import matplotlib.pyplot as plt
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split
emotion_list = []
# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("/n",'r').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()