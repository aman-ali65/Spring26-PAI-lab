# Water Jug Problem Solver

x = 0
y = 0


x_cap = 7
y_cap = 4
goal = 6

# goal = int(input("Enter the goal amount of water to be measured: "))
# x_cap = int(input("Enter capacity of jug X: "))
# y_cap = int(input("Enter capacity of jug Y: "))

print(f"Jug X capacity: {x_cap}, Jug Y capacity: {y_cap}, Goal: {goal}")
print("\nRules:")
print("1: Fill X")
print("2: Fill Y")
print("3: Empty X")
print("4: Empty Y")
print("5: Pour X -> Y until X is empty")
print("6: Pour X -> Y until Y is filled")
print("7: Pour Y -> X until Y is empty")
print("8: Pour Y -> X until X is filled\n\n")


while x != goal and y != goal:
    print(f"Current State: X = {x} , Y = {y}")

    r = int(input("Enter your choice (1-8) or 0 for exit: "))

    if r == 1:
        x = x_cap

    elif r == 2:
        y = y_cap

    elif r == 3:
        x = 0

    elif r == 4:
        y = 0

    elif r == 5:
        
        totl = x + y
        y = min(y_cap, totl)  
        x = 0                  

    elif r == 6:
        
        space_in_y = y_cap - y
        transfer = min(x, space_in_y)
        y += transfer
        x -= transfer

    elif r == 7:
        
        totl = x + y
        x = min(x_cap, totl)  
        y = 0                  

    elif r == 8:
        
        space_in_x = x_cap - x
        transfer = min(y, space_in_x)
        x += transfer
        y -= transfer

    elif r == 0:
        print("Exiting.........\n")
        break

    else:
        print("Invalid choice")

else:
    print(f"\nGoal achieved! ; Current State: X = {x} , Y = {y}")