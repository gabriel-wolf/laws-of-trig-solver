# TODO: add new identities
# TODO: backwards solve (e.g. average --> sides)
# FIXME: loc allow solve var not to c
# TODO: heron add reg perimeter
# FIXME: add los loc mutliple solutions






from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

from sympy import expand, trigsimp, expand_trig
from sympy import sin, pi, cos, tan, asin, acos, atan, Eq, Function, exp, simplify, solveset, S
from sympy.abc import x, theta
from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')




 
def heron(A, B, C, showSteps=False, justsolution=False):
    showStepsList = []
    
    Svar = N((A + B + C)/2,5)
    showStepsList.append("S = " + str(Svar))
    Area = N(sqrt((Svar)*((Svar-A)*(Svar-B)*(Svar-C))),5)
    showStepsList.append("Area = " + str(Area))
    
    if (showSteps == True):
        for step in showStepsList:
            print(step)
    
    if justsolution == False:
        return ("Area: " + str(Area) + "\nSemi-Per: " + str(Svar))
    else:
        return Area



def thesolver(A, B, C, a, b, c, method="sin", showSteps=False):
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
    print("Or use this:")
    print(">>> heron(A, B, C, True/False)")
    print("Method and showSteps are optional args")
    print("Try it!\n")
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





# NOT CURRENTLY WORKING
def challenge15(times = 5, forever=False):
    from random import randint
    if (forever == True):
        times = -12345

    while (times == -12345 or times > 0):
        # if (True):
        try:
            c = randint(0,12)
            # print(str(int(12-c)))
            a = randint(0,int(N(12-c)))
            b = 12 - c - a
            A = 0
            B = 0
            C = 0

            if (a >= b and a >= c):
                C = a
                B = b
                A = c
            elif (b >= a and b >= c):
                C = b
                A = a
                B = c
            else:
                C = c
                B = b
                A = a
       

            if (forever == True):
                if(Eq(N((A**2)+(B**2),5),N(C**2,5)) == False):
                    # print("Got part of it!")
                    if ((heron(A,B,C,False,True)).is_integer() == True):
                        print("GOT IT!\nANSWER IS: A : " + str(A) + " B : " + str(B) + " C : " + str(C))
                        times = 0
                        exit(0)
            else:
                if (heron(A,B,C,False,True).is_integer() == True):
                    print("int int int!")
                    print("Trying: " + str(A) + " " + str(B) + " " + str(C))
                    print("Sum: " + str(A+B+C))
                    print("Solutions: " + heron(A,B,C))
                    print(str(N((A**2)+(B**2),5)) + " = " + str(N(C**2,5)))
                    if(Eq(N((A**2)+(B**2),5),N(C**2,5)) == False):
                        print("Not right triangle!")
                    print("\n\n")

        except:
           None
            
        1
        if times != 12345:
            times = times - 1

               


            
def challenge16_7(times = 20):
    from random import randint
    
    for i in range(times):
        c = randint(0,500)
        a = randint(0,int(N(500-c)))
        b = 500 - c - a
        A = 0
        B = 0
        C = 0

        if (a >= b and a >= c):
            C = a
            B = b
            A = c
        elif (b >= a and b >= c):
            C = b
            A = a
            B = c
        else:
            C = c
            B = b
            A = a

        print("Trying A: " + str(A) + " B: " + str(B) + " C: " + str(C) + "...")
        print("Area: " + str(heron(A,B,C,False,True)))
        try:
            if (float(sympify(heron(A,B,C,False,True))) == int(sympify(heron(A,B,C,False,True)))):
                print("Area is int!")
        except:
            None
        if (Eq(N((A**2)+(B**2),5),N(C**2,5)) == False):
            print("Not right triangle")
  
        try:
            if ((Eq(N((A**2)+(B**2),5),N(C**2,5)) == False) and (float(sympify(heron(A,B,C,False,True))) == int(sympify(heron(A,B,C,False,True))))):
                print("Satisfies both!")
                exit(0)
        except:
            None
            
        print("\n")
        
            

# NOT WORKING
def challenge16_9():
    a, b, c = symbols('a b c')
    expr1 = (b*((2*a*cos(theta))-b))
    expr2 = ((a-c)*(c+a))
    expr = (Eq(expr1, expr2))
    
    print(solve(expr1))
    print(expand_trig(expr1))

    print(solve(expr2))
    print(expand_trig(expr2))

    print(solve(expr))
    print(expand_trig(expr))


    


    
userInputLoop()


