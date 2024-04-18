#the function named "getorder" is created 
def getorder(final_orders):
    for i in range(0,len(final_orders)):
        print("preparing your order:-",final_orders[i])
    final_orders.reverse() #here we reversed the list to dispatch the item in order they come
    print("The following order is dispatched:")
    for j in range(0,len(final_orders)):
        print(final_orders.pop()) #we have used pop methos to remove the elements as we doesnot give any parametre to pop() it will by defaul remove the last element
    
#at first we have taken the name of the user
name = input("please enter your name")
print()
#we have created an empty list i.e. "final_orders" to store the orders in it
final_orders = []
#here, we have printed the menu by using the another list
print("Here is our restaurent's menu! You can choose anything")
menu = ['dal bati churma','panner tikka','palak paneer','dal biscuit','malai kofta','laccha paratha']
print()
for i in menu:
    print(i,end="     ")
    print()
#here we ask user to enter what they want and the loop iterates for thier choice untile they type no and append thier order in final_order list simultaneously
for i in menu:
    orders = input("what you wants to order,or wants to order anything else.(type no to procced only with selected items):-")
    if(orders=='no'):
        break
    else:
        final_orders.append(orders)
print("you have ordered :-",final_orders)

getorder(final_orders) #here we called the function for processing details
