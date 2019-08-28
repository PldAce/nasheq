#//=============================================================================
#//  Group Number:       15
#//  PROGRAMMER1:        Armando Carrasquillo
#//
#//
#//  CLASS:              CAP55076
#//  SECTION:            U01
#//  SEMESTER:           Spring 2019
#//  CLASSTIME:          M/W 6:25-7:40 pm
#//
#//  Project:            Nash EQ Calculator
#//  DUE:                4/7/2019 11:59 pm
#//
#//  CERTIFICATION:	 I certify that this work is my own and that none of it
#//                   is of the work of any other person
#//=============================================================================
from array import *
from random import randint

rows, cols, choice = 0, 0, 'a'

def p1Strat():
    print ("-------------------------------------------------------")
    print ("Player: Player1's strategies")
    print ("-------------------------------------------------------")
    pline = ""
    val = 1
    for i in range(rows):
        if i == 0:
            pline = "{A" + str(val) + ", "
        elif i == rows - 1:
            val = val + 1
            pline = pline + "A" + str(val) + "}"
        else:
            val = val + 1
            pline = pline + "A" + str(val) + ", "
    print (pline + "\n")

def p2Strat():
    print ("-------------------------------------------------------")
    print ("Player: Player2's strategies")
    print ("-------------------------------------------------------")
    pline = ""
    val = 1
    for i in range(cols):
        if i == 0:
            pline = "{B" + str(val) + ", "
        elif i == rows - 1:
            val = val + 1
            pline = pline + "B" + str(val) + "}"
        else:
            val = val + 1
            pline = pline + "B" + str(val) + ", "
    print (pline + "\n")

def payOffs(arr):
    pline, val = "", ""
    for i in range(rows):
        for j in range(cols):
            if j == 0:
                pline = '{0: >3}'.format(arr[i][j])
            else:
                val = '{0: >3}'.format(arr[i][j])
                pline = pline + ", " + val
        print (pline)
    print ("\n")

def normalForm(x,y):
    print ("========================================")
    print ("Display Normal Form")
    print ("========================================")
    nfline, dline, val = "", "", 1
    for i in range(cols):
        if i == 0:
            nfline = "          " + "B" + str(val) + "       "
        else:
            val = val + 1
            nfline = nfline + "      " + "B" + str(val) + "       "
    print (nfline)
    for i in range(cols):
        if i == 0:
            dline = "   ---------------"
        elif i == (cols - 1):
            dline = dline + "---------------"
        else:
            dline = dline + "---------------"
    print (dline)
    p1strat, stratline, pvals, val = "", "", "", 0
    for i in range(rows):
        val = val + 1
        p1strat = "A" + str(val) + " "
        for j in range(cols):
            if j != cols - 1:
                pvals = pvals + "|  (" + '{0: >3}'.format(x[i][j]) + "," + '{0: >3}'.format(y[i][j]) + ")   "
            else:
                pvals = pvals + "|  (" + '{0: >3}'.format(x[i][j]) + "," + '{0: >3}'.format(y[i][j]) + ")  |"
        stratline = p1strat + pvals
        print (stratline)
        print (dline)
        pvals = ""
    print ("\n")

def checkEQ(a, x, y, player):
    maV= -99
    for i in range(x):
        for j in range(y):
            if (player == 1 and int(a[j][i]) > int(maV)):
                maV = a[j][i]
            elif (player == 2 and int(a[i][j]) > int(maV)):
                maV = a[i][j]
        for k in range(y):
            if (player == 2 and int(a[i][k]) == int(maV)):
                a[i][k] = "H"
            elif (player == 1 and int(a[k][i]) == int(maV)):
                a[k][i] = "H"
        maV = -99

def printEQ(p1ANash, p2BNash):
    setEQ = ""
    for i in range(rows):
        for j in range(cols):
            if (p1ANash[i][j] == "H" and p2BNash[i][j] == "H"):
                nashEQ = 1
                if setEQ == "":
                    setEQ = "(A" + str(i + 1) + ", B" + str(j + 1) + ")"
                else:
                    setEQ = setEQ + ", (A" + str(i + 1) + ", B" + str(j + 1) + ")"
    if setEQ == "":
        setEQ = "NONE"
        nashEQ = 0
    print ("Pure Nash EQ: " + setEQ + "\n")
    return nashEQ

