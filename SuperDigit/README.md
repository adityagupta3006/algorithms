# Recursive Digit Sum.
We define super digit of an integer  using the following rules:

* If  has only  digit, then its super digit is x.
* Otherwise, the super digit of x is equal to the super digit of the digit-sum of x. 
Here, digit-sum of a number is defined as the sum of its digits.

For example, super digit of 9875 will be calculated as:<br />
super_digit(9875) = super_digit(9+8+7+5) <br />
                  = super_digit(29)   <br />
                  = super_digit(2+9)  <br />
                  = super_digit(11)   <br />
                  = super_digit(1+1)  <br />
                  = super_digit(2)    <br />
                  = 2.

[HackerRank Link](https://www.hackerrank.com/challenges/recursive-digit-sum/problem)
