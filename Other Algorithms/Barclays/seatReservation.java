// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int N, String S) {
        int emptySeats = 3*N;
        String occupiedSeats;
        
        // Edge case
        if(S.isEmpty())
            return emptySeats;
            
        String seatsBooked[] = S.split(" ");
        HashMap<Integer, String> seatsMap = new HashMap<>();
        
        String leftColumn[] = new String[]{"A","B","C"};
        String centerColumn[] = new String[]{"E","F","D", "G"};
        String rightColumn[] = new String[]{"H","J","K"};
        
        // Check all seats booked in aa row
        for (String seatBooked : seatsBooked)
        {
            int len = seatBooked.length();
            String column = seatBooked.substring(len - 1);
            Integer row = Integer.valueOf(seatBooked.substring(0, len - 1));
            
            if (seatsMap.containsKey(row))
            {
                seatsMap.put(row, column + seatsMap.get(row));
            }
            else
            {
                seatsMap.put(row, column);
            }
        }
        
        // Update the empty seat count
        for (Integer seatRowNumber : seatsMap.keySet())
        {
            occupiedSeats = seatsMap.get(seatRowNumber);
            
            // Check if A or B or C is in occupied seats
            if (occupiedSeats.contains(leftColumn[0]) || occupiedSeats.contains(leftColumn[1]) || occupiedSeats.contains(leftColumn[2]))
            {
                emptySeats -= 1;
            }
            
            // Check if E or F or (D and C) is in occupied seats
            if (occupiedSeats.contains(centerColumn[0]) || occupiedSeats.contains(centerColumn[1]) || (occupiedSeats.contains(centerColumn[2]) && occupiedSeats.contains(centerColumn[3])))
            {
                emptySeats -= 1;
            }
            
            // Check if H or J or K is in occupied seats
            if (occupiedSeats.contains(rightColumn[0]) || occupiedSeats.contains(rightColumn[1]) || occupiedSeats.contains(rightColumn[2]))
            {
                emptySeats -= 1;
            }
            
        }
        return emptySeats;
    }
}