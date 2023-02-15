# f = open('text.txt', 'r')
# f.close()

with open('text.txt', 'r') as f:
    # print(f.read())
    pass

for i in f:
    print(i)
    