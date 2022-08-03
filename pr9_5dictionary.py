from collections import Counter
  
# Initial Dictionary
my_dict = {'A': 12, 'B': 23, 'C': 37, 
           'D': 49, 'E': 59, 'F': 73}
  
k = Counter(my_dict)
  
# Finding 3 highest values
high = k.most_common(3) 
  
print("Initial Dictionary:")
print(my_dict, "\n")
  
  
print("Dictionary with 3 highest values:")
print("Keys: Values")
  
for i in high:
    print(i[0]," :",i[1]," ")
