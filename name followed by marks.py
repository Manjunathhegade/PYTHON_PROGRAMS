def SSLC_mark():
    list=[]
    list1 = []
    list2 = []
    list3 = []
    while True:
        student_marks = input("enter your name with total marks\n")
        if student_marks == " ":
            break
        else:
            list.append(student_marks)
    
    for item in list:
        item = int(item[-2:])
        if item >= 90 and item <= 100:
            list1.append(item)


    for item1 in list1:
        item1 = str(item1)
        list2.append(item1)

    for item2 in list:
        for item3 in list2:
            if item3 in item2:
                list3.append(item2)
        
    return list3

print(SSLC_mark())
