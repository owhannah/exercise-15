# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp

def exponent(base, exp):
    result = 1

    for _ in range(exp):
        result *= base

    return result

# Display the case 1 and case 2 example:
case_1, exp_1 = 2, 5
result_1 = exponent(case_1, exp_1)
print(f"{case_1} raise to the power of {exp_1}: {result_1}")

case_2, exp_2 = 5, 4
result_2 = exponent(case_2, exp_2)
print(f"{case_2} raise to the power of {exp_2}: {result_2}")