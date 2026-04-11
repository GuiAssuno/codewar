import sys

def resolver():
    # Lê todos os dados de uma vez (ultrarrápido e à prova de formatação quebrada)
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    idx = 0
    while idx < len(entrada):
        n = int(entrada[idx])
        idx += 1
        
        # O problema encerra quando N for 0
        if n == 0:
            break
            
        # Processa as várias consultas (trens) para este bloco de N vagões
        while idx < len(entrada):
            primeiro_vagao = int(entrada[idx])
            
            # Se a linha for apenas 0, significa que o bloco de consultas acabou
            if primeiro_vagao == 0:
                idx += 1
                print() # Imprime a linha em branco obrigatória após cada bloco
                break
            
            # Monta a sequência alvo que o chefe quer
            alvo = [primeiro_vagao]
            for _ in range(1, n):
                idx += 1
                alvo.append(int(entrada[idx]))
                
            # --- SIMULAÇÃO DA ESTAÇÃO (PILHA) ---
            estacao = []
            trem_chegando = 1
            possivel = True
            
            for vagao_desejado in alvo:
                # Enquanto a estação estiver vazia OU o topo não for o vagão que eu quero,
                # eu continuo empurrando novos vagões da Direção A para a estação.
                while trem_chegando <= n and (not estacao or estacao[-1] != vagao_desejado):
                    estacao.append(trem_chegando)
                    trem_chegando += 1
                
                # Se o vagão que eu quero finalmente estiver no topo da estação, ele sai.
                if estacao and estacao[-1] == vagao_desejado:
                    estacao.pop()
                else:
                    # Se não chegou e não está no topo, ele está travado embaixo de outros.
                    possivel = False
                    break
                    
            if possivel:
                print("Yes")
            else:
                print("No")

resolver()
