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
    qtd = (input().split())
    inputs = readInputs(int(qtd[2]))
    clauses = readClauses(inputs)
    variables = readVariables(clauses,int(qtd[3]))
    result = {'clauses':clauses, 'variables':variables}
    return result

def nextAssignment(currentAssignment):
    nextAssignment = []
    return nextAssignment

def doSolve(clauses, assignment):
    isSat = False
    formula = []
    total = 0
    while (not isSat) or (total < 2 ** len(assignment)):
        for i in range(len(clauses)):
            adFor = [False]
            for j in range(len(clauses[i]) - 1):
                if(assignment[clauses[i][j] - 1] or assignment[(clauses[i][j + 1]) - 1] == True):
                    adFor[0] = True
                    break
            formula.append(adFor)

        for k in range(len(formula) - 1):
            if(formula[k] == False):
                break
            elif(formula[k] and formula[k + 1] == True):
                isSat = True

        if(isSat == False): 
            assignment = nextAssignment(assignment)

        total += 1

    result = {'isSat': isSat, 'satisfyingAssignment': None}
    if (isSat):
        result['satisfyingAssignment'] = assignment

    return result

def solve():
    formula = readFormula()
    result = doSolve(formula['clauses'], formula['variables'])
    return result