## write the file

with open("test.txt", 'w') as file:
    file.write('Hello, this is a test file.')
    
    
    
    
## Read the file

with open("test.txt", 'r') as file:
    content=file.read()
    print(content)
    

balance=1000
try:
    deposit=float(input("enter the amount"))
    balance+=deposit
    print('Total amount: ', balance)
    
except ValueError:
    print("please enter the valid amount")


    
    
    
    
