# from PIL import Image
#
# def abrirImagem():
#     im = Image.open("sample-image.png")
#
#
import csv
import sqlite3

from PIL import Image

def abrir_imagem(imagem):
    #im = Image.open("sample-image.png")
    im = Image.open(imagem)
    im.show()

def consultar_imagem(item):
    try:
        con = sqlite3.connect('catalogo.db')
        cur = con.cursor()
        dados = (item[0])
        cur.execute('SELECT imagem FROM produtos WHERE codcli = ?',(dados,))
        con.commit()
        resposta = cur.fetchone()
        nome_arquivo = f'c:\marcelo\projetos\python\catalogo\imgconv\{item[0]}.jpg'
        writeTofile(resposta[0], nome_arquivo)
        abrir_imagem(nome_arquivo)
        print(f'Código {item[0]} consultado com sucesso.')
        cur.close()
        con.close()

    except sqlite3.Error as erro:
        print(f'Erro na consulta {item[0]}.',erro)

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
        print(filename)
    print("Stored blob data into: ", filename, "\n")

def inserir_bd(item):
    try:
        con = sqlite3.connect('catalogo.db')
        cur = con.cursor()
        cur.execute('insert into prod_cliente (codpro, descricao, embalagem, preco_cx, preco_un, cod_barras, categoria) values (?,?,?,?,?,?,?)',item,)
        con.commit()
        #print(f'Item {item[0]} incluso com sucesso.')
        cur.close()
        con.close()
    except sqlite3.Error as erro:
        print(f'Erro na inclusão {item[0]}.',erro)

def contar_itens():
    con = sqlite3.connect('catalogo.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM prod_cliente',)
    print(f'Quantidade de itens inseridos no catálogo: {len(cur.fetchall())}')
    cur.close()
    con.close()

def inserir_imagem(item):
    try:
        con = sqlite3.connect('catalogo.db')
        cur = con.cursor()
        dados = (None,item[6], item[0])
        cur.execute('INSERT INTO produtos (cod_barras, imagem, codcli) values (?, ?, ?)',dados,)
        con.commit()
        print(f'Código {item[0]} atualizado com sucesso.')
        cur.close()
        con.close()

    except sqlite3.Error as erro:
        print(f'Erro na atualização {item[0]}.',erro)

def atualizar_bd(item):
    try:
        con = sqlite3.connect('catalogo.db')
        cur = con.cursor()
        #soh atualiza com preco diferente
        # dados = (item[1],item[2], item[3], item[4],item[5], item[6], item[0],item[3])
        # cur.execute('UPDATE prod_cliente SET descricao = ?, embalagem = ?, preco_cx = ?, preco_un = ?, cod_barras = ?, categoria = ? WHERE codpro = ? and preco_cx != ?',dados,)
        #atualiza tudo
        dados = (item[1],item[2], item[3], item[4],item[5], item[6], item[0])
        cur.execute('UPDATE prod_cliente SET descricao = ?, embalagem = ?, preco_cx = ?, preco_un = ?, cod_barras = ?, categoria = ? WHERE codpro = ?',dados,)
        con.commit()
        print(f'Código {item[0]} atualizado com sucesso.')
        cur.close()
        con.close()

    except sqlite3.Error as erro:
        print(f'Erro na atualização {item[0]}.',erro)

