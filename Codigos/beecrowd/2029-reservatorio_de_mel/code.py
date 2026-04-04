# O laço 'while True' vai rodar infinitamente até o arquivo de testes acabar
while True:
    try:
        # Lendo os dados de entrada
        volume = float(input())
        diametro = float(input())
        
        # O raio é sempre a metade do diâmetro
        raio = diametro / 2.0
        
        # O valor de pi exigido pelo problema
        pi = 3.14
        
        # Calculando a área da boca do recipiente (Área do círculo = pi * r²)
        area = pi * (raio * raio)
        
        # Calculando a altura (Volume do cilindro = Área da base * Altura)
        # Logo, Altura = Volume / Área da base
        altura = volume / area
        
        # Imprimindo os resultados formatados com 2 casas decimais (.2f)
        print(f"ALTURA = {altura:.2f}")
        print(f"AREA = {area:.2f}")
        
    except EOFError:
        # Quando o Beecrowd parar de enviar dados, dá um erro de EOF (End of File).
        # O 'break' serve para sair do laço 'while' em segurança e encerrar o programa.
        break