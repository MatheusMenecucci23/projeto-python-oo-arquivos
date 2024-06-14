# Locadora de Automóveis

Este repositório foi criado para estudos de Programação Orientada a Objetos (POO) e manipulação de arquivos em Python. A aplicação gerencia informações sobre aluguéis de veículos, clientes e veículos disponíveis para locação.

## Estrutura do Projeto

- **clientes.json**: Arquivo para persistência dos dados dos clientes.
- **veiculos.json**: Arquivo para persistência dos dados dos veículos.
- **aluguels.json**: Arquivo para persistência dos dados dos aluguéis.
- **loja.py**: Arquivo principal da aplicação.

## Funcionalidades

A aplicação apresenta o seguinte menu de opções para o usuário:

### Menu Principal:
1. Submenu de Clientes
2. Submenu de Veículos
3. Submenu de Aluguéis
4. Submenu Relatórios
5. Sair

### Submenus:

Cada submenu oferece as opções:
- **Listar todos**: Lista todos os registros.
- **Listar um**: Lista um registro específico.
- **Incluir**: Inclui um novo registro, garantindo a não duplicidade de chaves.
- **Alterar**: Altera um registro existente.
- **Excluir**: Exclui um registro após confirmação.

### Submenu Relatórios:

1. Mostrar todas as reservas de um cliente.
2. Mostrar todas as reservas de um veículo.
3. Mostrar reservas entre datas específicas.

## Estrutura de Dados

### Clientes
- `CPF`: Chave primária
- `Nome`
- `Endereço`
- `Telefone fixo`
- `Telefone celular`
- `Data de nascimento`

### Veículos
- `Código`: Chave primária
- `Descrição`
- `Categoria`
- `Capacidade`
- `Combustível`
- `Ano`
- `Modelo`

### Aluguéis
- `CPF do cliente`: Chave composta
- `Código do veículo`: Chave composta
- `Data de entrada`: Chave composta
- `Data de saída`: Chave composta

## Requisitos

- Python 3.x
- VSCode (ou qualquer outro editor de texto)

## Como Rodar a Aplicação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/locadora-automoveis.git
   cd locadora-automoveis
