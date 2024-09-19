def print_models(unprinted_designs, completed_model):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_model.append(current_design)

def show_completed_models(completed_models):
    print (f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print (completed_model)