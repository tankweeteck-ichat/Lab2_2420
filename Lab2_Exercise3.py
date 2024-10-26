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



def calc_average(inputlist):
    print("calc_average")


def find_min_max(inputlist):
    print("find_min_max")


def sort_temperature(inputlist):
    print("sort_temperature")


def calc_median_temperature(inputlist):
    print("calc_median_temperature")


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)



if __name__ == "__main__":
    main()

