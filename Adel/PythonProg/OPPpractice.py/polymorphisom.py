class Complex:


    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary



    def __add__(self,num):
        newR=self.real+num.real
        newI=self.imag+num.imag
        return Complex(newR,newI)



    def __sub__(self,num):
        newR=self.real-num.real
        newI=self.imag-num.imag
        return Complex(newR,newI)



    def showcompex(self):
        print(f"{self.real}+{self.imag}j")


c1 = Complex(2, 3)
c1.showcompex()


c2 = Complex(1, 4)
c2.showcompex()

c3=c1+c2

c3.showcompex()
