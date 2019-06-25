from itertools import product

def readInputs(qtdClau):
    inputs = []
    for i in range(qtdClau):
        var = input("Clausula {}: ".format(i + 1)).split()
        inputs.append(var)
    return inputs

def readClauses(inputs):
    clauses = []
    for i in range(len(inputs)):
        adClau = []
        for j in inputs[i]:
            if(j == '0'):
                break
            elif(j != ' '):
                adClau.append(j)
        clauses.append(adClau)
    return clauses

def readVariables(clauses,qtdVar):
    variables = []
    for i in range(qtdVar):
        variables.append(False)
    return variables

def readFormula():
    qtd = input().split()
    inputs = readInputs(int(qtd[3]))
    clauses = readClauses(inputs)
    variables = readVariables(clauses,int(qtd[2]))
    result = {'clauses':clauses, 'variables':variables}
    return result

def nextAssignment(currentAssignment, total):
    string = ''
    for i in range(len(currentAssignment)):
        if(currentAssignment[i] == True):
            currentAssignment[i] = '1'
            print(currentAssignment)
        else:
            currentAssignment[i] = '0'
            print(currentAssignment)

    for i in range(len(currentAssignment)):
        string = string + currentAssignment[i]

    decimal = int(string,2)
    print(decimal)
    decimal += 1
    print(decimal)
    string = bin(decimal)[2:].zfill(len(currentAssignment))
        
    for i in range(len(string)):
        if(int(string[i]) > 0):
            currentAssignment[i] = True
        else:
            currentAssignment[i] = False

    return currentAssignment

def doSolve(clauses, assignment):
    isSat = False
    formula = []
    total = 0

    while (not isSat and 2 ** len(assignment)):
        formula = []

        for i in range(len(clauses)):
            for j in range(len(clauses[i])):
                if(int(clauses[i][j]) < 0):
                    assignment[int(clauses[i][j])] = not assignment[int(clauses[i][j])]

        print(assignment)
                    
        for i in range(len(clauses)):
            adFor = False
            for j in range(len(clauses[i]) - 1):
                if(assignment[abs(int(clauses[i][j])) - 1] or assignment[abs(int(clauses[i][j + 1])) - 1] == True):
                    adFor = True
                    break
            formula.append(adFor)
        print("Formula {}".format(total + 1), formula)

        for k in range(len(formula) - 1):
            if(formula[k] == False):
                isSat = False
                break
            elif(formula[k] and formula[k + 1] == True):
                isSat = True

        if(isSat == False): 
            assignment = nextAssignment(assignment,total)
        print(assignment)
        total += 1

    result = {'isSat': isSat, 'satisfyingAssignment': None}

    if (isSat):
        result['satisfyingAssignment'] = assignment

    return result

def solve():
    formula = readFormula()
    result = doSolve(formula['clauses'], formula['variables'])
    return result

print(solve())
