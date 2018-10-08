try:
    fh = open('zfile.txt')
    for line in fh.readLines():
        print(line)
except IOError as e:
        print("Exception catched")
        
print("after exception")