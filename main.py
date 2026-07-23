from Modulo_06.ex86 import Mensagem
from Modulo_06.ex87 import Risco
from Modulo_06.ex88 import RegistroDeRiscos
from datetime import date

def c_mensagem() -> Mensagem:
    autor = input('Digite o nome do autor que gerou a mensagem: ')
    texto = input('Digite o texto da mensagem: ')
    return Mensagem(autor, texto, date.today())

def c_risco(mensagem) -> Risco:
    categoria = input('Digite a categoria do risco: ')
    impacto = input('De 0 a 10 fale o impacto: ')
    return Risco(mensagem, categoria, impacto)

def main():
    registro = RegistroDeRiscos()

    while True:
        try:
            operacao = input('Digite a operação que quer realizar(1-Sair, 2-Adicionar risco, 3-Filtrar por categoria, 4-Mais criticos): ')

            if operacao == '1':
                break
            elif operacao == '2':
                registro.adicionar(c_risco(c_mensagem()))
            elif operacao == '3':
                palavra = input('Digite a categoria que quer filtrar: ')
                print(registro.por_categoria(palavra))
            elif operacao == '4':
                quantidade = input('Fala a quantidade de risco que seja apresentado: ')
                print(registro.mais_graves(int(quantidade)))
            else:
                print('Operacação invalida')
        except ValueError:
            print('Cadastre apenas mensagem com riscos')


if __name__ == "__main__":
    main()