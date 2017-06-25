import string

def Preparedata (path_train, path_dev, max):
	# dict of words has elements [frequecy, [classes of each sentences], varience]
	words = {}
	total_words = 1.0

	strip = string.whitespace + string.punctuation + string.digits + "\"'"

	content = []
	x_train = []
	y_train = []
	x_dev = []
	y_dev = []

	for line in open(path_train):
		post_line = []
		rank = int(line.split(' ', 1)[0])
		y_train.append(rank)
		for word in line.split():
			word = word.strip(strip)
			if len(word) >= 2:
				if words.get(word) == None:
					words[word] = [1,[rank,]]
				else:
					t = words.get(word)
					t[0] = t[0] + 1
					t[1].append(rank)
					words[word] = t
				total_words = total_words + 1
				post_line.append(word)
		content.append(post_line)

	# find overall rank expectation
	overall_rank_exp = 0.0
	for i in range(len(y_train)):
		overall_rank_exp = overall_rank_exp + y_train[i]
	overall_rank_exp = overall_rank_exp / len(y_train)

	# print(overall_rank_exp)
	
	# update varience of each word
	for k,v in words.items():
		sum_ranks = 0
		for i in range(len(v[1])):
			sum_ranks = sum_ranks + v[1][i]
		word_exp = sum_ranks / float(len(v[1]))
		word_var = (word_exp - overall_rank_exp) ** 2
		v.append(word_var)
		words[k] = v

	# print(total_words)

	# get a frequency dict
	dict_words_validation = {}
	for k,v in words.items():
		# dict_words_validation[k] = v[0]/total_words
		dict_words_validation[k] = v[2]*v[0]/total_words

	# sort frequency dict into list
	sortlist_words_validation = sorted(dict_words_validation.iteritems(), key=lambda d:d[1], reverse = True)
	# for i in range (0,100):
	# 	print(sortlist_words_validation[i])

	# build sorted dict according to frequency
	i = 0
	sortdict_words_validation = {}
	for v in sortlist_words_validation:
		sortdict_words_validation[v[0]] = i
		i = i+1
	# print(sortdict_words_validation)

	# generate x_train
	for line in content:
		post_line = []
		for word in line:
			if sortdict_words_validation.get(word) != None and sortdict_words_validation[word] < max:
				post_line.append(sortdict_words_validation[word])
		x_train.append(post_line)

	#generate y_train
	for line in open(path_dev):
		post_line = []
		y_dev.append(int(line.split(' ', 1)[0]))
		for word in line.split():
			word = word.strip(strip)
			if sortdict_words_validation.get(word) != None and sortdict_words_validation[word] < max:
				post_line.append(sortdict_words_validation[word])
		x_dev.append(post_line)

	# adjust 5 classes into 2
	# x_train, y_train = Class5to2(x_train, y_train)
	# x_dev, y_dev = Class5to2(x_dev, y_dev)

	return(x_train, y_train, x_dev, y_dev)

def Class5to2 (x, y):
	x2 = []
	y2 = []
	for i in range(len(x)):
		if y[i] == 2:
			continue
		if y[i] > 2:
			y2.append(1)
		else:
			y2.append(0)
		x2.append(x[i])
	return x2, y2
		


# x_train, y_train, x_dev, y_dev = Preparedata("train.txt", "dev.txt", 20000)
# print(y_train)
# print(x_train)

# dic = {}
# dic["a"] = [1,]
# dic["b"] = [2,]
# dic["a"].append(4)
# dic["c"] = [1,[1,2]]
# # if dic.get("a")[1] == 1:
# # 	print("that's right")
# print(dic["c"])
# if dic.get("c") == None:
# 	dic["c"] = [1,]
# else:
# 	t = dic.get("c")
# 	t[0] = t[0] + 1
# 	t[1].append(3)
# 	dic["c"] = t

# print(dic.get("c"))
# print(dic)
