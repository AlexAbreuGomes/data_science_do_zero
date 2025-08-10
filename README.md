# Estudos do Livro: Data Science do Zero (Noções Básicas com Python)

Este diretório registra minhas leituras, anotações, exercícios e explorações práticas do livro **"Data Science do Zero: Noções Básicas com Python"**. A organização segue a estrutura de capítulos (cap01, cap02, ...), cada um com código e notas associadas.

---
## Objetivos
- Consolidar entendimento conceitual capítulo a capítulo.
- Manter scripts simples e didáticos reproduzindo exemplos e variações.
- Produzir anotações em Markdown para revisão futura.
- Servir como base para evoluções (visualização, métricas, modelos, etc.).

---
## Estrutura de Pastas
| Pasta    | Conteúdo | Status |
|----------|----------|--------|
| `cap01/` | Introdução: Python básico, estruturas simples, rede social, interesses | Em progresso |
| `cap02/` | (Reservado) – Probabilidade / estatística introdutória | Planejado |
| `cap03/` | (Reservado) – Visualização de dados | Planejado |
| `cap04/` | (Reservado) – Álgebra linear / vetores | Planejado |
| `cap05/` | (Reservado) – Estatística descritiva | Planejado |
| `...`    | Demais capítulos seguirão mesma convenção | — |

Cada capítulo poderá conter:
- `introducao.py` ou scripts principais do tema.
- Outros arquivos `.py` para experimentos complementares.
- `cod_<tema>.md` explicando o código detalhadamente.
- Anotações adicionais em `.md` (resumos, fórmulas, insights).

---
## Guia de Leitura / Evolução
1. Ler o capítulo no livro.
2. Reproduzir o exemplo base em Python puro (sem bibliotecas externas se o capítulo assim propõe).
3. Escrever anotações em Markdown (contexto + conceitos + exemplos próprios).
4. Refatorar se necessário para clareza (nomes, funções pequenas, docstrings).
5. (Opcional) Expandir com: métricas extras, testes rápidos, comparações.

---
## Conteúdos Já Abordados (cap01)
- Representação de rede social com dicionários (lista de adjacência).
- Contagem de conexões e ranking por grau.
- Amigos de amigos (FOAF) e recomendação simples.
- Interesses compartilhados e similaridade baseada em contagem.
- Uso de `defaultdict` e `Counter`.

---
## Próximos Passos
- Criar esqueleto de arquivos para `cap02/`.
- Adicionar métricas derivadas (ex.: grau médio, distribuição de graus como histograma).
- Normalizar similaridade entre usuários (Jaccard / Cosine simples).
- Introduzir testes unitários básicos para funções de recomendação.

---
## Convenções
- Idioma: Português nas anotações e docstrings.
- Nome de pastas: `capXX` com zero à esquerda até 9.
- Somente dependências da biblioteca padrão nas primeiras fases.
- Expansões com libs (p.ex. `networkx`, `matplotlib`) serão documentadas quando introduzidas.

---
## Como Navegar
- Leia primeiro os arquivos `cod_*.md` para entendimento rápido.
- Abra os scripts `.py` e execute incrementalmente (REPL ou terminal) para exploração.
- Modifique entradas (ex.: listas de interesses) para observar mudanças em sugestões.

---
## Licença / Uso
Material de estudo pessoal. Livre para leitura e inspiração acadêmica.

---
Autor: Alex Abreu
