import ply.lex as lex

tokens = [  'VARIABLE','NUMERO','SUMA','RESTA','MULTIPLICACION','DIVISION', 'IGUALDAD','POTENCIACION','ESIGUAL','NEGACION','CONDICIONSI','CICLOPARA','MAYOR','MENOR','MAYORIGUAL','MENORIGUAL','ABRIRPARENTESIS','CERRARPARENTESIS']

condicionLIST=['SI','SINO','ENTONCES']

paraList=['PARA','HASTA','SALTAR','HACER']

t_ignore = ' \t'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IGUALDAD = r'='
#t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_POTENCIACION = r'\^'
t_ESIGUAL = r'=='
t_NEGACION= r'!='
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL    = r'>='
t_MENORIGUAL    = r'<='
t_ABRIRPARENTESIS = r'('
t_CERRARPARENTESIS = r')'

def t_COMENTARIO(t):
    r'\#.*'
    pass


def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    for r in condicionLIST:
            if r.upper() == t.value.upper():
                t.type = 'CONDICIONSI'
                return t
    for r in paraList:
            if r.upper() == t.value.upper():
                t.type = 'CICLOPARA'
                return t
    return t


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

postfija="postfija.txt"
listaExpresiones = [x.strip('\n') for x in open(postfija, "r").readlines()]


lex.lex() # Build the lexer
for x in listaExpresiones:
    lex.input(x)
    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
