age = input("how old are you? ")
age = int(age)

if age > 18:
  print("\nYou're old enough to smoke crack!")
else:
  print("\nYou'll be able to smoke crack one day!")

prompt = "\nIf you can't smoke crack yet, which drug would you like to do instead? "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
  drug = input(prompt)

  if drug == 'quit':
    break
  else:
    print(f"You really want to do that {drug.title()}!?")