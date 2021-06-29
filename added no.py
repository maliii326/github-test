tuple_item = ()
total_items = int(input("enter the total number of items:"))
for i in range(total_items):
    user_input = int(input("enter a number:"))
    tuple_item += (user_input,)
    print(f"items added to tuple are {tuple_item}")

 