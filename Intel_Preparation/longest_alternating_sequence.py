
#Implement a function that given an integer array and its length, returns the #length of the longest sequence of alternating odd and even numbers. For #instance, in the array 112365546, it will return 5 (for the sequence 12365)

array = [1,1,2,3,6,5,5,4,6]
sequential_count = [1]; # Base case is only 1 

count = 1
for i in range(1, len(array)):
  curr = array[i];
  prev = array[i-1];

  if (curr % 2 == 0 and prev % 2 == 1):
    count += 1
  elif(curr % 2 == 1 and prev % 2 == 0):
    count += 1
  else:
        sequential_count.append(count)
        count = 1

seq_len = max(sequential_count)

print('Longest sequence of alternating odd and even numbers is: ' + str(seq_len))
