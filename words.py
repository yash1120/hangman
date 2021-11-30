word_list =[]
f = open("ab.text",'r')
for i in range(10000):
    word_list.append(f.readline().strip())
