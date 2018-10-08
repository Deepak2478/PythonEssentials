class Animal:
    def talk(self): print('talk')
    def walk(self):print('walk')

class Duck(Animal):
    def __init__(self,color):
        self._color = color
        
    def quack(self):
        print('Quack')
        
    def set_color(self,color):
        self._color = color
        
    def get_color(self):
        return self._color
    
def main():
    donald = Duck()
    print(donald.get_color())
    donald.set_color('blue')
    print(donald.get_color())
    donald.talk()
    
if __name__ == "__main__":main()