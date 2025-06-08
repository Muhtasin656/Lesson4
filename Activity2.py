amount=int(input("enter the amount"))
note100=amount//100
note50=(amount %100)//50
note10=((amount %100)%50)//10
print("note of 100 rupee are",note100)
print("note of 50 are",note50)
print("note of 10 are",note10)