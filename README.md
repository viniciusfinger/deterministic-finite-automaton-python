
# Deterministic Finite Automaton in Python 🐍

Deterministic finite automaton simulator built in Python for the Formal Languages and Automata course at La Salle University.


## Running locally:

Clone the project:

```bash
  git clone git@github.com:viniciusfinger/afd-python.git
```

Access the project folder:

```bash
  cd afd-python
```

Run the main file:

```bash
  python3 main.py
```
## Running on browser:

Access the link bellow and click "Run":

https://replit.com/@FelipeRonzani/AFD-Linguagens-Formais-e-Automatos

## How to use:

After running, just fill in the information requested by the console

You must insert the automaton states into this pattern, according to the number of states you need, following the pattern s{number of state}:

```bash
  s0 s1 s2 s3
```

Then, insert the alphabet characters into this pattern, however you want:

```bash
  a b c d
```

When asked to complete the sentence with the next state, you must enter next state for that value or a period (.) when there is no next state.

The number above the arrow is the value read by the tape, the state on the left is the current state and the state on the right (which you must fill in) is where it will go.

```bash
    0
s0 ---> (coloque o estado que irá quando estiver em s0 e a fita ler 0, ou ponto (.) caso não haja transição)
```

At the end, the program will request a word to be validated in the automaton.

Se for válida, printará "Palavra aceita pelo autômato". Caso contrário, printará "Palavra rejeitada pelo autômato".
