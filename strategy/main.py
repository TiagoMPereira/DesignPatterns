from scripts.lista_bubble import ListaBubble
from scripts.lista_quick import ListaQuick
from scripts.lista_insertion import ListaInsertion
import numpy as np


if __name__ == "__main__":

    algoritmos = {"quick": ListaQuick, "bubble": ListaBubble, "insertion": ListaInsertion}

    while True:
        numeros = input("Olá!\nEntre com a sua lista de números inteiros (separe-os por espaços em branco):\n")
        numeros = [int(n) for n in numeros.split(" ")]
        numeros = np.array(numeros)

        algoritmo = input("Agora selecione seu algoritmo de ordenação \nbubble\nquick\ninsertion\n")
        if not algoritmo in algoritmos.keys():
            print(f"O algoritmo '{algoritmo}' não é válido, obrigado e tchau")
            break
    
        lista = algoritmos[algoritmo]()
        print(f"Você selecionou: {lista.ordenador.alg_name}")
        a_ordenar = numeros.copy()
        ordenado = lista.retorna_ordenado(a_ordenar)

        print(f"A lista ordenada é: \n{ordenado}")

        op = input("digite 1 para sair ou 0 para continuar\n")
        if op == "1":
            break
