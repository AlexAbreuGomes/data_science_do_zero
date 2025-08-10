# Explicação Detalhada do Código: introducao.py

Este documento explica, de forma didática, cada parte do script `introducao.py`, que modela uma pequena rede social e calcula estatísticas simples sobre conexões (amizades) entre usuários.

---

## 1. Visão Geral

O objetivo do código é:

- Representar usuários de uma rede social.
- Registrar amizades (relações bidirecionais).
- Calcular métricas como total de conexões e média de amigos.
- Gerar um ranking de usuários mais conectados.
- Identificar amigos de amigos (FOAF) para sugestões.
- Mapear e comparar interesses entre usuários.

---

## 2. Estrutura dos Usuários (`users`)

Uma lista de dicionários, cada dicionário representa um usuário:

```python
users = [
    {"id": 0, "name": "hero"},
    {"id": 1, "name": "dunn"},
    # ...
]
```

Campos:

- `id`: identificador único (int)
- `name`: nome do usuário (str)

Por que usar lista de dicionários? Simplicidade e legibilidade em exemplos introdutórios.

---

## 3. Lista de Amizades (`friendship_pair`)

Par de inteiros indicando uma amizade mútua:

```python
friendship_pair = [ (0, 1), (0, 2), (1, 2), ... ]
```

Cada tupla (A, B) significa que A é amigo de B e B é amigo de A (grafo não direcionado).

---

## 4. Construindo a Estrutura de Adjacência (`friendships`)

Criação do dicionário onde cada chave (id) mapeia para a lista de amigos:

```python
friendships = {user["id"]: [] for user in users}
for i, j in friendship_pair:
    friendships[i].append(j)
    friendships[j].append(i)
```

Isso produz algo como:

```python
{ 0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], ... }
```

Essa é a representação típica de um grafo via lista de adjacência.

---

## 5. Função `number_of_friends`

Responsável por calcular o grau (número de conexões diretas) de um usuário:

```python
def number_of_friends(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)
```

Abstrai a lógica de consulta ao dicionário e melhora a reutilização.

---

## 6. Cálculo de Métricas Globais

```python
total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users
```

Explicação:

- `total_connections`: soma dos graus (cada amizade é contada duas vezes em grafos não direcionados — uma por extremidade).
- `num_users`: quantidade de nós.
- `avg_connections`: média simples de amigos por usuário.

Obs.: Se quiser o número de arestas únicas, poderia usar `total_connections / 2`.

---

## 7. Exibição das Estatísticas

```python
print(f"Total connections: {total_connections}")
print(f"Average connections per user: {avg_connections:.2f}")
```

Formato amigável para leitura e inspeção.

---

## 8. Ranking de Popularidade

Lista com (id, número_de_amigos) e ordenação decrescente:

```python
num_friends_by_id = [ (user["id"], number_of_friends(user)) for user in users ]
num_friends_by_id.sort(key=lambda t: t[1], reverse=True)
print(num_friends_by_id)
```

- `list comprehension`: gera a lista de tuplas.
- `sort` com `key=lambda t: t[1]`: ordena pelo segundo elemento (quantidade de amigos).
- `reverse=True`: maior primeiro.

Exemplo de saída:

```
[(1, 3), (2, 3), (5, 3), (0, 2), (3, 2), ...]
```

---

## 9. Conceitos de Grafos Envolvidos

| Conceito              | Aplicação no Código                       |
| --------------------- | ----------------------------------------- |
| Nó (vértice)          | Usuário (dicionário)                      |
| Aresta (não dirigida) | Par de amizade (tupla)                    |
| Lista de adjacência   | Dicionário `friendships`                  |
| Grau do nó            | Número de amigos (`len(friendships[id])`) |
| Centralidade de Grau  | Ranking por número de amigos              |

---

## 10. Amigos de Amigos (FOAF)

### Função `foaf_ids_bad`

Retorna uma lista com possíveis duplicações e inclui amigos existentes.

```python
def foaf_ids_bad(user):
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]
```

Limitações: inclui o próprio usuário, amigos atuais e duplicatas.

### Função `friends_of_friends`

```python
def friends_of_friends(user):
    return Counter(
        foaf_id
        for friend_id in friendships[user["id"]]
        for foaf_id in friendships[friend_id]
        if foaf_id != user["id"] and foaf_id not in friendships[user["id"]]
    )
```

Retorna potenciais novos amigos com contagem de amigos em comum.

Uso típico: sistema de recomendação simples baseado em conexões de 2º nível.

---

## 11. Interesses dos Usuários

Lista de tuplas `(id_usuario, interesse)`:

```python
interests = [ (0, "Hadoop"), (0, "Big Data"), ..., (9, "Big Data") ]
```

Permite construir relações temáticas e detectar similaridade.

### Indexações:

```python
user_ids_by_interest[interest] -> [ids]
interests_by_user_id[user_id] -> [interesses]
```

Criadas com `defaultdict(list)` para agrupamento eficiente.

---

## 12. Busca de Usuários por Interesse

```python
def data_scientists_who_like(target_interest):
    return [user_id for user_id, ui in interests if ui == target_interest]
```

Busca linear simples (poderia ser otimizada usando `user_ids_by_interest`).

---

## 13. Similaridade por Interesses

```python
def most_commom_interests_with(user):
    return Counter(
        other_id
        for interest in interests_by_user_id[user["id"]]
        for other_id in user_ids_by_interest[interest]
        if other_id != user["id"]
    )
```

Produz um Counter onde cada usuário é ranqueado pela quantidade de interesses em comum.

Aplicações:

- Recomendação de conexões.
- Agrupamento temático.
- Sugestão de conteúdo.

---

## 14. Versão Compacta (Nova Parte Adicional)

```python
users = [...]
friendship_pair = [...]
friendships = {u["id"]: [] for u in users}
for i, j in friendship_pair:
    friendships[i].append(j)
    friendships[j].append(i)

def number_of_friends(user):
    return len(friendships[user["id"]])

total_connections = sum(number_of_friends(u) for u in users)
num_users = len(users)
avg_connections = total_connections / num_users
print(total_connections, f"{avg_connections:.2f}")
num_friends_by_id = [(u["id"], number_of_friends(u)) for u in users]
num_friends_by_id.sort(key=lambda t: t[1], reverse=True)
print(num_friends_by_id)
```

---

## 15. Possíveis Extensões

- Normalizar similaridade (ex.: Jaccard, Cosine).
- Recomendação híbrida (FOAF + interesses).
- Ponderar interesses raros vs comuns (TF-IDF simples).
- Detectar comunidades via Louvain ou Label Propagation.
- Calcular centralidades avançadas (betweenness, closeness, eigenvector).

---

## 16. Resumo Final

O script evolui de uma rede básica para incorporar:

- Sugestões via amigos de amigos.
- Similaridade semântica via interesses.

Isso aproxima o exemplo de funcionalidades reais de redes sociais iniciais.

---

Autor: (Alex Abreu)
