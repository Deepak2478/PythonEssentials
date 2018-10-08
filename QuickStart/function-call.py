def func(a=7):
    for i in range(a,10):
        print(i,' ')
    print()


def main():
    func(1)
    func()
    func(5)

if __name__ == "__main__":main()    