def randBR(x, player1, player2, numb, numb2, arr):
    a, temp = 100, 0
    for i in range(numb - 1):
        temp = (randint(0,a))
        a = a - temp
        arr[i] = round(float(temp / 100), 2)
    if (a == 0):
        arr[i + 1] = 0.00
    else:
        arr[i + 1] = round(float(a / 100), 2)

def printBR(x, player1, player2, numb, numb2, arr):
    a, max, brPrint = 100, -1000.01, ""
    bestr = "BR("
    result = [1.01 for j in range(numb)]
    tempF = 0.00
    print ("-------------------------------------------------------")
    print ("Player " + str(player1) + "'s' Expected Payoffs with " + str(player2) + " Mixing")
    print ("-------------------------------------------------------")
    for i in range(numb2):
        if player1 == 1:
            brPrint = "U(A" + str(i + 1) + ",  ("
        else:
            brPrint = "U(("
        for j in range(numb):
            tempF = tempF + float(x[i][j]) * arr[j]
            if (j == (numb - 1)):
                if player1 == 1:
                    brPrint = brPrint + ", " + '{0: >3}'.format(str(arr[j])) + ")) = " + str(round(tempF, 2))
                    result[i] = round(tempF, 2)
                else:
                    brPrint = brPrint + ", " + '{0: >3}'.format(str(arr[j])) + "), B" + str(i + 1) + ")) = " + str(round(tempF, 2))
                    result[i] = round(tempF, 2)
                if i == numb - 1:
                    bestr = bestr + ", " + '{0: >3}'.format(str(arr[j])) + ") ="
            elif j == 0:
                brPrint = brPrint + '{0: >3}'.format(str(arr[j]))
                if i == numb - 1:
                    bestr = bestr +'{0: >3}'.format(str(arr[j]))
            else:
                brPrint = brPrint + ", " + '{0: >3}'.format(str(arr[j]))
                if i == numb - 1:
                    bestr = bestr + ", " + '{0: >3}'.format(str(arr[j]))
        if (tempF > max):
            max = round(tempF, 2)
        print (brPrint)
        tempF = 0.00
    for k in range(numb):
        if (max == result[k]):

            if player1 == 1:
                bestr = bestr + " {A" + str(k + 1) + "}"
            else:
                bestr = bestr + " {B" + str(k + 1) + "}"

    print ("\n")
    print ("-------------------------------------------------------")
    print ("Player " + str(player1) + "'s' Best Response with " + str(player2) + " Mixing")
    print ("-------------------------------------------------------")
    print (bestr + "\n")

def pMix(x,b1,b2, player):
    printMix = ""
    temp = 0.00
    b1L= "("
    b2L = "("
    val = 0
    for i in range(rows):
        for j in range(cols):
            val = val + (float(x[i][j]) * b1[j] * b2[i])
            if (i == rows - 1 and j != cols - 1):
                b2L = b2L + str(b2[j]) + ", "
            elif i == rows - 1:
                b2L = b2L + str(b2[j]) + ")"
        if i == rows - 1:
            b1L = b1L + str(b1[i]) + ")"
        else:
            b1L = b1L + str(b1[i]) + ", "
    if player == 1:
        print ("Player 1 -> U (" + str(b2L) + ", " + str(b1L) + ") = " + str(round(val,2)))
    else:
        print ("Player 2 -> U (" + str(b2L) + ", " + str(b1L) + ") = " + str(round(val,2)))

def mixindiff():
    p, p1, q, q1 = 0.0,0.0,0.0,0.0
    p = (float(p2B[1][1]) - float(p2B[1][0])) / (float(p2B[0][0]) - float(p2B[1][0]) + float(p2B[1][1]) - float(p2B[0][1]))
    p1 = float(1 - p)

    q = (float(p1A[1][1]) - float(p1A[0][1])) / (float(p1A[0][0]) - float(p1A[0][1]) + float(p1A[1][1]) - float(p1A[1][0]))
    q1 = float(1 - q)

    print ("-------------------------------------------------------")
    print ("Player 1 & 2 Indifferent Mix Probabilities")
    print ("-------------------------------------------------------")
    print("Player 1 probability of strategies (A1) = " + str(round(p,2)))
    print("Player 1 probability of strategies (A2) = " + str(round(p1,2)))
    print("Player 2 probability of strategies (B1) = " + str(round(q,2)))
    print("Player 2 probability of strategies (B2) = " + str(round(q1,2)))
    print("\n")

