# Start with some designs that need to be printed.
unprinted_designs = ['farmer dildo', 'rabbit dildo', 'roger rabbidildo']
completed_models = []
# Move each design to completed_models aka pop from unprinted to completed list/array
while unprinted_designs:
  current_design = unprinted_designs.pop()
  print(f"Printing model: {current_design}")
  completed_models.append(current_design)
# Show 'appended' models in completed_model list/array
print("\nThe following models have been printed:")
for completed_model in completed_models:
  print(completed_model)