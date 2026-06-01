Trabalho: Sistema de Monitoramento Climático

Objetivo

Construir um programa em Python que leia uma lista de cidades, consulte as condições climáticas atuais de cada uma via API, armazene esses dados utilizando conceitos de Orientação a Objetos e exiba um relatório formatado na tela.

Requisitos do Sistema

1. Modelagem de Dados (Orientação a Objetos)

O aluno deve criar uma classe chamada CidadeClima.

Atributos privados/públicos: nome, temperatura, umidade e condicao.
Método Construtor (__init__): Para inicializar as propriedades.
Método de Exibição: Um método (ou sobrescrita do __str__) para retornar os dados formatados da cidade.
2. Consumo de Dados (API e Listas)

O programa deve possuir uma lista inicial com pelo menos 5 cidades pré-definidas (ex: ['São Paulo', 'London', 'Tokyo', 'New York', 'Paris']).
O sistema deve iterar sobre essa lista e fazer uma requisição HTTP (usando a biblioteca requests) para a API do OpenWeatherMap (OU A API TRABALHADA NA ÚLTIMA AULA) para cada cidade.
Os dados JSON retornados devem ser extraídos e instanciados como objetos da classe CidadeClima.
Cada objeto criado deve ser guardado em uma lista principal chamada relatorio_clima.
3. Exibição dos Resultados

O programa deve percorrer a lista relatorio_clima e exibir os dados na tela de forma organizada e legível para o usuário.