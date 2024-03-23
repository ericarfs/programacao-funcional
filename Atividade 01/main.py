def cabeca(a): 
    return a[0]

def cauda(a):
    return a[1:]

def num_primo(numero, fator): 
    if fator > (numero/2) + 1:
        return True 
    
    if numero % fator == 0:
        return False
        
    return num_primo(numero, fator + 1)


def listar_primos(numero, final):
    if numero > final:
        return []
    

    if num_primo(numero, 2):
        return [numero] + listar_primos(numero + 1, final)
        
    return listar_primos(numero + 1, final)
    
    
def encontrar_diferencas(lista):
    if len(lista) < 2:
        return []
        
    m = cauda(lista)
    c = cabeca(lista)
    c2 = cabeca(m)
    
    return [c2 -c] + encontrar_diferencas(m)
    

def encontrar_maior(lista, comb):
    if len(lista) == 0:
        return 0
    
    m = encontrar_maior(cauda(lista), comb)
    c = cabeca(lista)
    
    return comb(c,m)
    
    
def main():
    inicio = int(input().rstrip())
    final = int(input().rstrip())

    lista_primos = listar_primos(inicio, final)
    lista_diferencas = encontrar_diferencas(lista_primos)
    maior_diferenca = encontrar_maior(lista_diferencas, lambda x,y: x  if x > y else y)


    print(maior_diferenca)

    
if __name__ == "__main__":
    main()
