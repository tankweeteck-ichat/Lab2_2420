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
    elif bmi>25.0:
        print("Over Weight")
    else:
        print("Normal Weight")

calculate_bmi(weight=57, height=1.73)
