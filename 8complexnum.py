class Complex:
    def __init__(self,real=0,imag=0):
        self.real = real
        self.imag = imag
    def display(self):
        print(f"{self.real}+{self.imag}i")
def addComplex(c1,c2):
    new_real = c1.real+c2.real
    new_imag = c1.imag+c2.imag
    return Complex(new_real,new_imag)
n = int(input("Enter the number of complex numbers(n>=2:)"))
while n<2:
    n=int(input("Enter the number n>=2"))
print("\nEnter the complex numbers:")
real = float(input("Enter real part of #1"))
imag = float(input("Enter imaginary part of #1"))
result = Complex(real,imag)
for i in range(2,n+1):
    real = float(input(f"Enter real part of #{i}:"))
    imag = float (input(f"Enter imaginary part of #{i}:"))
    temp= Complex(real,imag)
    result = addComplex(result,temp)
print("\n Sum of all Complex numbers =",end='')
result.display()
