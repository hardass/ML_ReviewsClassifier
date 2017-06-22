import sys  
import string  
#import collections  
  
if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:  
 print("usage: uniqueword filename_1 filename_2 ... filename_n")  
 sys.exit()  
else:  
 words = {}   
 # words = collections.defaultdict(int)  
 strip = string.whitespace + string.punctuation + string.digits + "\"'"  
 for filename in sys.argv[1:]:  
  for line in open(filename):  
    for word in line.split():  
    word = word.strip(strip)  
    if len(word) >= 2:  
     words[word] = words.get(word, 0) + 1  
     # words[word] += 1  
 for word in sorted(words):  
  print("'{0}' occurs {1} times".format(word,words[word])) 