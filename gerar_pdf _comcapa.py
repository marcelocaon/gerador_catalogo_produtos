import fpdf

import main as main
from fpdf import FPDF
from pathlib import Path

title = 'Catálogo de Produtos'

class PDF(FPDF):
    def capa(self):
        self.add_page()

        # Arial 12
        self.set_font('Arial', 'B', 50)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Text color
        self.set_text_color(0,0,0)
        # Calculate width of title and position
        w = self.get_string_width('Catálogo de Produtos') + 6
        self.set_x((210 - w) / 2)
        self.ln(50)
        self.cell(w, 9, 'Catálogo de Produtos', 0, 1, 'C', 0)
        #self.multi_cell(0,5,'Catálogo de Produtos', 'C','')

        self.image('img/logo.jpg', 35, 100, 150)



        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Text color
        self.set_text_color(0,0,0)
        self.ln(180)
        self.multi_cell(0,5,'Rua Gisela, 1233 - Bela Vista, São José / SC','')
        self.multi_cell(0,5,'email: sd.distribuidora.sc@gmail.com','')
        self.multi_cell(0,5,'(48) 3094-0788 e (48) 99190-4134','')
    
    def header(self):
        #se for a primeira pagina (capa) entao nao imprime o cabecalho
        if self.page_no() != 1:
            # Logo
            self.image('img/logo.jpg', 10, 8, 15)
            # Arial bold 15
            self.set_font('Arial', 'B', 25)
            # Calculate width of title and position
            w = self.get_string_width(title) + 6
            self.set_x((210 - w) / 2)
            # Colors of frame, background and text
            self.set_draw_color(255, 255, 255) #cor da borda = branca
            self.set_fill_color(255, 255, 255) #cor do preenchimento da celula = branca
            self.set_text_color(220, 50, 50)
            self.rect(5,205,5,265)
            # Thickness of frame (1 mm)
            #self.set_line_width(1)

            # Title
            self.cell(w, 9, title, 1, 1, 'C', 1)
            # Line break
            self.ln(10)

    def footer(self):
        #se for a primeira pagina (capa) entao nao imprime o rodape
        if self.page_no() != 1:
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            # Arial italic 8
            self.set_font('Arial', 'I', 8)
            # Text color in gray
            self.set_text_color(128)
            # Page number
            self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')
            # Borda da pagina
            self.set_draw_color(0, 0, 0) #cor do desenho para preto
            self.rect(5,5,200,280)

