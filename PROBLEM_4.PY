def add_topings(scoop_size,toppings):
    print("Your scoop size that you have selected is :",scoop_size)
    if toppings:
        print("your Toppings:")
        for k in toppings:
            print(k,end="    ")
    else:
        print("No toppings added.")
        print()
    print("Your ice-cream soon will be on your tables:")
    shake=input("did you like to try out our shakes(yes/no):")
    if(shake=='yes'):
        shake_choice = input("what you wants nuts shake or fruits shake:")
        print(make_shake(shake_choice))
    else:
        print("Thankyou, you will recieve your icecream soon")
def make_shake(shake_choice):
    nuts_shake = ['banana nut shake','walnut shake','date and nut shake']
    fruit_shake = ['chocolate shake','banana shake','strawberry shake','mango shake']
    for i in nuts_shake:
        print(i,end="      ")
    print()
    for j in fruit_shake:
        print(j,end="       ")
    option = input("select what you wants to try:")
    for i in nuts_shake:
        if(option==i):
            print("preparing your nuts shake")
            break
    for j in fruit_shake:
        if(option==j):
            print("preparing your fruits_shake")
            break
print("Hello, welcome to our icecream parlour")
scoop_input=input("select the scoop size you want in icecream:")
toppings =['fudge','wheeped cream','crushed nuts']
toppings_selected = []
for i in toppings:
    print(i,end="  ")
for j in toppings:
    select = input("select the toppings you like to have,you can select multiple,enter no to procced with selected items:")
    if(select=='no'):
        break
    else:
        toppings_selected.append(select)
print("you have selected topings :-",toppings_selected)
print(add_topings(scoop_input,toppings_selected))
            
    