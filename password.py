import random
class Password:
    def __init__(self):
        self.letters=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.numbers=list("0987654321")
        self.symbols=list("!#@$%^&*()+=-")
        self.l=random.randint(8,10)
        self.n=random.randint(2,4)
        self.c=random.randint(2,4)
    def generate(self):
        ans=""
        for i in range(self.l):
            ans+=random.choice(self.letters)
        for i in range(self.n):
            ans+=random.choice(self.numbers)
        for i in range(self.c):
            ans+=random.choice(self.symbols)
        pw=list(ans)
        random.shuffle(pw)
        return "".join(pw)