test_list = [(1, 5), (4, 3), (8, 15), (7, 6)]
  
print ("The original list is : " + str(test_list))
  
res1 = min(test_list)[0], max(test_list)[0]
res2 = min(test_list)[1], max(test_list)[1]
  
print ("The min and max of index 1 :  " +  str(res1))
print ("The min and max of index 2 :  " +  str(res2))
