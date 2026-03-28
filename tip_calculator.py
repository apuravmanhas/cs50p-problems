#function 
def calculate_tip(food_cost, tip_percentage):
    tip_amount = food_cost * (tip_percentage / 100)
    return tip_amount

def main():
    food_cost = float(input("Enter the cost of the food: "))
    tip_percentage = float(input("Enter the tip percentage: "))
    tip = calculate_tip(food_cost, tip_percentage) # Call the function to calculate the tip
    print(f"The tip amount is: {tip:.2f}")
main()