messages = ['Olá, boa tarde!', 'Olá, bom dia!', 'Olá, boa noite!']
new_messages = []

def show_messages(msgs):
   for msg in msgs:
        print(msg)
    

def send_messages(msgs):
    print('Passando para a outra lista: ')
    while messages:
        writing_message = messages.pop()
        
        new_messages.append(writing_message)


print('Primeira lista: ')
show_messages(messages)

send_messages(messages)

print('\nSegunda lista: ')
show_messages(new_messages)

print('\nPrimeira lista vazia:')
print (messages)
