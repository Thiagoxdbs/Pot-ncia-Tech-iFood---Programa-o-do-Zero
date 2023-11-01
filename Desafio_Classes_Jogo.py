def criando_perfil():
    PERFIL = ('Nome', 'Idade', 'Classe')
    print('''Observação!\nClasses permitidas, são: 
          -->Mago
          -->Guerreiro
          -->Monge
          -->Ninja''')
    for c in PERFIL:
        heroi_list.append(input(f'{c} do Heroi: \n').lower().lstrip())
    return heroi_list

class heroi:
    def __init__(self,nome,idade,classe):
        self._nome = nome
        self._idade = idade
        self._classe = classe
    
    def atacar(self):
        teste_classe = heroi_list[2]
        ATAQUE_MAGO = 'mago' == teste_classe
        ATAQUE_GUERREIRO = 'guerreiro' == teste_classe
        ATAQUE_MONGE = 'monge' == teste_classe
        ATAQUE_NINJA = 'ninja' == teste_classe
        if ATAQUE_MAGO:
            print(f'\"O {heroi_list[0]} atacou usando Magia.\"')
        if ATAQUE_GUERREIRO:
            print(f'\"O {heroi_list[0]} atacou usando Espada.\"')
        if ATAQUE_MONGE:
            print(f'\"O {heroi_list[0]} atacou usando Artes marciais.\"')
        if ATAQUE_NINJA:
            print(f'\"O {heroi_list[0]} atacou usando Shuriken.\"')
        
    @property
    def classe(self):
        return self._classe
    
    @property
    def nome(self):
        return self._nome
    
def validacao_loop():
    print('Classe escolhida está incorreta.\nEscolha novamente!')
    heroi_list = criando_perfil()
    teste_classe = heroi_list[2]
    validacao = 'mago' == teste_classe or 'guerreiro' == teste_classe or 'monge' == teste_classe or 'ninja' == teste_classe
    return validacao

heroi_list = list()
heroi_list = criando_perfil()
teste_classe = heroi_list[2]
validacao = 'mago' == teste_classe or 'guerreiro' == teste_classe or 'monge' == teste_classe or 'ninja' == teste_classe


while not validacao:
    heroi_list.clear()
    validacao = validacao_loop()
    if validacao:
        break

while validacao:
    acao_heroi = input(f'Escolha a ação do seu personagem:\n[1]Recriar Personagem\n[2]Atacar\n[3]Sair\n--> ').upper()
    CRIAR_PERSONAGEM = acao_heroi == '1' or acao_heroi[0] == 'C'
    ATACAR = acao_heroi == '2'or acao_heroi[0] == 'A'
    SAIR = acao_heroi == '3'or acao_heroi[0] == 'S'
    if CRIAR_PERSONAGEM:
        heroi_list.clear()
        heroi_list = criando_perfil()
        validacao = validacao_loop()
    elif ATACAR:
        heroi.atacar(f'O {heroi.nome}:\n')
    elif SAIR:
        validacao = False

