def multiplicatio_or_sum(num1,num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2


result = multiplicatio_or_sum(20,30)
print("The result is :", result)

result = multiplicatio_or_sum(40,30)
print("The result is :", result)
