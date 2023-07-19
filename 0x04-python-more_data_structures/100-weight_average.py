#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        first_av = 0
        second_av = 0
        third_av = 0

        for item in my_list:
            first_av += item[0] * item[1]
            second_av += item[0]
            third_av += item[1]

        if third_av == 0:
            return 0
        else:
            average = first_av / third_av
            return average
