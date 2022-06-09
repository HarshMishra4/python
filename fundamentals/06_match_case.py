# Match Case 
# Simple python program to convert
# given day value from number to Word

day = 9

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case default:
        print("Invalid Input")

        



# ================================================
#               Using Boolean case
# ================================================

isLoggedIn = True
match isLoggedIn:
    case True:
        print("Welcome User")
    case False:
        print("Please Login to Continue")
    
