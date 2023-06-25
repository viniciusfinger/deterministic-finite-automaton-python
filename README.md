
# Autômato Finito Determinístico em Python 🐍

Simulador de autômato finito determinístico construído em Python para a cadeira de Linguagens Formais e Autômatos da Universidade La Salle.


## Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:viniciusfinger/afd-python.git
```

Entre no diretório do projeto

```bash
  cd afd-python
```

Rode o arquivo principal

```bash
  python3 main.py
```
## Outra forma de rodar o código no navegador:

Acesse o link abaixo e clique em "Run"

```bash
  https://replit.com/@FelipeRonzani/AFD-Linguagens-Formais-e-Automatos
```
## Instruções de uso:

A partir de agora é só preencher as informações solicitadas pelo console.

Você deverá inserir os estados do autômato nesse padrão, de acordo com a quantidade de estados que necessitar:

```bash
  s0 s1 s2 s3
```

E os caracteres do alfabeto nesse padrão, de acordo com o que desejar:

```bash
  a b c d
```

Quando solicitado para completar a sentença com o próximo estado, deverá inserir próximo estado para aquele valor ou um ponto (.) quando não houver próximo estado.

O número acima da seta é o valor lido pela fita, o estado à esquerda é o estado atual e o estado à direita (que você deve preencher) é para onde irá.
```bash
    0
s0 ---> (coloque o estado que irá quando estiver em s0 e a fita ler 0, ou ponto (.) caso não haja transição)
```

No final, o programa solicitará uma palavra para ser validada no autômato. 

Se for válida, printará "Palavra aceita pelo autômato". Caso contrário, printará "Palavra rejeitada pelo autômato".
