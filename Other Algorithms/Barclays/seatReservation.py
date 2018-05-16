# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict

def solution(N, S):
    emptySeats = 3* int(N)  # total empty seats
    
    # edge case
    if S == '':
        return emptySeats
    
    seatsBooked = S.split(' ')   # split input
    seatsMap = defaultdict(list) # define a seatsMap 
    
    # get all seats booked in a row
    for seatBooked in seatsBooked:
        seatsMap[seatBooked[:-1]].append(seatBooked[-1])
    
    # update empty seat count 
    for seatRowNumber in seatsMap.keys():
        occupiedSeats = seatsMap[seatRowNumber]
        
        # check if A or B or C is in the occupied seats
        if('A' in occupiedSeats or 'B' in occupiedSeats or 'C' in occupiedSeats):
            emptySeats -= 1
        
        # check if E or F or D and G is in the occupied seats
        if('E' in occupiedSeats or 'F' in occupiedSeats or ('D' in occupiedSeats and 'G' in occupiedSeats)):
            emptySeats -= 1

        # check if H or J or K is in the occupied seats    
        if('H' in occupiedSeats or 'J' in occupiedSeats or 'K' in occupiedSeats):
            emptySeats -= 1
            
    return emptySeats