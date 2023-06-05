def mod_inverse(x, y):
    # Função para calcular o inverso modular de x em relação a y

    def extended_euclidean_algorithm(a, b):
        # Implementação do algoritmo de Euclides estendido

        if b == 0:
            return (1, 0)
        
        # Divide a por b e obtém o quociente q e o resto r
        (q, r) = (a // b, a % b)
        
        # Chama recursivamente o algoritmo de Euclides estendido para (b, r)
        (s, t) = extended_euclidean_algorithm(b, r)
        
        # Retorna o resultado da recursão e realiza os cálculos necessários para obter os coeficientes s e t corretos
        return (t, s - (q * t))

    inv = extended_euclidean_algorithm(x, y)[0]
    
    if inv < 1:
        inv += y  # Queremos apenas valores positivos
        
    return inv
