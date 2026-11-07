from src.tunesort.cli import interface

def main(escolha):
    escolha = interface.mostrar_menu()
    acoes = {
        "curtidas" : 1,
        "organizar" : 2,
        "playlist" : 3,
        "config" : 4,
        "sobre" : 5,
        "sair" : 6
    }

    acoes[escolha]()
main()