# dataMax
Contact Details:
Blerta Kola
blertakola4@gmail.com


My algorithm:
ugjet variable is set initially to -1. Then we have a for loop with three iterations representing the number of the digits of the missing numbers. For each iteration 
we have two tracking variables one for the index and one for the length of the number. Then we have a while loop with a condition j < len(string we inputed).
prev variable is set to the value of the sliced string from j - step_size to j, new_step is equal to the length of the prev variable. current variable is set to the 
value of the sliced string from j to j + new_step. Then we check if the difference between current and prev is equal to one. If is equal to one we assign the value 
of new_step to step and increment the value of j with the value of step. If not true we set the ugjet value to current - 1. We have another condition we check if
the value of ugjet has changed (we have found a missing number) or there is a gap between them which means that there is a gap between them and theres 
no missing number. We break the loop. 


Time complexity:
This algorithm has two nested loops. The outer loops runs in constant time. The while loop in the worst case 
scenario runs in O(n) time where n is the length of the inputed string. Since the inner loop can iterate up to n times for each iteration of the outer loop, I
think the time complexity for this algorithm is O(3*n) = O(n^2)
