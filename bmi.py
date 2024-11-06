def calculate_bmi(height, weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))

    # Calculate the BMI
    bmi = weight/(height**2)
    print("BMI =", round(bmi,2))

    # Print the Weight Classification
    print("Weight Classification = ", end="")  # Use the end="" to suppress the newline
    if bmi<18.5:
        print("Under Weight")
        return -1
    elif bmi>25.0:
        print("Over Weight")
        return 1
    else:
        print("Normal Weight")
        return 0

result = calculate_bmi(weight=37, height=1.73)
print("Result = ", result)
result = calculate_bmi(weight=57, height=1.73)
print("Result = ", result)
result = calculate_bmi(weight=97, height=1.73)
print("Result = ", result)
