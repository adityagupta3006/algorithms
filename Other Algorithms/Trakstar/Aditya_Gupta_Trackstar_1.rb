=begin
Author	-	Aditya Gupta
email	-	agupta42@uncc.edu

Write a Ruby method that prints numbers from 1 to 100; 
except for multiples of three print "Trak", 
multiples of five print "Star", 
and multiples of both three and five print "Trakstar".	
=end

def trackstar(count)
  	for i in 1..count
  	  	# printing Trackstar if i is a multiple of 3 and 5
  	  	if i%3 == 0 && i%5 == 0
  	    	puts 'Trakstar'
  	    # printing Trackstar if i is a multiple of 3 
  	  	elsif i%3 == 0
  	    	puts 'Trak'
  	    # printing Trackstar if i is a multiple of 5
  	  	elsif i%5 == 0
  	    	puts 'Star'
  	 	end 
  	end
end

count = 100
trackstar(count)