def ler_arquivo():
    with open ('produtos.txt', 'r') as f:
        lista = []

        for row in csv.reader(f,delimiter=';'):
            lista.append(row)

        for linha in lista:
            item = []
            preco_novo = linha[6].replace(',','.')
            preco_novo = "{:.2f}".format(float(preco_novo))
            ##Troca , por .
            preco_novo_un = linha[8].replace(',','.')
            ##tranforma para numero real com 2 digitos apos o ponto

            preco_novo_un = "{:.2f}".format(float(preco_novo_un))
            # if preco_novo_un == '0.00':
            #     print("Código: " + linha[0] + " Descrição: " + linha[1] + " Emb: " + linha[3] + " Preço un: R$ " + str(
            #         preco_novo))
            # else:
            #     print("Código: "+linha[0]+" Descrição: "+linha[1]+" Emb: "+linha[3]+" Preço cx: R$ "+str(preco_novo)+ " Preço un: R$ "+str(preco_novo_un))

            item.append(linha[0])
            item.append(linha[1])
            item.append(linha[3])
            item.append(linha[6])
            if linha[8] !='0':
                item.append(linha[8])
            else:
                item.append(linha[6])
            item.append(0000000000000) #codigo de barras
            categoria = linha[11].split(' ')
            #print(categoria[1])
            
            #Coloca os nomes das categorias no BD
            #categoria = linha[11]
            if categoria[1] == 'ADAMS' or categoria[1] == 'ARCOR' or categoria[1] == 'CAMPESTRE' or categoria[1] == 'DALVA' or categoria[1] == 'DORI' or categoria[1] == 'AMENDUPA' or categoria[1] == 'FINI' or categoria[1] == 'FLORESTAL' or categoria[1] == 'Jazam' or categoria[1] == 'LUIZ' or categoria[1] == 'PECCIN' or categoria[1] == 'RICLAN' or categoria[1] == 'SANTA' or categoria[1] == 'Uniao'  or categoria[1] == 'GAROTO'  or categoria[1] == 'Quero' or categoria[1] == 'NESTLE':
                item.append('DOCES e SALGADINHOS')
                #categoria[1]= 'DOCES e SALGADINHOS'
            elif categoria[1] == 'BDL' or categoria[1] == 'ADN' or categoria[1] == 'BIC' or categoria[1] == 'DEYCON' or categoria[1] == 'FEIJAO' or categoria[1] == 'ERVA' or categoria[1] == 'FEIJAO' or categoria[1] == 'GERAL' or categoria[1] == 'KRAFT' or categoria[1] == 'LIMPINHA' or categoria[1] == 'MARANATA' or categoria[1] == 'MARTINS' or categoria[1] == 'MEMPHIS' or categoria[1] =='OWENS-ILLINOIS'  or categoria[1] == 'VASSOURAS'  or categoria[1] == 'ZETTAPACK'or categoria[1] == 'TELL'or categoria[1] == 'ODERICH' or categoria[1] == 'Mococa' or categoria[1] == 'Queijo' :
                item.append('MERCEARIA')
                #categoria[1] == 'MERCEARIA'
            elif categoria[1] == 'FONT'  or categoria[1] == 'BEBIDAS'  or categoria[1] == 'PINGO'  or categoria[1] == 'SUCO':
                item.append('BEBIDAS')
                #categoria[1] == 'BEBIDAS'
            elif categoria[1] == 'GIRANDO' or categoria[1] == 'SANY' or categoria[1] == 'BRILHOLAC':
                #categoria[1] == 'GIRANDO SOL'
                item.append('LIMPEZA')
            elif categoria[1] == 'DU':
                #categoria[1] == 'CONDIMENTOS'
                item.append('CONDIMENTOS')                
            elif categoria[1] == 'ELMA':
                #categoria[1] == 'ELMA CHIPS'
                item.append('ELMA CHIPS')
            elif categoria[1] == 'Biscoitos':
                item.append('Biscoitos SAGRA')                
            elif categoria[1] == 'TUBARAO'  or categoria[1] == 'SIRIUS'  or categoria[1] == 'HIGIE'  or categoria[1] == 'TISCOSKI'  or categoria[1] == 'GREEN' or categoria[1] == 'FRALDA':
                #categoria[1] == 'HIGIENE PESSOAL'
                item.append('HIGIENE PESSOAL')                
            elif categoria[1] == 'MC'  or categoria[1] == 'ORLEPLAST'  or categoria[1] == 'PLAZAPEL'  or categoria[1] == 'LIPLAST'  or categoria[1] == 'TOTALPLAST'or categoria[1] == 'EMBRAST'or categoria[1] == 'VABENE':
                #categoria[1] == 'DESCARTÁVEIS'
                item.append('DESCARTÁVEIS')                
            elif categoria[1] == 'MULTINACIONAL' or categoria[1] == 'PLASCOR'  or categoria[1] == 'RELUZ' or categoria[1] == 'OUROLUX' or categoria[1] == 'PARANA'or categoria[1] == 'PIRISA' or categoria[1] == 'BLUMENAU' or categoria[1] == 'Alcool' or categoria[1] == 'CARVAO' or categoria[1] == 'THREE' or categoria[1] == 'FIBRAFORM':
                #categoria[1] == 'UTILIDADES'
                item.append('BAZAR E UTILIDADES')
            else:
                item.append(categoria[1])
            #Aqui insere todos os itens novamente
            inserir_bd(item)

            #Aqui eh pra usar opcao de atualizar os preços
            #atualizar_bd(item)

            #img = convertToBinaryData('img/semfoto.jpg')
            #item.append(img)
            #inserir_imagem(item)

def listar_produtos():
    try:
        con = sqlite3.connect('catalogo.db')
        cur = con.cursor()
        produtos=[]
#        cur.execute('SELECT codpro, descricao, categoria, embalagem, preco_cx, preco_un FROM prod_cliente ORDER BY categoria, descricao')
        cur.execute(
            'SELECT codpro, descricao, categoria, embalagem, preco_cx, preco_un, categoria FROM prod_cliente WHERE categoria NOT Null ORDER BY categoria, descricao')
        produtos = cur.fetchall()
        cur.close()
        con.close()
        return produtos
    except sqlite3.Error as erro:
        print('Erro na consulta.',erro)

def apagar_itens_cliente():
    try:
        con = sqlite3.connect('catalogo.db')
        cur = con.cursor()
        cur.execute(
            'DELETE FROM prod_cliente')
        print(f'Total de itens apagados: {cur.rowcount}')
        con.commit()
        cur.close()
        con.close()
    except sqlite3.Error as erro:
        print('Erro ao apagar itens do banco.',erro)

if __name__ == '__main__':
    apagar_itens_cliente()
    ler_arquivo()
    contar_itens()
    #tt = []
    #tt.append('2327')
    #consultar_imagem(tt)