#Main
print("Welcome to Nash my EQ!!!!")
nashEQ = 1
while choice != 'e':
    nashEQ = 1
    choice = input("Enter (R)andom or (M)anual payoffs enteries or (E)xit: ")
    #Manual mode
    if choice == 'm':
        rows = int(input("Enter the number of rows:"))
        cols = int(input("Enter the number of cols:"))
        val1A, val1B, val2A, val2B = 1,1,1,1
        p1A = [[0 for i in range(rows)] for j in range(cols)]
        p2B = [[0 for i in range(rows)] for j in range(cols)]
        for i in range(rows):
            val1B, val2B = 1, 1
            for j in range(cols):
                p1A[i][j] = str(input("Enter Player 1's payoff for A" + str(val1A) + " B" + str(val1B) + ": " ))
                val1B = val1B + 1
                p2B[i][j] = str(input("Enter Player 2's payoff for A" + str(val2A) + " B" + str(val2B) + ": " ))
                val2B = val2B + 1
            val1A = val1A + 1
            val2A = val2A + 1
        p1ANash = [[0 for j in range(cols)] for i in range(rows)]
        p2BNash = [[0 for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                p1ANash[i][j] = p1A[i][j]
                p2BNash[i][j] = p2B[i][j]
        p1Strat()
        print ("-------------------------------------------------------")
        print ("Player: Player1's payoffs")
        print ("-------------------------------------------------------")
        payOffs(p1A)
        p2Strat()
        print ("-------------------------------------------------------")
        print ("Player: Player2's payoffs")
        print ("-------------------------------------------------------")
        payOffs(p2B)
        normalForm(p1A,p2B)
        checkEQ(p1ANash, cols, rows, 1)
        checkEQ(p2BNash, rows, cols, 2)
        normalForm(p1ANash, p2BNash)
        nashEQ = printEQ(p1ANash, p2BNash)
        if (nashEQ == 0 and (rows == 2 and cols == 2)):
            mixindiff()

    #Random mode
    elif choice == 'r':
        rows = int(input("Enter the number of rows:"))
        cols = int(input("Enter the number of cols:"))
        p1A = [[0 for j in range(cols)] for i in range(rows)]
        p2B = [[0 for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                p1A[i][j] = str(randint(-99, 99))
                p2B[i][j] = str(randint(-99, 99))
        p1ANash = [[0 for j in range(cols)] for i in range(rows)]
        p2BNash = [[0 for j in range(cols)] for i in range(rows)]
        p1ABel = [0 for j in range(cols)]
        p2BBel = [0 for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                p1ANash[i][j] = p1A[i][j]
                p2BNash[i][j] = p2B[i][j]
        p1Strat()
        print ("-------------------------------------------------------")
        print ("Player: Player1's payoffs")
        print ("-------------------------------------------------------")
        payOffs(p1A)
        p2Strat()
        print ("-------------------------------------------------------")
        print ("Player: Player2's payoffs")
        print ("-------------------------------------------------------")
        payOffs(p2B)
        normalForm(p1A,p2B)
        checkEQ(p1ANash, cols, rows, 1)
        checkEQ(p2BNash, rows, cols, 2)
        normalForm(p1ANash, p2BNash)
        nashEQ = printEQ(p1ANash, p2BNash)
        print("\n")
        randBR(p2B, 2, 1, rows, cols, p2BBel)
        randBR(p1A, 1, 2, cols, rows, p1ABel)
        printBR(p1A, 1, 2, cols, rows, p1ABel)
        printBR(p2B, 2, 1, rows, cols, p2BBel)
        print ("-------------------------------------------------------")
        print ("Player 1 & 2 Expected Payoffs with both Players Mixing")
        print ("-------------------------------------------------------")
        pMix(p1A,p1ABel,p2BBel, 1)
        pMix(p2B,p1ABel,p2BBel, 2)
        print("\n")
        if (nashEQ == 0 and (rows == 2 and cols == 2)):
            mixindiff()


    else:
        print ("Please select one of the three options.")
