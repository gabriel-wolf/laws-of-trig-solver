from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

from sympy import sin, pi, cos, tan, asin, acos, atan, Eq, Function, exp, simplify, solveset, S
from sympy.abc import x
from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')



def thesolver(A, B, C, a, b, c, method, showSteps):
    showStepsList = []
    nameSolveFor = ""
    canUseBoth = []
    indexSFO = 0
    solvingForAngle = False
    solvingForSide = False
    bothDict = {"A": A, "B": B, "C": C, "a": a, "b": b, "c": c}
    allSides = [a, b, c]
    allAngles = [A, B, C]

    eq1 = 0
    eq2 = 0
    
    for key, val in bothDict.items():
        if (val == "?"):
            nameSolveFor = key
            if(str(key.upper()) == str(key)):
                showStepsList.append("We are solving for a angle.")
                solvingForAngle = True
            else:
                showStepsList.append("We are solving for a side.")
                solvingForSide = True
        

    for i in range(3):
        if (allSides[i] != "X" and allSides[i] != "?"):
            if (allAngles[i] != "X" and allAngles[i] != "?"):
                if (i == 0):
                    canUseBoth.append(1)
                elif (i == 1):
                    canUseBoth.append(2)
                elif (i == 2):
                    canUseBoth.append(3)

    showStepsList.append("The variable we are solving for is variable " + str(nameSolveFor))

    if (method == "sin"):
        showStepsList.append("Here are the sets of matching known sides and angles that we can use:")
        for name in canUseBoth:
            if (int(name) == 1):
                eq1 = (sin(int(allAngles[int(name) - 1]))/(int(allSides[int(name) - 1])))
                showStepsList.append("A = " + str(allAngles[int(name) - 1]))
                showStepsList.append("a = " + str(allSides[int(name) - 1]))
            if (int(name) == 2):
                eq1 = (sin(int(allAngles[int(name) - 1]))/(int(allSides[int(name) - 1])))
                showStepsList.append("B = " + str(allAngles[int(name) - 1]))
                showStepsList.append("b = " + str(allSides[int(name) - 1]))
            if (int(name) == 3):
                eq1 = (sin(int(allAngles[int(name) - 1]))/(int(allSides[int(name) - 1])))
                showStepsList.append("C = " + str(allAngles[int(name) - 1]))
                showStepsList.append("c = " + str(allSides[int(name) - 1]))

    if (method == "cos"):
        eq1 = (x**2)

    if (str(nameSolveFor) == "A"):
        indexSFO = 1
    if (str(nameSolveFor) == "B"):
        indexSFO = 2
    if (str(nameSolveFor) == "C"):
        indexSFO = 3
    if (str(nameSolveFor) == "a"):
        indexSFO = 4
    if (str(nameSolveFor) == "b"):
        indexSFO = 5
    if (str(nameSolveFor) == "c"):
        indexSFO = 6
        
    if (method == "sin"):
        showStepsList.append("And here is the set containg the value we are looking for:")
        if (int(indexSFO) > 3):
            indexhere = indexSFO
            if (int(indexhere) == 1):
                showStepsList.append("A = " + str(allAngles[int(indexhere) - 1]))
                showStepsList.append("a = ?")
                eq2 = (sin(int(allAngles[int(indexhere) - 1]))/x)
            if (int(indexhere) == 2):
                showStepsList.append("B = " + str(allAngles[int(indexhere) - 1]))
                showStepsList.append("b = ?")
                eq2 = (sin(int(allAngles[int(indexhere) - 1]))/x)
            if (int(indexhere) == 3):
                showStepsList.append("C = " + str(allAngles[int(indexhere) - 1]))
                showStepsList.append("c = ?")
                eq2 = (sin(int(allAngles[int(indexhere) - 1]))/x)
        else:
            indexhere = indexSFO
            if (int(indexhere) == 1):
                showStepsList.append("A = ?")
                showStepsList.append("a = " + str(allSides[int(indexSFO) - 1]))
                eq2 = (sin(x)/(allSides[int(indexSFO) - 1]))
            if (int(indexhere) == 2):
                showStepsList.append("B = ?")
                showStepsList.append("b = " + str(allSides[int(indexSFO) - 1]))
                eq2 = (sin(x)/(allSides[int(indexSFO) - 1]))
            if (int(indexhere) == 3):
                showStepsList.append("C = ?")
                showStepsList.append("c = " + str(allSides[int(indexSFO) - 1]))
                eq2 = (sin(x)/(allSides[int(indexSFO) - 1]))

                
    if (method == "cos"):
        eq2 = ((allSides[0])**2)+((allSides[1])**2)-(2*(allSides[0])*(allSides[1]))*(cos(rad(allAngles[2])))

            
    showStepsList.append("The 2 equations on each side of the equal sign are as follows:")
    showStepsList.append(eq1)
    showStepsList.append(eq2)


    if (showSteps == True):
        for step in showStepsList:
            print(step)
    
    solveList = (solve(Eq(eq1,eq2),x))


    if (method == "sin"):
        return abs((deg(solveList[1])).evalf())
    else:
        return abs(solveList[1].evalf())

    

