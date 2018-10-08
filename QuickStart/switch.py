from random import choice, choices
def main():
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth'
        )
    v = 'five'
    print(choices.get(v,'others'))
    
if __name__ == "__main__": main()