# Tax Calculaion

income = 250_000
ripoffland_rate = 0.43
lowtaxland_rate = 0.05

ripoffland_tax = income * ripoffland_rate
lowtaxland_tax = income * lowtaxland_rate
tax_difference = ripoffland_tax - lowtaxland_tax

print(lowtaxland_tax)
print(ripoffland_tax)
print(tax_difference)

print(f"Your income is {income} and you would pay {lowtaxland_tax} income tax in Lowtaxland or {ripoffland_tax} income tax in Ripoffland. You would save {tax_difference} by paying taxes in Lowtaxland!")
print("Your income is " + str(income) + " and you would pay " + str(lowtaxland_tax) + " income tax in Lowtaxland or " + str(ripoffland_tax) + " income tax in Ripoffland. You would save " + str(tax_difference) + " by paying taxes in Lowtaxland!")


# Input practice

print('what is your name?')
user_name = input()
print('Hello', user_name)




