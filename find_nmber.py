for num in range(10000,44444):
    frequency = {0:0,1:0,2:0,3:0,4:0}
    number = str(num)
    for i in range(5):
        if int(number[i]) not in frequency:
            frequency[int(number[i])] = 1
        else:
            frequency[int(number[i])] += 1
    if int(number[0]) == frequency[0] and \
                    int(number[1]) == frequency[1] and \
                    int(number[2]) == frequency[2] and \
                    int(number[3]) == frequency[3] and \
                    int(number[4] )== frequency[4]:
        print number
        break



