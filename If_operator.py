Weight_in_Kgs = input("What is the weight (kgs): ")
Height_in_cms = input("What is your height (cms): ")
H_in_inches = float(Height_in_cms) / 2.54
W_in_pounds = float(Weight_in_Kgs) / 0.453592
# print(W_in_pounds)
# print(H_in_inches)
sqr_H = (H_in_inches) * (H_in_inches)
BMI = 703 * (W_in_pounds / (sqr_H))
print("Your BMI is : "+ str(BMI))
if( float(BMI) < 18.5 ):
    result = "UnderWeight"
elif(float(BMI) < 24.9 ):
    result = "NormalWeight"
elif (float(BMI) < 29.9):
    result = "OverWeight"
else:
    result = "Obesity"
##print ("Hey dear! your are " + str(int( W_in_pounds)), "lbs and " + str(int(H_in_inches)), "inchs,", "This shows you are "+ result )
print(f"Hey dear! your are {int(W_in_pounds)} pounds and {int(H_in_inches)} inchs, This shows you are {result}")
