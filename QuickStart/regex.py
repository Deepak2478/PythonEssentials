import re

def main():
    fh = open('reven.txt')
    for line in fh:
        match = re.search('(Len/test)it',line)
        if match:
            print(line.replace(match.group(),'###'))

if __name__ == "__main__":main()