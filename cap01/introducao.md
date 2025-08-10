
### Anotações – Algoritmo de Ranking por Popularidade e Centralidade de Grau

## 1. Conceito de Centralidade de Grau

**Definição:** Medida que indica quantas conexões diretas (arestas) um nó possui em um grafo.

**Aplicação:** Identificar os nós mais “populares” ou “conectados” em uma rede.

**Fórmula Normalizada:**

```
𝐶_𝐷(𝑖) = 𝑘_𝑖 / (𝑛 − 1)
```

Onde:
* `𝑘_𝑖` = número de conexões diretas do nó `𝑖`
* `𝑛` = número total de nós na rede

Valor varia de 0 a 1.

## 2. Estrutura da Rede no Algoritmo

Cada usuário é um nó (vértice).

Cada amizade é uma aresta bidirecional.

Rede representada por:

* Lista de usuários (`users`)
* Lista de pares de amizade (`friendship_pair`)
* Dicionário de listas (`friendships`), mapeando id → [amigos].

## 3. Passos do Algoritmo

### Construir a rede

* Criar um dicionário `friendships` com uma lista de amigos para cada usuário.
* Preencher as listas de amigos a partir de `friendship_pair`.

### Função para calcular o grau

```python
def number_of_friends(user):
    return len(friendships[user["id"]])
```

Retorna a quantidade de amigos (grau) de um usuário.

### Estatísticas globais

* **Total de conexões:** soma dos graus de todos os usuários.
* **Média de conexões:** total de conexões dividido pelo número de usuários.

### Ranking por Popularidade

* Criar lista de tuplas (`id_usuario`, `grau`).
* Ordenar em ordem decrescente pelo grau.
* Exibir o ranking.

## 4. Interpretação

Usuários no topo do ranking possuem maior centralidade de grau.

**Alta centralidade de grau** → maior capacidade de influenciar diretamente outros na rede.

Não considera caminhos indiretos (isso é abordado em outras métricas como betweenness e closeness).

## 5. Observações

* Em grafos direcionados, diferenciar grau de entrada (`in-degree`) e grau de saída (`out-degree`).
* O exemplo implementado é não direcionado (amizade é recíproca).
* Centralidade de grau é simples de calcular, mas não mede a posição estratégica do nó na rede, apenas seu número de conexões diretas.