#descricao do produto
    # def chapter_title(self, num, label):
    #     # Arial 12
    #     self.set_font('Arial', '', 12)
    #     # Background color
    #     self.set_fill_color(200, 220, 255)
    #     # Title
    #     self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
    #     # Line break
    #     self.ln(4)

    def imprime_categoria(self, categoria):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Text color
        self.set_text_color(0,0,0)
        # Title
        self.cell(0, 6, categoria, 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # # Read text file
        # with open(name, 'rb') as fh:
        #     txt = fh.read().decode('latin-1')
        txt = 'Descrição do produto'
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        # self.set_font('', 'I')
        # self.cell(0, 5, '(end of excerpt)')

    # def print_chapter(self, num, title, name):
    #     self.add_page()
    #     self.chapter_title(num, title)
    #     self.chapter_body(name)

    def verifica_imagem(self,imagem):

        #verifica se o codigo do produto tem 5 digitos, se não completa com zeros a esquerda
        if len(str(imagem)) < 5:
            imagem = str(imagem).zfill(5)
        #verifica se a imagem existe no diretorio, caso não exista retorna uma imagem padrao
        path_to_file = 'fotos/'+str(imagem)+'.jpg'
        path = Path(path_to_file)
        path_to_file2 = 'fotos/'+str(imagem)+'.png'
        path2 = Path(path_to_file2)
        if path.is_file():
            return path_to_file        
        #elif path2.is_file():
            #return path_to_file2
        else:
            path_to_file = 'img/semfoto.jpg'
            return path_to_file

    def montar_relatorio(self, lista):
        print('inicio geracao relatorio')
        self.add_page()
        #pos_x = 20
        #pos_y = 30
        pos_y = 40  # devido ao titulo, posiciona a imagem mais embaixo
        categoria = ''
        for item in lista:
            if categoria == '':
                categoria = item[6]
                self.imprime_categoria(categoria)
                # self.cell(10, 50, categoria)
                # self.ln(15)
            else:
                if categoria != item[6]:
                    categoria = item[6]
                    self.add_page()
                    #como pulei pagina por causa da categoria, tenho que colocar a proxima posicao da imagem pra cima tbem
                    pos_y = 40 #devido ao titulo, posiciona a imagem mais embaixo
                    self.imprime_categoria(categoria)
                    # self.cell(10, 50, categoria)
                    # self.ln(15)

            if pos_y > 260:
                self.add_page()
                pos_y = 30
                img = self.verifica_imagem(item[0])
                #self.image('img/semfoto.jpg', 20, pos_y, 15)
                #image(name, x = None, y = None, w = 0, h = 0, type = '', link = '') w e h = 0, calcula automaticamente o tamanho da imagem
                self.image(img, 20, pos_y, 17, 0)
            else:
                img = self.verifica_imagem(item[0])
                #self.image('img/semfoto.jpg', 20, pos_y, 15)
                self.image(img, 20, pos_y, 17, 0)
            # Times 12
            self.set_font('Arial', 'B', 10)

            # Colors of frame, background and text
            self.set_draw_color(0, 0, 255)  # cor da borda
            self.set_fill_color(135, 206, 250)  # cor do preenchimento da celula
            # Thickness of frame (1 mm)
            self.set_line_width(0.1)

            # Output justified text = 0 / B = border na parte de baixo
            self.set_text_color(0, 0, 0) #cor preta da letra
            self.set_x(45)
            #self.multi_cell(130, 5, f'Cod: {str(item[0])}-{item[1][:50]}', fill=True) #limitei a 50 caracteres a descricao,
            self.multi_cell(130, 5, f'Cod: {str(item[0])}-{item[1][:45]}', fill=True) #limitei a 45 caracteres a descricao, pq coloquei a borda,

            #self.multi_cell(130, 5, f'Cod: {str(item[0])}-{item[1][:50]}','B') #limitei a 50 caracteres a descricao
            self.set_font('Arial', '', 10)
            self.set_text_color(220, 50, 50) #cor vermelha da letra
            self.set_x(45)
            preco_novo_cx = item[4].replace(',','.')
            preco_novo_un = item[5].replace(',','.')
            preco_cx = "{:.2f}".format(float(preco_novo_cx)) #dois digitos apos a virgula
            preco_un = "{:.2f}".format(float(preco_novo_un))

            # Colors of frame, background and text
            self.set_draw_color(255, 255, 255)  # cor da borda = branca
            self.set_fill_color(255, 255, 255)  # cor do preenchimento da celula = branca
            # Thickness of frame (1 mm)
            self.set_line_width(0)

            if item[5] != item[4]:
                self.multi_cell(0, 5, f'Emb: {item[3]} - Preço un: R$ {preco_un} - Preço cx: R$ {preco_cx}','')
            else:
                self.multi_cell(0, 5, f'Emb: {item[3]} - Preço un: R$ {preco_un}','')
            self.ln(10)
            #pos_x = pos_x + 10
            pos_y = pos_y + 20

        print('fim geracao relatorio')


lista_produtos = main.listar_produtos()
print(lista_produtos)
#0 = codigo
#1 = descricao
#2 = categoria
#3 = embalagem
#4 = preco cx
#5 = preco un
#6 = categoria

pdf = PDF()
pdf.set_title(title)
pdf.set_author('MG Labs')

pdf.capa()
pdf.montar_relatorio(lista_produtos)

#Capítulos podem ser as categorias dos produtos
# pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_c1.txt')
# pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')

#nome do arquivo, colocar catalogo + empresa
pdf.output('catalogo.pdf', 'F')
