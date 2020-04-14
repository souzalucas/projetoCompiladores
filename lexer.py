#nao esquece do comentario
#corrigir expressao pra numero inteiro e ponto flutuante
#cadeia de caracter 'string'
import sys
import ply.lex as lex

# lista de palavras reservadas
reservadas = {
    'se'        : 'SE',
    'entao'     : 'ENTAO',
    'senao'     : 'SENAO',
    'repita'    : 'REPITA',
    'ate'       : 'ATE',
    'fim'       : 'FIM',
    'leia'      : 'LEIA',
    'retorna'   : 'RETORNA',
    'escreva'   : 'ESCREVA',
    'inteiro'   : 'INTEIRO',
    'flutuante' : 'FLUTUANTE'
}

# lista de nomes de tokens com as palavras reservadas
tokens = ['MAIS', 'MENOS', 'MULTIPLICACAO', 'DIVISAO', 'DOIS_PONTOS', 'VIRGULA', 'MENOR', 'MAIOR', 'IGUAL', 'DIFERENTE', 'MENOR_IGUAL', 'MAIOR_IGUAL', 'E_LOGICO', 'OU_LOGICO', 'NEGACAO', 'ABRE_PARENTESE', 'FECHA_PARENTESE', 'ABRE_COLCHETE', 'FECHA_COLCHETE', 'ATRIBUICAO', 'NUM_INTEIRO', 'NUM_PONTO_FLUTUANTE', 'NUM_NOTACAO_CIENTIFICA', 'ID'] + list(reservadas.values())
 
# expressões regulares para tokens simples
t_MAIS    = r'\+'
t_MENOS   = r'-'
t_MULTIPLICACAO   = r'\*'
t_DIVISAO  = r'/'
t_DOIS_PONTOS = r':'
t_VIRGULA = r','
t_MENOR = r'<'
t_MAIOR = r'>'
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MENOR_IGUAL = r'<='
t_MAIOR_IGUAL = r'>='
t_E_LOGICO = r'\&\&'
t_OU_LOGICO = r'\|\|'
t_NEGACAO = r'!'
t_ABRE_PARENTESE = r'\('
t_FECHA_PARENTESE = r'\)'
t_ABRE_COLCHETE = r'\['
t_FECHA_COLCHETE = r'\]'
t_ATRIBUICAO = r'='

def t_ID(t):
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value,'ID')    # Check for reserved words
    return t
 
# expressão regular para numero inteiro
def t_NUM_INTEIRO(t):
    r'[-\+]?[0-9]+'
    t.value = int(t.value)    
    return t

# expressão regular para numeros de ponto flutuante
def t_NUM_PONTO_FLUTUANTE(t):
    r'[-\+]?([0-9]+.[0-9]*)|([0-9]*.[0-9]+)'
    t.value = float(t.value)    
    return t

# expressão regular para notacao cientifica
def t_NUM_NOTACAO_CIENTIFICA(t):
    r'[-\+]?([0-9]+.[0-9]*)|([0-9]*.[0-9]+)e[-\+]?([0-9]+.[0-9]*)|([0-9]*.[0-9]+)'
    t.value = float(t.value)    
    return t

# expressão regular para quebra de linha
def t_NOVA_LINHA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#expressao regular para espacos e tabulacoes
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
escreva(1)
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)