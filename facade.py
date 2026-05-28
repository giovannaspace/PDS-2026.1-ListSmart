from backend import *
from classes_dados import *
from observer import *
from builder import *

######################## IMPLEMENTAÇÃO DESIGN PATTERN ESTRUTURAL FACADE ########################

class Facade():

    @staticmethod # pode chamar sem precisar instanciar antes
    def login_facade(email,senha):
        usuario = Usuario.login(email, senha)  # chama o metodo de verificação na classe Usuario
        return usuario
    
    @staticmethod
    def cadastro_facade(nome,email,senha):
        usuario = cadastro(nome,email,senha)
        return usuario

    @staticmethod
    def listas_facade(idUsuario):

        listas = buscarLista(idUsuario) #idUsuario extraido do parametro passado pelo flask (sessions["idUsuario"])
        for lista in listas:
            lista["quantidade"] = contarItens(lista["id"])

        return listas
    
    @staticmethod
    def criarListas_facade(nome,teto,obs,idUsuario):
        nova_lista = Lista(nomeLista=nome, tetoOrcamentario=teto, observacoes=obs,idDono=idUsuario)
        
        # ADD NO BANCO DE DADOS
        ListaNovaBD(nova_lista)

    @staticmethod
    def sugestao_categoriaLista_facade():
        gerente = GerenciamentoCategoria()
        categorias = gerente.sugestaoNomeLista()
        return categorias
    
    @staticmethod
    def sugestao_categoriaItem_facade():
        gerente = GerenciamentoCategoria()
        catItens = gerente.sugestaoNomeItem()
        return catItens

    @staticmethod
    def itens_facade(idLista):

        listaRec = Lista.recontruirLista(idLista)
        marcados = listaRec.calcularTotalMarcados() or 0
        pendentes = listaRec.calcularTotalPendentes() or 0
        totalGeral = listaRec.calcularTotalGeral() or 0

        tetoInfo = listaRec.calcularTetoOrcamentario()

        itens = listaRec.itensDaLista()

        return listaRec,marcados,pendentes,totalGeral,tetoInfo,itens



    @staticmethod
    def criarItem_facade(idLista, temDesconto,nome,qtd,unidade,preco,categoria,obs,tipo,porcentagem,x,y):
        builder = itemBuilder()
        
        if temDesconto == 1:
            # porcentagem
            if tipo == 1:
                desconto_calculo = tipoDesconto(preco,1,0,0,porcentagem)
                 # debug print(desconto_calculo)
                director = builderDirector(builder, nome, qtd, unidade, preco, obs, categoria, idLista, desconto_calculo, 0)

                item = director.get_Promo()
                ItemNovaBD(item)

            # leve X pague Y
            else:
                desconto_calculo = tipoDesconto(preco,2,x,y,0)
                director = builderDirector(builder, nome, qtd, unidade, preco, obs, categoria, idLista, desconto_calculo, 0)
                item = director.get_Promo()
                ItemNovaBD(item)
        
        else:
            director = builderDirector(builder, nome, qtd, unidade, preco, obs, categoria, idLista, 0, 0)

            #director = builderDirector(builder,nome,qtd,unidade,preco,0,obs,0,idLista,categoria)
            item = director.get_Comum()
            ItemNovaBD(item) # antes estava no metodo adicionarItem da classe Lista

            #Lista.adicionarItem(idLista,nome, qtd, unidade, preco,obs,categoria,"n",0,0,0,0)
           
    @staticmethod
    def marcar_item_facade(idLista,idItem):

        listaRec = Lista.recontruirLista(idLista)
        listaRec.alterarStatus(idItem)

    
    @staticmethod
    def item_caracteristicas_facade(idItem,nome,quantidade,unidade,preco,categoria,nota):
        itemRec = Item.reconstruirItem(idItem)

        if nome:
            itemRec.atualizarItem("nome", nome)

        if unidade:
            itemRec.atualizarItem("unidade", unidade)

        if preco:
            itemRec.atualizarItem("preco", float(preco))

        if nota:
            itemRec.atualizarItem("nota", nota)

# para quantidade e categoria (função separada no banco de dados):
        atualizar_quant_e_categoria(itemRec,quantidade,categoria)


    @staticmethod
    def deletar_item_facade(idItem):
        itemRec = Item.reconstruirItem(idItem)

        if itemRec:
            itemRec.removerItem()        
    

    @staticmethod
    def email_facade(idLista,email):
        listaRec = Lista.recontruirLista(idLista)
        comp = compartilhamento(listaRec)
        comp.enviarEmail(email)


    @staticmethod
    def zap_facade(idLista,numero):
        listaRec = Lista.recontruirLista(idLista)
        comp = compartilhamento(listaRec)
        comp.enviarZap(numero)
