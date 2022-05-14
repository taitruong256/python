class _Dictionary:
    key=0
    value=0
    def __init__(self, key, value):
        self.key=key
        self.value=value

NumberFace=6
NumberDices=0
TotalRequire=0
RequireResultNumber=0
Dices=[]
for i in range(10): Dices.append([0]*NumberFace)
TempIndex=0
RequireResult=[]
for i in range(NumberFace): RequireResult.append(_Dictionary(0, 0))
StartIndexRow=3
StartIndexColumn=1
TypeCalculation=0  # 0 as compute single value, 1 as compute whole table
Numerator=0
Demoninator=0
NameOfFace=[""]*NumberFace

def Probability():
    TypeCalculation=0
    Initial=0
    
def Initial():
    NameOfFace[0] = "BAU"
    NameOfFace[1] = "CUA"
    NameOfFace[2] = "TOM"
    NameOfFace[3] = "CA"
    NameOfFace[4] = "GA"
    NameOfFace[5] = "NAI"
    
def GCD(x, y):
    while x>0:
        Current = x
        x = y % x
        y = Current
    return y

def Factorial(n):
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res





    



