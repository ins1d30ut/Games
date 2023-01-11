age = input("how old are you? ")
age = int(age)

if age > 18:
  print("\nYou're too old to start to learn to code FOO!")
else:
  print("\nYou'll be able to learn pyThonG one day!")

prompt = "\nIf you can't learn python yet, which language would you like to learn instead? "
prompt += "\n\n(Enter 'q' when you are finished.)\n "

while True:
  language = input(prompt)

  if language == 'q':
    break
  else:
    print(f"You really want to do that {language.title()}!? If so, you whack dawg!")