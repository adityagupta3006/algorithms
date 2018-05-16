=begin
Author	-	Aditya Gupta
email	-	agupta42@uncc.edu

Write a Ruby method that determines 
if two words are anagrams of each other.	
=end

def isAnagram(firstWord, secondWord)
	# check if the lengths are not equal
	return false if firstWord.length != secondWord.length

	histogram = Array.new ASCII_COUNT, 0
	# iterate through the first word
	firstWord.length.times do |i|
		histogram[[i].ord] += 1
		histogram[other[i].ord] -= 1
	end
	histogram.any? { |count| count != 0 }
end

isAnagram("iceman","cinema")