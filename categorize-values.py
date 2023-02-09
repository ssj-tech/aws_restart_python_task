myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    item2 = type(item)
    print(f"{item} is of the data type {item2}")
#Another way of writing the code using     
    myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print(f"{item} is of the data type {type(item)}")
#Another way of writing the code using     
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))

a = "good"
b = 456
print(f"{a} {b}")
