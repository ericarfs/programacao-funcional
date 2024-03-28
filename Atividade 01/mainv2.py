def cabeca(a): 
    return a[0]

def cauda(a):
    return a[1:]

def eh_primo(numero, fator): 
    if fator > (numero/2) + 1:
        return True 
    
    if numero % fator == 0:
        return False
        
    return eh_primo(numero, fator + 1)


def listar_primos(numero, final):
    if numero > final:
        return []
    

    if eh_primo(numero, 2):
        return [numero] + listar_primos(numero + 1, final)
        
    return listar_primos(numero + 1, final)
    


def buscar_maior_diferenca(lista, maior_diferenca, comb):
    if len(lista) == 1:
        return maior_diferenca
    
    m = cauda(lista)
    c = cabeca(lista)
    c2 = cabeca(m)

    return buscar_maior_diferenca(m, comb(c2 - c, maior_diferenca), comb)




    
def main():
    inicio = int(input().rstrip())
    final = int(input().rstrip())

    lista_primos = listar_primos(inicio, final)
    maior_diferenca = buscar_maior_diferenca(lista_primos, 0, lambda x,y: x  if x > y else y)

    print(maior_diferenca)

    
if __name__ == "__main__":
    main()
