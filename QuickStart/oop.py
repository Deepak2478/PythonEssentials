class AnimalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self):return self.strings['fur']
    
class Duck(AnimalActions):
    strings = dict(
        quack = "regrgfd",
        feathers = "sdfsdf",
        bark = "dfgds",
        fur = "sdfds"
    )
    

class Person(AnimalActions):
    strings = dict(
        quack = "dsfd",
        feathers = "fdgdfs",
        bark = "sgfsd",
        fur = "sdsdffds"
    )
    
def in_the_duckhouse(duck):
    print(duck.quack())
    print(duck.feathers())
    
def main():
    donald= Duck()
    john = Person()
    
    print("_In the duckhouse_")
    for o in (donald,john):
        in_the_duckhouse(o)

if __name__ == "__main__":main()