def sendtoSolver():
    print("not here yet")
    return "sorry"


def demoproblems():
    try:
        print(thesolver(80, "?", "X", 11, 9, "X", "sin", False))
    except:
        print("Something went wrong when trying to solve demo problem #1")
    try:
        print(thesolver("X", "X", 83, 15, 12, "?",  "cos", False))
    except:
        print("Something went wrong when trying to solve demo problem #2")

    
def dointeractive():
    print("Interactive mode activated.")
    A = None;
    B = None;
    C = None;
    a = None;
    b = None;
    c = None;
    method = "sin"
    steps = False
    promptsList = ["\nA >>> ", "\nB >>> ", "\nC >>> ", "\na >>> ", "\nb >>> ", "\nc >>> ", "\nmethod >>> ", "\nsteps >>> ", "\nSolve now?\n>>> "]
    while True:
        for prompt in promptsList:
            currindex = promptsList.index(prompt)
            print("A = " + str(A) + " B = " + str(B) + " C = " + str(C) + " a = " + str(a) + " b = " + str(b) + " c = " + str(c))
            if (method == "sin"):
                print("Solving using the law of sines. ", end="")
            else:
                print("Solving using the law of cosines. ", end="")
            if (steps == True):
                print("Showing steps.")
            else:
                print("Not showing steps.")

            if (currindex > 7):
                uinput = input(prompt)
                if (uinput.lower() == "yes"):
                    try:
                        print(thesolver(A, B, C, a, b, c, method, steps))
                    except:
                        print("Something went wrong when solving.")
                    break
                elif (uinput.lower() == "quit"):
                    print("Quitting...")
                    exit(0)
                else:
                    print("Okay. Returning to normal mode.")
            elif (currindex == 6):
                uinput = input(prompt)
                if (uinput == "sin"):
                    method = "sin"
                elif (uinput == "cos"):
                    method = "cos"
                elif (uinput.lower() == "quit"):
                    print("Quitting...")
                    exit(0)
                else:
                    method = "sin"
            elif (currindex == 7):
                uinput = input(prompt)
                if (uinput.lower() == "true" or uinput.lower() == "yes"):
                    steps = True
                elif (uinput.lower() == "false" or uinput.lower() == "no"):
                    steps = False
                elif (uinput.lower() == "quit"):
                    print("Quitting...")
                    exit(0)
                else:
                    steps = False
            else:
                uinput = input(prompt)
                if (uinput.lower() == "quit"):
                    print("Quitting...")
                    exit(0)
                else:
                    if (currindex == 0):
                        if (str(uinput) == "X"):
                            A = "X"
                        elif (str(uinput) == "?"):
                            A = "?"
                        else:
                            A = int(uinput)
                    elif (currindex == 1): 
                        if (str(uinput) == "X"):
                            B = "X"
                        elif (str(uinput) == "?"):
                            B = "?"
                        else:
                            B = int(uinput)
                    elif (currindex == 2): 
                        if (str(uinput) == "X"):
                            C = "X"
                        elif (str(uinput) == "?"):
                            C = "?"
                        else:
                            C = int(uinput)
                    elif (currindex == 3): 
                        if (str(uinput) == "X"):
                            a = "X"
                        elif (str(uinput) == "?"):
                            a = "?"
                        else:
                            a = int(uinput)
                    elif (currindex == 4): 
                        if (str(uinput) == "X"):
                            b = "X"
                        elif (str(uinput) == "?"):
                            b = "?"
                        else:
                            b = int(uinput)
                    elif (currindex == 5): 
                        if (str(uinput) == "X"):
                            c = "X"
                        elif (str(uinput) == "?"):
                            c = "?"
                        else:
                            c = int(uinput)
                            
                
            
            
        
        
        


def userInputLoop():
    print("For now you have to use the notation as follows: ")
    print(""">>> thesolver(A, B, C, a, b, c, "sin/cos", True/False)""")
    print("""Where the unkown values are denoted by "X" and the variable solving for is "?". True/False = show steps""")
    print("Or you can type interactive to try out interactive mode")
    while True:
        uinput = input(">>> ")
        if (uinput == "quit"):
            break
        elif (uinput == "interactive"):
            dointeractive()
        else:
            try:
                print(eval(uinput))
            except:
                print("Something went wrong when trying to do evaluate the user input.")


            
            
userInputLoop()


