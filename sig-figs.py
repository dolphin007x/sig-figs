num = input("Enter the number : ")
digits = list(num)
isDecimal = False
nod = 0

if '.' in digits:
    isDecimal = True
    nod = len(digits)-digits.index('.')-1

modified_num = int(num) if isDecimal == False else float(num)
modified_num *= pow(10, nod)
modified_num = int(modified_num)

print(len(str(modified_num)))
