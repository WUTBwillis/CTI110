#calculate salary
#1)ask user to enter pay rate
payRate= float(input("How much do you get paid per hour?"))

#2)ask user to enter hours worked
hoursWrkd= float(input("How many hours did you work?"))

#3)evaluate (decision) hours worked, if>40, calculate overtime hours
if hoursWrkd > 40:
    overtime = hoursWrkd-40
    overPay = (overtime * payRate) * 1.5
    regPay = 40 * payRate
    grossPay = hoursWrkd + regPay
else:
    grossPay = hoursWrkd * payRate

print("your gross pay is $", grossPay, sep="")

#3.1- overtime=(payrate*(hours worked(or)-40)*1.5
#3.2- calculate how much paid for regular 40 hours
#3.3- add 3.1+3.2=gross pay
#4)if they have done overtime
#4.1- gross pay = hours worked * payrate
