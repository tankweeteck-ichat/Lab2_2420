# ET0735 Lab 2 - Exercise 2
# print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    print("get_user_input")
    inputstr = input()
    strlist = inputstr.split(",")
    #print(strlist)
    floatlist = []
    for x in strlist:
        floatlist.append(float(x))
    #print(floatlist)
    return floatlist



def calc_average(float_list):
    print("calc_average")
    average = sum(float_list) / len(float_list)
    print("Average:", average)
    return average



def find_min_max(float_list):
    print("find_min_max")
    float_list.sort()
    return [float_list[0], float_list[-1]]



def sort_temperature(inputlist):
    print("sort_temperature")
    inputlist.sort()
    print("Sorted = ", inputlist)
    return inputlist


def calc_median_temperature(sortedlist):
    print("calc_median_temperature")
    cnt = len(sortedlist)
    print("cnt=", cnt)
    if cnt%2 == 1:  # No. of elements i list is odd.
        median = sortedlist[cnt//2]   # // is Integer Division
    else:
        median = (sortedlist[cnt//2 - 1] + sortedlist[cnt//2])/2
    print("Median = ", median)



def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    average = calc_average(num_list)
    min_max_list = find_min_max(num_list)
    print(min_max_list)
    sorted_list = sort_temperature(num_list)
    calc_median_temperature(sorted_list)


if __name__ == "__main__":
    main()

