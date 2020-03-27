#This script is used to calculate the economic useful life of a assets
#Author: Osvaldo Fernández

#######################################################
#####################Factors Functions#################
#######################################################
def aGivenP(i: float, n: int) -> float:
    return (i * (1 + i) ** n )/( (1 + i) ** n - 1 )

def aGivenF(i: float, n: int) -> float:
    return i/( (1 + i) ** n - 1 )

def pGivenF(i: float, n: int) -> float:
    return 1/( (1 + i) ** n )
#######################################################
#######################################################
#######################################################

#######################################################
#######################SCRIPT##########################
#######################################################

#Interest rate
interest = 0.10

#Initial Cost
P = 13000

#Commercial values
VC = [9000, 8000, 6000, 2000, 0]

#Annual cost of operation
CAO = [2500, 2700, 3000, 3500, 4500]

#Years of studies
N = len(VC)

#Anual values
VA = []

#Minimal anual value
minVA = -P

#Year with minimun anual value
utilLifeYears = 0

for k in range(N):
    #Annual operating cost at year zero
    VCAO = 0
    for j in range(k + 1):
        VCAO = VCAO + CAO[j] * pGivenF(interest, j + 1)
    
    #Formula for VA
    VAaux = -P * aGivenP(interest, k + 1) + VC[k] * aGivenF(interest, k + 1) - VCAO * aGivenP(interest, k + 1)

    #Adding to annual values VA
    VA.append(round(VAaux, 2))

    #Checking if it is the year with the lowest VA (VUE)
    if abs(VAaux) <= abs(minVA):
        minVA = abs(VAaux)
        utilLifeYears = k + 1

#Results
print("Anual values = " + str(VA))
print("Economic useful life = " + str(utilLifeYears) + " years")