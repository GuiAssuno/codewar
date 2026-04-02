import pathlib
from pathlib import Path
path = Path(__file__).parent

caminho1 = path / 'azeitonas/in/10.txt'
caminho2 = path / 'azeitonas/out/20.txt'


def comparador():
    try:
        with open(caminho1, 'r', encoding='utf-8') as f1, open(caminho1, 'r', encoding='utf-8') as f2:
            linha_num =1
            
            while True:
                linha_f1 = f1.readline()
                linha_f2 = f2.readline()

                if not linha_f1 and not linha_f2:
                    print(" ")
                    print(" ")
                    print(" ")
                    print(" ")
                    print(" ")                    
                    print(" ====  APROVADO  ====")
                    print(" ")
                    print(" ")
                    print(" ")
                    print(" ")
                    print(" ")
                    return True

                if linha_f1 != linha_f2:
                    print(" ")
                    print(" ")
                    print("!!!!!!!!!!!!   ERRO ENCONTRADO      !!!!!!!!!")
                    print(" ")
                    print(" ")
                    return False
                linha_num += 1
    except FileNotFoundError as e:
        print(e)
        return False


if __name__ == '__main__':
    
    #print (caminho1)
    #print (caminho2)
    valor = comparador()