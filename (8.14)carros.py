def car(manufacturer, model, **args):
    args['fabricante'] = manufacturer
    args['modelo'] = model
    return args

new_car = car('fiat', 'siena',
              cor='branco',
              radio='possui')

print(new_car)

