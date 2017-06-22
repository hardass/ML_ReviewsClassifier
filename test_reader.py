import sys
import string
#import collections

if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
    print("usage: uniqueword filename_1 filename_2 ... filename_n")
    sys.exit()
else:
    words = {}
    i = 0
    # words = collections.defaultdict(int)
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    for filename in sys.argv[1:]:
        post_input = []
        for line in open(filename):
            post_line = []
            for word in line.split():
                word = word.strip(strip)
                if len(word) >= 2:
                    if words.get(word, 0) == 0:
                        words[word] = i
                        i = i + 1
                    post_line.append(words[word])
            post_input.append(post_line)
    for line in post_input:
        print(line)
    # for word in sorted(words):
<<<<<<< HEAD
        # print("'{0}' unique number is {1}".format(word, words[word]))
=======
        # print("'{0}' unique number is {1}".format(word, words[word]))
>>>>>>> 65be23a1e640bbb5921e5bdbb80ce31101096da8
