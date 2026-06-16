from flask import Flask, render_template, request, redirect, session,url_for
from backend import *

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")



bancoDados()
gerente = GerenciamentoCategoria()
gerente.categoria()
gerente.dicionario()

from facade import *

# ================= LOGIN =================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        # CHAMADA FACADE
        usuario = Facade.login_facade(email,senha)

        if usuario:
            session["idUsuario"] = usuario.idUsuario
            return redirect(url_for("listas"))
        else:
            return "Login inválido"

    return render_template("login.html")




# ================= CADASTRO =================
@app.route("/cadastro", methods=["GET","POST"])
def cadastroView():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        # CHAMADA FACADE
        resultado = Facade.cadastro_facade(nome,email,senha)

        if resultado:
            return redirect(url_for("login"))
        else:
            return "Erro ao cadastrar (email já existe ou inválido)"
    
    return render_template("cadastro.html")

# ================= AMBIENTE LOGADO =================
##Tela de mostrar as listas do usuário 
@app.route("/listas")
def listas():
    if "idUsuario" not in session:
        return redirect("/")
    
    # CHAMADA FACADE
    listas = Facade.listas_facade(session["idUsuario"])

    return render_template("listas.html",listas=listas)

@app.route("/criarLista", methods=["GET","POST"])
def criarLista():
    if request.method == "POST":
        nome = request.form["nomeLista"]
        teto = request.form["teto"]
        idUsuario = session["idUsuario"]
        obs = request.form["observacoes"]

        # CHAMADA FACADE
        Facade.criarListas_facade(nome,teto,obs,idUsuario)
        #novaLista = Lista(nomeLista=nome, tetoOrcamentario=teto, observacoes=obs,idDono=idUsuario)
        #ListaNovaBD(novaLista)

        return redirect(url_for("listas"))

    #categorias = gerente.sugestaoNomeLista()
    categorias = Facade.sugestao_categoriaLista_facade()
    return render_template("telaCriarLista.html",categorias=categorias)

@app.route("/itens/<idLista>")
def itens(idLista):

    listaRec,marcados,pendentes,totalGeral,tetoInfo,itens = Facade.itens_facade(idLista)
   # listaRec = Lista.recontruirLista(idLista)
   # marcados = listaRec.calcularTotalMarcados() or 0
   # pendentes = listaRec.calcularTotalPendentes() or 0
   # totalGeral = listaRec.calcularTotalGeral() or 0

   # tetoInfo = listaRec.calcularTetoOrcamentario()

   # itens = listaRec.itensDaLista()

    return render_template("itens.html",lista=listaRec, itens=itens,idLista=idLista,marcados=marcados,pendentes=pendentes,totalGeral=totalGeral,tetoInfo=tetoInfo)

