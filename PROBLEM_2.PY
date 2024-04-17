#Problem_statement: - 2
def choice():
    global user_name
    global size
    brands = ['puma','nike','H&m', 'van heusen','gucci','allen solly','jacks and jones']
    size_list = ['s','m','l','xl','xxl','xxxl']
    brand_name = input("Which brand of T-shirt are you looking for:")
    for i in brands:
        if(brand_name == i):
            for j in size_list:
                if(size==j):
                    print("Hi,",user_name, "the brand and the size you are looking for is available in our shop")
                    break
            break
    else:
        print("Hi, user the ebrand you are looking for is not available in our store")
def get_name():
    global user_name
    user_name = input("enter your name:")
    return user_name
def get_tshirt():
    get_name()
    get_size()
    choice()
def get_size():
    global size
    size = input("what is the size you want")
    return size
    
get_tshirt()
