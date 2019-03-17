import re
import numpy

fname = "Paragraph_3.txt"

num_lines = 0
num_words = 0
num_chars = 0
num_sents = 0 
avg_letter = 0
words = []
i = 0 
with open(fname, 'r') as f:
    for line in f:
        
        words = line.split(" ")
        words1 = line.split("'")
        words2 = line.split("-")
        awords = line.split()
        sent = line.split(".")
                  
        #print(str.rstrip(sent))
        
        num_words1 = (len(words1) -1) + (len(words2 ) -1)
        num_words  += len(words) + num_words1
        
        #print(avg_letter)

        for string in sent:
            if string:
                num_sents += 1
               

                #avg_sent = sum(string)/len(string)
    