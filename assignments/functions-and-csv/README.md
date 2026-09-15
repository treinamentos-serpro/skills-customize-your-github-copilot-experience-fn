# 📘 Tarefa: Funções e Dados em CSV

## 🎯 Objective

Praticar o uso de funções, listas, dicionários e leitura de arquivos CSV em Python puro. Nesta atividade, os alunos criarão um pequeno analisador de notas para processar dados de estudantes, calcular médias e identificar resultados relevantes.

## 📝 Tasks

### 🛠️ Leitura e organização dos dados

#### Descrição
Crie uma função chamada `read_students(file_path)` para ler um arquivo CSV contendo dados de estudantes e retornar uma lista de dicionários com informações organizadas.

#### Requisitos
O programa completo deve:

- Ler um arquivo CSV com cabeçalho, por exemplo: `nome,nota1,nota2,nota3`
- Ignorar linhas vazias ou incompletas
- Converter as notas em valores numéricos
- Retornar uma lista de dicionários no formato:
  ```python
  [{"nome": "Ana", "nota1": 80, "nota2": 90, "nota3": 85}, ...]
  ```
- Exibir uma mensagem de erro clara se o arquivo não existir

### 🛠️ Cálculo de médias e filtro de desempenho

#### Descrição
Crie funções para calcular a média de cada aluno e identificar quais estudantes passaram ou ficaram abaixo da média mínima.

#### Requisitos
O programa completo deve:

- Definir uma função `average(student)` que devolve a média das notas do aluno
- Definir uma função `passed_students(students, minimum=60)` que retorna apenas os alunos com média maior ou igual ao valor mínimo
- Incluir pelo menos um exemplo de uso demonstrando como chamar as funções
- Mostrar o resultado em uma estrutura legível, como uma lista de nomes ou dicionários

### 🛠️ Relatório final do desempenho

#### Descrição
Crie uma função chamada `generate_report(students)` para produzir um resumo final com as principais informações da turma.

#### Requisitos
O programa completo deve:

- Contar quantos estudantes foram lidos do arquivo
- Calcular a média geral da turma
- Identificar o aluno com maior média
- Informar quantos estudantes passaram com média maior ou igual a 60
- Imprimir um relatório final em formato legível, por exemplo:
  ```python
  Total de estudantes: 10
  Média da turma: 76.5
  Melhor aluno: Lucas
  Estudantes aprovados: 7
  ```
