import re

def findIds(codigo):
    pattern = re.compile(r"int\s[a-z]\=", re.MULTILINE | re.DOTALL) 
    
    ids = pattern.findall(codigo)

    retorno = []
    for id in ids:
        id = id.replace("int ", '') 
        id = id.replace("=", '') 
        retorno.append(id)

    return retorno

def analise(codigo, tokens, estruturas):
    
    #foram de extrair identificados
    ids = findIds(codigo)

    for i in range(0, len(estruturas)):
        codigo = codigo.replace(estruturas[i], ' ')
    
    c = codigo.split()
    
    for i in range(0, len(c)):
        if not c[i].isdigit(): 
            if not c[i] in tokens:
                if not c[i] in ids:
                    return 'Erro de Sintaxe: ', c[i]
    
    return 'Codigo correto'
    
if __name__ == '__main__':
    codigo = 'int main(){ c, int a=1; int b=2; return 0; }'
    tokens = ['int', 'main', 'return', 'if', 'for']
    estruturas = [';', '(', ')', '{', '}', '=']
    
    print(analise(codigo, tokens, estruturas))