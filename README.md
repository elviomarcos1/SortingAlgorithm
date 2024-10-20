# Comparação de Algoritmos de Ordenação

Este projeto foi desenvolvido para comparar a eficiência de três algoritmos de ordenação: **Heap Sort**, **Selection Sort** e **Insertion Sort**. A comparação é feita a partir da execução desses algoritmos sobre um conjunto de dados aleatórios gerados automaticamente, com diferentes tamanhos. Para visualização dos resultados, utilizamos gráficos interativos com a ajuda das bibliotecas **Dash**, **Plotly** e **Pandas**.

## Descrição do Projeto

O objetivo principal deste projeto é analisar e comparar o desempenho dos algoritmos de ordenação mencionados acima. Para isso, seguimos os seguintes passos:

1. **Geração de Dados Aleatórios**:
   - Criamos um arquivo que gera conjuntos de dados aleatórios.
   - Os tamanhos dos conjuntos variam de 200 a 5000, em intervalos de 200.

2. **Algoritmos de Ordenação**:
   - **Heap Sort**: Um algoritmo eficiente baseado em estruturas de heap.
   - **Selection Sort**: Um algoritmo simples de ordenação por seleção.
   - **Insertion Sort**: Um algoritmo de ordenação por inserção, geralmente eficiente para pequenos conjuntos de dados.

3. **Execução dos Algoritmos**:
   - Cada algoritmo é executado em um número crescente de dados aleatórios, começando com 200 até 5000 dados.
   - Medimos o tempo de execução de cada algoritmo para cada tamanho de conjunto de dados.

4. **Visualização dos Resultados**:
   - Usamos as bibliotecas **Dash**, **Plotly** e **Pandas** para organizar os dados coletados e criar gráficos interativos.
   - Os gráficos são exibidos em uma escala **semilogarítmica**, facilitando a comparação do desempenho dos algoritmos.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação usada no desenvolvimento do projeto.
- **Dash**: Framework para a criação de web apps interativos em Python.
- **Plotly**: Biblioteca utilizada para criar os gráficos interativos.
- **Pandas**: Usada para manipulação e organização de dados.
- **NumPy**: Utilizada para geração de números e arrays aleatórios.

## Como Executar o Projeto

Siga os passos abaixo para executar o projeto localmente:

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd nome-do-projeto
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):
   - **Windows**:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
   - **Linux**:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```
5. Execute o aplicativo:
   ```
   python app.py
   ```

##Estrutura do projeto
```
/nome-do-projeto
│
├── /algorithms
│   ├── heap_sort.py
│   ├── selection_sort.py
│   └── insertion_sort.py
│
├── /data
│   └── data_generator.py
│
├── app.py
├── requirements.txt
└── README.md
```

   
