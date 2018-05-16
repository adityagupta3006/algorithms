// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public String solution(int N, String S, String T) 
    {
        String ships[] = S.split(","); // splitting ships and storing in ships array
        
        // creating HashMap for ship number and ship locations
        HashMap<Integer, HashSet<String>> shipMap = new HashMap<>(); 
        
        String target[] = T.split(" "); // splitting targets
        
        int hitCount = 0;  // maintaining hit count
        int sunkCount = 0; // maintaining sunk count
        
        // Populating ship map by start and end locations
        for(int i = 0; i < ships.length; i++)
        {
            shipMap.put(i, getShipLocations(ships[i]));
        }
        
        // checking whether the ship is hit or sunk
        for(HashSet<String> shipLocations : shipMap.values())
        {
            boolean isShipHit = false;
            for(String hit : target)
            {
                if(shipLocations.contains(hit))
                {
                    shipLocations.remove(hit);
                    isShipHit = true;
                }
            }
            if(shipLocations.size() == 0)
            {
                sunkCount += 1;
            }
            else if(isShipHit)
            {
                hitCount += 1;   
            }
        }
        return Integer.toString(sunkCount) + "," + Integer.toString(hitCount);
        
    }   
    
    /* this function takes start and input locations as string 
        returns a HashSet of all the ship locations
    */
    public HashSet<String> getShipLocations(String ship)
    {   
        // if only location is entered instead of start and end locations
        if(!ship.contains(" ")) 
            return new HashSet<String>(Arrays.asList(ship));
        
        // populating HashSet to store all locations covered by the ship
        HashSet<String> shipLocationSet = new HashSet<>();
        String startLocation = ship.split(" ")[0];
        String endLocation = ship.split(" ")[1];
        
        int startRow = Integer.parseInt(startLocation.substring(0,startLocation.length()-1));
        char startColumn = startLocation.charAt(startLocation.length()-1);        
        
        int endRow = Integer.parseInt(endLocation.substring(0,endLocation.length()-1));
        char endColumn = endLocation.charAt(endLocation.length()-1);
        
        // finding out the locations
        for(int i=startRow; i<= endRow; i++)
        {
            for(char j = startColumn; j<= endColumn; j++)
            {
             shipLocationSet.add(Integer.toString(i) + Character.toString(j));   
            }
        }
        return shipLocationSet;
    }
}