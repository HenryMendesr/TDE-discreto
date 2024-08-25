nome_arquivo = "TDE-3.txt"

def U(conj1, conj2):
    print(conj1 | conj2)
    
def I(conj1, conj2):
    print(conj1 & conj2)
    
def D(conj1, conj2):
    print(conj1 - conj2)
    
def P_C(conj1, conj2):
    produto = {(e1, e2) for e1 in conj1 for e2 in conj2}
    print(produto)
    
def T_S(string): return {e.strip() for e in string.split(',')}

with open(nome_arquivo, 'r', encoding='latin-1') as arquivo:
    linhas = [l.strip() for l in arquivo]
    numOp = int(linhas[0])
    for i in range(numOp):
        conj1, conj2 = T_S(linhas[3*i+2]), T_S(linhas[3*i+3])
        operacao = linhas[3*i+1]
        
        if operacao == 'U':
            print("União:")
            U(conj1, conj2)
        elif operacao == 'I':
            print("Interseção:")
            I(conj1, conj2)
        elif operacao == 'D':
            print("Diferença:")
            D(conj1, conj2)
        else:
            print("Produto Cartesiano:")
            P_C(conj1, conj2)