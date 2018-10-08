class Egg:
    def __init__(self,kind="fried"):
        self.kind = kind
        
    def whatKind(self):
        return self.kind
    
def main():
    fried = Egg()
    scrambbled = Egg("scrambled")
    print(fried.whatKind())
    print(scrambbled.whatKind())
    
if __name__ == "__main__":main()