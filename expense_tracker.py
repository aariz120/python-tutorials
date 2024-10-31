expenses=[]
def add_expense(amount,category,description):
    expenses.append({"amount":amount,"category":category,"description":description})
    
    
def view_expenses():
    for index,expense in enumerate(expenses,1):
        print(f"{index}.amount:${expense['amount']:.2f},category:{expense['category']},description:{expense['description']}")
        
def total_expenses():
    return sum(expense['amount']for expense in expenses)

def expenses_by_category():
    categories={}
    for expense in expenses:
        category=expense['category']
        amount=expense['amount']
        categories[category]=categories.get(category,0)+amount
    return categories

def main():
    while True:
        print("\n Expense Manager")
        print("1.Add expense")
        print("2.View expense")
        print("3.View total expenses")
        print("4.Expenses by category")
        print("5. Exit")
        
        choice=input("enter your choice(1-5)")
        if choice=='1':
            amount=float(input("enter amount :"))
            category=input("enter category :")
            description=input("enter description")
            add_expense(amount,category,description)
            print("expense added successfully")
            
        elif choice=='2':
            view_expenses()
            
        elif choice=='3':
            print(f"total expenses:${total_expenses():.2f}")
            
        elif choice=="4":
            categories=expenses_by_category()
            for category,amount in categories.items():
                print(f"{category} : ${amount:.2f}")
            
        elif choice=="5":
            print("Thankyou for usiong Expense Manager, Goodbye!")
            break
        else:
            print("invalid choice . please try again")
            
if __name__=="__main__":
    main()
            