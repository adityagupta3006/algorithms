# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, S, T):
    # splitting ships and storing in ships array
    ships = S.split(',')
    shipMap = {}
    target = T.split(' ')
    hitCount = 0
    sunkCount = 0
    
    for shipNumber, ship in enumerate(ships):
        shipMap[shipNumber] = getShipLocations(ship)
   
    
    for shipLocations in shipMap.values():
        isShipHit = False
        for hit in target:
            if hit in shipLocations:
                shipLocations.remove(hit)
                isShipHit = True
        if len(shipLocations) == 0:
            sunkCount += 1
        elif isShipHit:
            hitCount += 1
            
    return (str(sunkCount) + ',' + str(hitCount)) 
            

# function to get ship cells 
def getShipLocations(ship):
    
    shipLocationSet = set()
    
    startLocation = (ship.split(' ')[0])
    endLocation = ship.split(' ')[1]
    
    startRow = int(startLocation[:-1])
    startColumn = ord(startLocation[-1])

    endRow = int(endLocation[:-1])
    endColumn = ord(endLocation[-1])
    
    #print(startRow, startColumn, ' - ', endRow, endColumn)
    
    for i in range(startRow, endRow+1):
        for j in range(startColumn, endColumn+1):
            shipLocationSet.add(str(i) + chr(j))
    return shipLocationSet            
    