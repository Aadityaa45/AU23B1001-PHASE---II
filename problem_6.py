global annual_site_profit
global future_gain_improvement
global improved_conversion_rate
global current_conversion_rate
global intrest_rate 
global EPL
global future_gain_improvement 
def future_gain_from_improvement():
    global annual_site_profit
    global future_gain_improvement
    global improved_conversion_rate
    global current_conversion_rate
    global intrest_rate 
    global EPL
    global future_gain_improvement 
    global improvement_cost
    annual_site_profit = float(input("enter the value of annual site profit:"))
    print()
    improved_conversion_rate = float(input("enter the improved conversion rate(in%):"))
    print()
    current_conversion_rate = float(input(" enter current conversion rate(in%):"))
    print()
    intrest_rate = float(input("enter the intrest rate:"))
    print()
    EPL = float(input("Expected project life(in years):"))
    print()
    improvement_cost = float(input("enter the imrovement cost:"))
    future_gain_improvement = ((annual_site_profit * (improved_conversion_rate/current_conversion_rate)) - annual_site_profit) * (((1+intrest_rate)**EPL-1)/intrest_rate) - (improvement_cost*((1+intrest_rate)**EPL))
    return future_gain_improvement


def total_gain_from_improvement():
    global future_gain_improvement 
    global intrest_rate
    global EPL
    global total_improvement_gain
    i = (future_gain_from_improvement())
    total_improvement_gain = (i /(1+intrest_rate)**EPL)
    return total_improvement_gain


def annual_gain_from_improvement():
    global EPL
    global annual_improvement_gain
    x = total_gain_from_improvement()
    print(x)
    annual_improvement_gain = x/EPL
    return annual_improvement_gain


def annual_ROI():
    global improvement_cost
    global Annual_ROI
    y = annual_gain_from_improvement()
    Annual_ROI = y/improvement_cost
    return Annual_ROI

def total_ROI():
    global improvement_cost
    global Total_ROI
    z = total_gain_from_improvement()
    Total_ROI = z/improvement_cost
    output = print("The total return on investment is:",Total_ROI)
    return output
    

requirements = ['annual site profit','improved conversion rate','current conversion rate','intrest rate','project life years','improvement cost']

print("You need following data to compute return on investment:-")

for items in requirements:
    print(items,end=" ")
    print()
    print()
print()
ask = input("start calculation(yes/no):")
print()
if(ask=='yes'):
    print(total_ROI())

else:
    ("thankyou")