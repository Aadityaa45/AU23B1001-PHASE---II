#Problem statement :-1
#here the function choice is define whose purpose is to check weather the given brand tshirt is available or not
def choice():
    #here global variable is used for user name
    global user_name
    #various t-shirt brands are stored in the brands list
    brands = ['puma','nike','H&m', 'van heusen','gucci','allen solly','jacks and jones']
    #here asked user to say which brand they are looking for
    brand_name = input("Which brand of T-shirt are you looking for:")
    #here we have implemented the for loop in brands to check the every element present in the list brands
    for i in brands:
        if(brand_name == i): #if entered brand name present in the list then it will greet the user
            print("Hi,",user_name, "the brand you are looking for is available in our shop")
            break #break is used to terminate the loop once after if the brand found 
    else:
        print("Hi, user the ebrand you are looking for is not available in our store")
#here we declared the function get_name() whose purpose is to take name input
def get_name():
    global user_name
    user_name = input("enter your name:")
    return user_name
def get_tshirt():
    get_name()
    choice()

get_tshirt()
