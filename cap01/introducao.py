from collections import Counter, defaultdict

"""
Análise de Rede Social - Estudo de Conexões entre Usuários

Este programa demonstra conceitos básicos de análise de redes sociais,
calculando estatísticas sobre amizades entre usuários.
"""

# Lista de usuários da rede social
# Cada usuário é representado por um dicionário com ID único e nome
users = [
    {"id": 0, "name": "hero"},
    {"id": 1, "name": "dunn"},
    {"id": 2, "name": "sue"},
    {"id": 3, "name": "chi"},
    {"id": 4, "name": "thor"},
    {"id": 5, "name": "clive"},
    {"id": 6, "name": "hicks"},
    {"id": 7, "name": "devin"},
    {"id": 8, "name": "kate"},
    {"id": 9, "name": "klein"},
]

# Pares de amizade representados como tuplas (id_usuario1, id_usuario2)
# Cada tupla indica que existe uma amizade bidirecional entre dois usuários
friendship_pair = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

# Criação do dicionário de amizades
# Inicializa uma lista vazia para cada usuário armazenar seus amigos
friendships = {user["id"]: [] for user in users}

# Populando o dicionário de amizades
# Para cada par de amigos, adiciona cada um na lista de amigos do outro
# Isso garante que a amizade seja bidirecional
for i, j in friendship_pair:
    friendships[i].append(j)  # adiciona j como amigo de i
    friendships[j].append(i)  # adiciona i como amigo de j

def number_of_friends(user):
    """
    Calcula o número de amigos de um usuário específico.
    
    Args:
        user (dict): Dicionário contendo informações do usuário, incluindo seu ID
        
    Returns:
        int: Número total de amigos do usuário
        
    Exemplo:
        user_hero = {"id": 0, "name": "hero"}
        num_amigos = number_of_friends(user_hero)  # retorna quantos amigos hero tem
    """
    user_id = user["id"]           # extrai o ID do usuário
    friend_ids = friendships[user_id]  # busca a lista de amigos deste usuário
    return len(friend_ids)         # retorna a quantidade de amigos

# Cálculo de estatísticas da rede social

# Soma total de todas as conexões na rede
# Usa generator expression para calcular o número de amigos de cada usuário
total_connections = sum(number_of_friends(user) for user in users)

# Número total de usuários na rede
num_users = len(users)

# Média de conexões por usuário
# Divide o total de conexões pelo número de usuários
avg_connections = total_connections / num_users

# Exibição dos resultados básicos
print(f"Total connections: {total_connections}")
print(f"Average connections per user: {avg_connections:.2f}")

# Análise e Ranking de Usuários por Popularidade (Número de Amigos)
"""
ALGORITMO DE RANKING POR POPULARIDADE:

Este bloco implementa um algoritmo simples para classificar usuários por popularidade
na rede social, baseado no número de conexões (amigos) que cada um possui.

PASSOS DO ALGORITMO:
1. MAPEAMENTO: Cria uma lista de tuplas (id_usuario, numero_de_amigos)
2. ORDENAÇÃO: Ordena por número de amigos em ordem decrescente  
3. EXIBIÇÃO: Mostra o ranking final

ESTRUTURA DE DADOS RESULTANTE:
Cada elemento da lista é uma tupla: (id, quantidade_amigos)
Exemplo: [(1, 3), (2, 3), (0, 2), ...]
Onde o primeiro número é o ID do usuário e o segundo é quantos amigos ele tem.

APLICAÇÃO PRÁTICA:
Este tipo de análise é fundamental em:
- Identificação de influenciadores em redes sociais
- Detecção de usuários centrais na rede
- Análise de distribuição de popularidade
- Recomendação de conexões
"""

# Passo 1: Criação da lista com ID e número de amigos para cada usuário
# List comprehension que percorre todos os usuários e cria tuplas (id, num_amigos)
num_friends_by_id = [
    (user["id"],
     number_of_friends(user)) 
        for user in users
    ]

# Passo 2: Ordenação por número de amigos (do maior para o menor)
# key=lambda: especifica que a ordenação deve ser feita pelo segundo elemento da tupla (índice 1)
# reverse=True: ordena de forma decrescente (maior número de amigos primeiro)
num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],
    reverse=True
    )

# Passo 3: Exibição do ranking final
print("\nRanking de usuários por número de amigos:")
print("(ID do usuário, Número de amigos)")
print(num_friends_by_id)

def foaf_ids_bad(user):
    """
    Retorna (sem filtragem) os IDs dos amigos dos amigos (FOAF - Friend Of A Friend).
    
    NOTA:
        Esta versão é "ruim" (bad) porque:
        - Pode conter IDs duplicados (se dois amigos têm o mesmo amigo em comum).
        - Inclui o próprio usuário caso algum amigo aponte de volta para ele.
        - Inclui amigos já existentes (não só potenciais novos).
    
    Args:
        user (dict): Dicionário com ao menos a chave "id".
    Returns:
        list[int]: Lista possivelmente com repetidos de IDs FOAF.
    """
    return [ foaf_id
                for friend_id in friendships[user["id"]]
                for foaf_id in friendships[friend_id]
        ]

print(friendships[0])
print(friendships[1])
print(friendships[2])

def friends_of_friends(user):
    """
    Sugere possíveis novos amigos baseando-se em amigos de amigos (FOAF) filtrados.

    Regras de filtragem:
        - Exclui o próprio usuário.
        - Exclui IDs já conectados diretamente (já são amigos).
    
    Retorna um Counter onde a chave é o ID do potencial amigo e o valor
    é o número de caminhos (amigos em comum) que levam até ele.
    Quanto maior a contagem, maior a relevância da sugestão.

    Args:
        user (dict): Usuário alvo.
    Returns:
        Counter: Mapeamento id_potencial_amigo -> quantidade_de_amigos_em_comum.
    """
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )

print(friends_of_friends(users[3]))

# ---------------------------------------------------------------------------
# Dados de interesses dos usuários.
# Cada tupla representa (id_usuario, interesse). Um mesmo usuário pode ter
# múltiplos interesses e interesses podem se repetir entre diferentes usuários.
# Esses dados permitem construir uma rede temática / semântica.
# ---------------------------------------------------------------------------
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
    """Retorna os IDs dos usuários que possuem o interesse exato informado.

    Busca linear por correspondências no conjunto de tuplas de interesses.
    Para grandes volumes, uma indexação (como o dicionário criado adiante)
    é mais eficiente.

    Args:
        target_interest (str): Interesse a procurar.
    Returns:
        list[int]: Lista de IDs de usuários que têm esse interesse.
    """
    return[ user_id
           for user_id, user_iterest in interests
           if user_iterest == target_interest
    ]

# Indexação dos interesses para acesso rápido:
# user_ids_by_interest: chave = interesse -> lista de usuários
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# interests_by_user_id: chave = id_usuario -> lista de interesses
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_commom_interests_with(user):
    """
    Encontra usuários que compartilham mais interesses com o usuário alvo.

    Para cada interesse do usuário:
        - Recupera todos os outros usuários que também têm esse interesse.
        - Ignora o próprio usuário.
    Agrega as ocorrências em um Counter, onde o valor indica
    quantos interesses em comum existem.

    Args:
        user (dict): Usuário alvo.
    Returns:
        Counter: id_outro_usuario -> quantidade_interesses_em_comum.
    """
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

print( most_commom_interests_with(users[5]))

