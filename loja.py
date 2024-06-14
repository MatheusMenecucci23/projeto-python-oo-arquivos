import json
from datetime import datetime

# Arquivos para persistência
CLIENTES_FILE = 'clientes.json'
VEICULOS_FILE = 'veiculos.json'
ALUGUEIS_FILE = 'aluguels.json'

#abrindo um arquivo json para leitura e retornando os dados do arquivo
def load_data(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

#abrindo o arquivo para escrita, e escreve os dados
def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def listar_todos(dados):
    return dados

def listar_um(dados, chave, valor):
    for item in dados:
        if item[chave] == valor:
            return item
    return None

def incluir(dados, item, chave):
    if listar_um(dados, chave, item[chave]) is None:
        dados.append(item)
        return True
    return False

def alterar(dados, chave, valor, novos_dados):
    for i, item in enumerate(dados):
        if item[chave] == valor:
            dados[i].update(novos_dados)
            return True
    return False

def excluir(dados, chave, valor):
    for i, item in enumerate(dados):
        if item[chave] == valor:
            del dados[i]
            return True
    return False

def submenu_clientes():
    clientes = load_data(CLIENTES_FILE)
    while True:
        print("\nSubmenu Clientes:")
        print("1. Listar todos")
        print("2. Listar um")
        print("3. Incluir")
        print("4. Alterar")
        print("5. Excluir")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            for cliente in listar_todos(clientes):
                print(cliente)
        elif opcao == '2':
            cpf = input("Digite o CPF do cliente: ")
            cliente = listar_um(clientes, 'CPF', cpf)
            if cliente:
                print(cliente)
            else:
                print("Cliente não encontrado.")
        elif opcao == '3':
            cliente = {
                'CPF': input("CPF: "),
                'Nome': input("Nome: "),
                'Endereco': input("Endereço: "),
                'Telefone_fixo': input("Telefone fixo: "),
                'Telefone_celular': input("Telefone celular: "),
                'Data_nascimento': input("Data de nascimento (dd/mm/yyyy): ")
            }
            if incluir(clientes, cliente, 'CPF'):
                save_data(CLIENTES_FILE, clientes)
                print("Cliente incluído com sucesso.")
            else:
                print("Cliente com esse CPF já existe.")
        elif opcao == '4':
            cpf = input("Digite o CPF do cliente: ")
            novos_dados = {
                'Nome': input("Nome: "),
                'Endereco': input("Endereço: "),
                'Telefone_fixo': input("Telefone fixo: "),
                'Telefone_celular': input("Telefone celular: "),
                'Data_nascimento': input("Data de nascimento (dd/mm/yyyy): ")
            }
            if alterar(clientes, 'CPF', cpf, novos_dados):
                save_data(CLIENTES_FILE, clientes)
                print("Dados do cliente alterados com sucesso.")
            else:
                print("Cliente não encontrado.")
        elif opcao == '5':
            cpf = input("Digite o CPF do cliente: ")
            if excluir(clientes, 'CPF', cpf):
                save_data(CLIENTES_FILE, clientes)
                print("Cliente excluído com sucesso.")
            else:
                print("Cliente não encontrado.")
        elif opcao == '6':
            break
        else:
            print("Opção inválida.")

def submenu_veiculos():
    veiculos = load_data(VEICULOS_FILE)
    while True:
        print("\nSubmenu Veículos:")
        print("1. Listar todos")
        print("2. Listar um")
        print("3. Incluir")
        print("4. Alterar")
        print("5. Excluir")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            for veiculo in listar_todos(veiculos):
                print(veiculo)
        elif opcao == '2':
            codigo = input("Digite o código do veículo: ")
            veiculo = listar_um(veiculos, 'Código', codigo)
            if veiculo:
                print(veiculo)
            else:
                print("Veículo não encontrado.")
        elif opcao == '3':
            veiculo = {
                'Código': input("Código: "),
                'Descrição': input("Descrição: "),
                'Categoria': input("Categoria: "),
                'Capacidade': input("Capacidade: "),
                'Combustível': input("Combustível: "),
                'Ano': input("Ano: "),
                'Modelo': input("Modelo: ")
            }
            if incluir(veiculos, veiculo, 'Código'):
                save_data(VEICULOS_FILE, veiculos)
                print("Veículo incluído com sucesso.")
            else:
                print("Veículo com esse código já existe.")
        elif opcao == '4':
            codigo = input("Digite o código do veículo: ")
            novos_dados = {
                'Descrição': input("Descrição: "),
                'Categoria': input("Categoria: "),
                'Capacidade': input("Capacidade: "),
                'Combustível': input("Combustível: "),
                'Ano': input("Ano: "),
                'Modelo': input("Modelo: ")
            }
            if alterar(veiculos, 'Código', codigo, novos_dados):
                save_data(VEICULOS_FILE, veiculos)
                print("Dados do veículo alterados com sucesso.")
            else:
                print("Veículo não encontrado.")
        elif opcao == '5':
            codigo = input("Digite o código do veículo: ")
            if excluir(veiculos, 'Código', codigo):
                save_data(VEICULOS_FILE, veiculos)
                print("Veículo excluído com sucesso.")
            else:
                print("Veículo não encontrado.")
        elif opcao == '6':
            break
        else:
            print("Opção inválida.")

def submenu_alugueis():
    alugueis = load_data(ALUGUEIS_FILE)
    while True:
        print("\nSubmenu Aluguéis:")
        print("1. Listar todos")
        print("2. Listar um")
        print("3. Incluir")
        print("4. Alterar")
        print("5. Excluir")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            for aluguel in listar_todos(alugueis):
                print(aluguel)
        elif opcao == '2':
            cpf = input("Digite o CPF do cliente: ")
            codigo = input("Digite o código do veículo: ")
            aluguel = listar_um(alugueis, 'CPF', cpf)
            if aluguel and aluguel['Código'] == codigo:
                print(aluguel)
            else:
                print("Aluguel não encontrado.")
        elif opcao == '3':
            aluguel = {
                'CPF': input("CPF do cliente: "),
                'Código': input("Código do veículo: "),
                'Data_entrada': input("Data de entrada (dd/mm/yyyy): "),
                'Data_saida': input("Data de saída (dd/mm/yyyy): ")
            }
            if incluir(alugueis, aluguel, 'CPF'):
                save_data(ALUGUEIS_FILE, alugueis)
                print("Aluguel incluído com sucesso.")
            else:
                print("Aluguel com esse CPF já existe.")
        elif opcao == '4':
            cpf = input("Digite o CPF do cliente: ")
            novos_dados = {
                'Código': input("Código do veículo: "),
                'Data_entrada': input("Data de entrada (dd/mm/yyyy): "),
                'Data_saida': input("Data de saída (dd/mm/yyyy): ")
            }
            if alterar(alugueis, 'CPF', cpf, novos_dados):
                save_data(ALUGUEIS_FILE, alugueis)
                print("Dados do aluguel alterados com sucesso.")
            else:
                print("Aluguel não encontrado.")
        elif opcao == '5':
            cpf = input("Digite o CPF do cliente: ")
            if excluir(alugueis, 'CPF', cpf):
                save_data(ALUGUEIS_FILE, alugueis)
                print("Aluguel excluído com sucesso.")
            else:
                print("Aluguel não encontrado.")
        elif opcao == '6':
            break
        else:
            print("Opção inválida.")

def submenu_relatorios():
    clientes = load_data(CLIENTES_FILE)
    veiculos = load_data(VEICULOS_FILE)
    alugueis = load_data(ALUGUEIS_FILE)
    while True:
        print("\nSubmenu Relatórios:")
        print("1. Mostrar todas as reservas de um cliente")
        print("2. Mostrar todas as reservas de um veículo")
        print("3. Mostrar reservas entre datas")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cpf = input("Digite o CPF do cliente: ")
            reservas = [aluguel for aluguel in alugueis if aluguel['CPF'] == cpf]
            for reserva in reservas:
                print(reserva)
        elif opcao == '2':
            codigo = input("Digite o código do veículo: ")
            reservas = [aluguel for aluguel in alugueis if aluguel['Código'] == codigo]
            for reserva in reservas:
                print(reserva)
        elif opcao == '3':
            data_inicio = input("Digite a data de início (dd/mm/yyyy): ")
            data_fim = input("Digite a data de fim (dd/mm/yyyy): ")
            data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
            data_fim = datetime.strptime(data_fim, '%d/%m/%Y')
            
            reservas = []
            for aluguel in alugueis:
                data_entrada = datetime.strptime(aluguel['Data_entrada'], '%d/%m/%Y')
                data_saida = datetime.strptime(aluguel['Data_saida'], '%d/%m/%Y')
                if data_entrada >= data_inicio and data_saida <= data_fim:
                    cliente = listar_um(clientes, 'CPF', aluguel['CPF'])
                    veiculo = listar_um(veiculos, 'Código', aluguel['Código'])
                    reservas.append({
                        'Veículo': veiculo,
                        'Cliente': cliente,
                        'Data_entrada': aluguel['Data_entrada'],
                        'Data_saida': aluguel['Data_saida']
                    })
            
            for reserva in reservas:
                print(f"Veículo: {reserva['Veículo']}")
                print(f"Cliente: {reserva['Cliente']}")
                print(f"Data de Entrada: {reserva['Data_entrada']}")
                print(f"Data de Saída: {reserva['Data_saida']}\n")
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

def main():
    while True:
        print("\nMenu Principal:")
        print("1. Submenu de Clientes")
        print("2. Submenu de Veículos")
        print("3. Submenu de Aluguéis")
        print("4. Submenu Relatórios")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            submenu_clientes()
        elif opcao == '2':
            submenu_veiculos()
        elif opcao == '3':
            submenu_alugueis()
        elif opcao == '4':
            submenu_relatorios()
        elif opcao == '5':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
