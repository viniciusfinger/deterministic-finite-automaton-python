from state import State


def get_destination_state(destination_state_id, states):
    for state in states:
        if state.id == destination_state_id:
            return state

def validate_initial_state(initial_state):
    if initial_state == "":
        print("Autômato inválido, nenhum estado inicial definido.")
        exit()

def validate_final_states(final_states):
    have_final_state = False

    for state in final_states:
        if state.is_final == True:
            have_final_state = True
            break

    if have_final_state == False:
        print("Autômato inválido, nenhum estado final definido.")
        exit()

def validate_valid_state(states, state_id):
    for state in states:
        if state_id == state.id:
            return True

    print("Estado inválido, não foi informado na etapa de inserir os estados.")
    exit()

states = []
start_state = ""
initial_state = ""
transitions = {}

print("Simulador de automato finito nao-deterministico.")

print("Insira os estados do autômato separados por espaço: ", end="")
raw_states_id = input().split()
for state_id in raw_states_id:
    states.append(State(state_id))

print("Digite os caracteres do alfabeto separados por espaço: ", end="")
alphabet = input().split()

print("Insira o estado inicial do autômato: ", end="")
initial_state_id = input()
validate_valid_state(states, initial_state_id)


print("Insira os estados finais do autômato separados por espaço: ", end="")
final_states_id = input().split()
for final_state_id in final_states_id:
    validate_valid_state(states, final_state_id)

for state in states:
    if state.id == initial_state_id:
        state.is_initial = True
        initial_state = state
    
    if state.id in final_states_id:
        state.is_final = True

validate_initial_state(initial_state)
validate_final_states(states)

print("Complete a sentença com o próximo estado de acordo com o caracter (digite um . se não houver transição.)")

for state in states:
    for character in alphabet:
        print(f"\t  {character}")
        print(f"{state.id}\t---->\t", end="")
        destination_state_id = input()
        
        if destination_state_id == ".":
            transitions[(state, character)] = None
        else:
            destination_state = get_destination_state(destination_state_id, states)
            transitions[(state.id, character)] = destination_state
            
print("Insira uma palavra para ser validada no autônomo: ", end="")
input_word = input()

current_state = initial_state

for character in input_word:
    current_state = transitions[(current_state.id, character)]
    
    if current_state is None:
        print("Palavra rejeitada pelo autônomo.")
        break
    
if (current_state.is_final):
    print("Palavra aceita pelo autônomo.")
else:
    print("Palavra rejeitada pelo autônomo.")
