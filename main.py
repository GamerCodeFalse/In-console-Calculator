#Calculator Project
#Made By Nishil Balmoori A.K.A GamerCodeFalse
#Was made in 25 or so minutes



def SolveProblem(Num1,Num2,operator):
    if DefineOperator(operator) == "Add":
        print("Your answer would be:", Num1+Num2)
    elif DefineOperator(operator) == "Sub":
        print("Your answer would be:", Num1-Num2)
    elif DefineOperator(operator) == "Multi":
        print("Your answer would be:", Num1*Num2)
    elif DefineOperator(operator) == "Divide":
        print("Your answer would be:", Num1/Num2)
    elif DefineOperator(operator) == "Expo":
        print("Your answer would be:", Num1**Num2)
    elif DefineOperator(operator) == "Root":
        print("Your answer would be:", Num1**(1/Num2))
def DefineOperator(char):
    if char == '+':
        return "Add"
    elif char == '-':
        return "Sub"
    elif char == '*':
        return "Multi"
    elif char == '/':
        return "Divide"
    elif char == '^':
        return "Expo"
    elif char == '!':
        return "Root"
def WelcomeAndProblemArgs():
    print("\n")
    print("Welcome to the Calculator in Python!\n")
    print("Note, ! is for root. ex: input: 2!9 output: 3.\n")
    FloatOrInt = input("Do you want the problem in decimal form or integer form?\n")
    if FloatOrInt == "Float":
        WelcomeAndProblemArgs.Num1 = float(input("Enter the first number for the problem:\n"))
        WelcomeAndProblemArgs.Num2 = float(input("Enter the second number for the problem:\n"))
        WelcomeAndProblemArgs.operator = input("What operator do you want (Enter +,-,*,/,^,!)?\n")
    elif FloatOrInt == "Integer":
        WelcomeAndProblemArgs.Num1 = int(input("Enter the first number for the problem:\n"))
        WelcomeAndProblemArgs.Num2 = int(input("Enter the second number for the problem:\n"))
        WelcomeAndProblemArgs.operator = input("What operator do you want (Enter +,-,*,/,^,!)?\n")
    else:
        print("Sorry This please enter A float or int answer.")
def run():
    WelcomeAndProblemArgs()
    SolveProblem(WelcomeAndProblemArgs.Num1, WelcomeAndProblemArgs.Num2, WelcomeAndProblemArgs.operator)

if __name__ == "__main__" :
    while True:
        run()