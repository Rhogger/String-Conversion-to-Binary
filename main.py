import pickle

def criarContato():
    nome = input("Digite o nome do contato: ")
    sobrenome = input("Digite o sobrenome do contato: ")
    telefone = input("Digite o número de telefone: ")
    pessoal = input("Digite o email pessoal: ")
    academico = input("Digite o email academico: ")

    contato = {
        "Informacao": {
            "Nome": nome,
            "Sobrenome": sobrenome,
            "Contato": {
                "Telefone": telefone,
                "Emails": {
                    "pessoal": pessoal,
                    "academico": academico
                }
            }
        }
    }

    return contato


def salvarContatos(contatos):
    with open("user.bin", "wb") as arquivo:
        pickle.dump(contatos, arquivo)
    print("Contato salvo com sucesso!")


def main():
            contatos = []
            contato = criarContato()
            contatos.append(contato)
            salvarContatos(contatos)

if __name__ == "__main__":
    main()