@app.route("/criarItem/<idLista>", methods=["GET","POST"])
def criarItem(idLista):

    if request.method == "POST":
        nome = request.form["nomeItem"]
        qtd = int(request.form["quantidade"])
        unidade = request.form["unidade"]
        preco = float(request.form["preco"])
        categoria = request.form["categoria"]
        obs = request.form["observacao"]

        temPromo = request.form["temPromocao"]
        tipo = request.form.get("tipoPromocao")

    #    builder = itemBuilder()

        if temPromo == "sim":

            if tipo == "porcentagem":  #tipo 1
                
                # CHAMADA FACADE
                porcentagem = int(request.form.get("porcentagem") or 0)
                Facade.criarItem_facade(idLista,1,nome,qtd,unidade,preco,categoria,obs,tipo,porcentagem,0,0)


                #desconto_calculo = tipoDesconto(preco,1,0,0,porcentagem)
                 # debug print(desconto_calculo)
                #director = builderDirector(builder, nome, qtd, unidade, preco, obs, categoria, idLista, desconto_calculo, 0)

                #director = builderDirector(builder,nome,qtd,unidade,preco,desconto_calculo,obs,0,idLista,categoria)
                    #item = director.get_Promo()
                    #ItemNovaBD(item) # antes estava no metodo adicionarItem da classe Lista
                #Lista.adicionarItem(idLista,nome, qtd, unidade, preco,obs,categoria,"s",1,0,0,porcentagem)

            elif tipo == "leve": #tipo 2
                x = int(request.form.get("leveX") or 0)
                y = int(request.form.get("pagueY") or 0)

                # CHAMADA FACADE
                Facade.criarItem_facade(idLista,1,nome,qtd,unidade,preco,categoria,obs,tipo,0,x,y)



              #  desconto_calculo = tipoDesconto(preco,2,x,y,0)

                # debug print(desconto_calculo)
             #   director = builderDirector(builder, nome, qtd, unidade, preco, obs, categoria, idLista, desconto_calculo, 0)
                #director = builderDirector(builder,nome,qtd,unidade,preco,desconto_calculo,obs,0,idLista,categoria)
            #    item = director.get_Promo()
               # ItemNovaBD(item) # antes estava no metodo adicionarItem da classe Lista

                #Lista.adicionarItem(idLista,nome, qtd, unidade, preco,obs,categoria,"s",2,x,y,0)
        else:
            # CHAMADA FACADE
            Facade.criarItem_facade(idLista,0,nome,qtd,unidade,preco,categoria,obs,tipo,0,0,0)


        return redirect(url_for("itens",idLista=idLista))
                
   # categorias = gerente.sugestaoNomeLista()
   # catItens = gerente.sugestaoNomeItem()

    # CHAMADA FACADE
    categorias = Facade.sugestao_categoriaLista_facade()
    catItens = Facade.sugestao_categoriaItem_facade()
    return render_template("telaCriarItem.html",categorias=categorias,catItens=catItens,idLista=idLista)


@app.route("/marcarItem/<idLista>", methods=["GET","POST"])
def marcarItem(idLista):

    idItem = request.form["idItem"]

    # CHAMADA FACADE
    Facade.marcar_item_facade(idLista,idItem)
   # listaRec = Lista.recontruirLista(idLista)
   # listaRec.alterarStatus(idItem)

    return redirect(url_for("itens",idLista=idLista))

@app.route("/item/<idItem>", methods=["GET", "POST"])
def item(idItem):

    itemRec = Item.reconstruirItem(idItem)

    if request.method == "POST":

        nome = request.form.get("nome")
        quantidade = request.form.get("quantidade")
        unidade = request.form.get("unidade")
        preco = request.form.get("preco")
        categoria = request.form.get("categoria")
        nota = request.form.get("nota")

        # CHAMADA FACADE
        Facade.item_caracteristicas_facade(idItem,nome,quantidade,unidade,preco,categoria,nota)
        #atualizar_quant_e_categoria(itemRec,quantidade,categoria)

        return redirect(url_for("listas"))

    return render_template("item.html", itemRec=itemRec)

@app.route("/item/deletar/<idItem>", methods=["POST"])
def deletarItem(idItem):

   # itemRec = Item.reconstruirItem(idItem)

    #if itemRec:
     #   itemRec.removerItem()
    # CHAMADA FACADE
    Facade.deletar_item_facade(idItem)
    return redirect(url_for("listas"))

@app.route("/compartilhar/email/<idLista>", methods=["POST"])
def compartilhar_email(idLista):
 
    #listaRec = Lista.recontruirLista(idLista)

    email = request.form.get("email")
    # CHAMADA FACADE
    Facade.chamada_observer_facade(idLista,email,0,2)

    #Facade.email_facade(idLista,email)
    
    
    
    #comp = compartilhamento(listaRec)
    #comp.enviarEmail(email)

    return redirect(url_for("listas", idLista=idLista))


@app.route("/compartilhar/zap/<idLista>", methods=["POST"])
def compartilhar_zap(idLista):

    #listaRec = Lista.recontruirLista(idLista)

    numero = request.form.get("numero")

    Facade.chamada_observer_facade(idLista,0,numero,1)
   # Facade.zap_facade(idLista,numero)
    
    
    
    #comp = compartilhamento(listaRec)
    #comp.enviarZap(numero)

    return redirect(url_for("listas", idLista=idLista))

if __name__ == "__main__":
    app.run(debug=True)
