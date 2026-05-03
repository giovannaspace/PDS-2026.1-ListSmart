from flask import Flask, render_template, request, redirect, session,url_for


from backend import *

app = Flask(__name__)
app.secret_key = "segredo"



bancoDados()
gerente = GerenciamentoCategoria()
gerente.categoria()
gerente.dicionario()


# ================= LOGIN =================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = Usuario.login(email, senha)

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

        resultado = cadastro(nome,email,senha)
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
    
    listas = buscarLista(session["idUsuario"])

    for lista in listas:
        lista["quantidade"] = contarItens(lista["id"])

    return render_template("listas.html",listas=listas)

@app.route("/criarLista", methods=["GET","POST"])
def criarLista():
    if request.method == "POST":
        nome = request.form["nomeLista"]
        teto = request.form["teto"]
        idUsuario = session["idUsuario"]
        obs = request.form["observacoes"]

        novaLista = Lista(nomeLista=nome, tetoOrcamentario=teto, observacoes=obs,idDono=idUsuario)
        ListaNovaBD(novaLista)

        return redirect(url_for("listas"))

    categorias = gerente.sugestaoNomeLista()

    return render_template("telaCriarLista.html",categorias=categorias)

@app.route("/itens/<idLista>")
def itens(idLista):

    listaRec = Lista.recontruirLista(idLista)
    marcados = listaRec.calcularTotalMarcados() or 0
    pendentes = listaRec.calcularTotalPendentes() or 0
    totalGeral = listaRec.calcularTotalGeral() or 0

    tetoInfo = listaRec.calcularTetoOrcamentario()

    itens = listaRec.itensDaLista()

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

        if temPromo == "sim":
            if tipo == "porcentagem":
                porcentagem = int(request.form.get("porcentagem") or 0)
                Lista.adicionarItem(idLista,nome, qtd, unidade, preco,obs,categoria,"s",1,0,0,porcentagem)

            elif tipo == "leve":
                x = int(request.form.get("leveX") or 0)
                y = int(request.form.get("pagueY") or 0)
                Lista.adicionarItem(idLista,nome, qtd, unidade, preco,obs,categoria,"s",2,x,y,0)
        else:
            Lista.adicionarItem(idLista,nome, qtd, unidade, preco,obs,categoria,"n",0,0,0,0)

        return redirect(url_for("itens",idLista=idLista))
                
    categorias = gerente.sugestaoNomeLista()
    catItens = gerente.sugestaoNomeItem()
    return render_template("telaCriarItem.html",categorias=categorias,catItens=catItens,idLista=idLista)


@app.route("/marcarItem/<idLista>", methods=["GET","POST"])
def marcarItem(idLista):

    idItem = request.form["idItem"]

    listaRec = Lista.recontruirLista(idLista)
    listaRec.alterarStatus(idItem)

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

        
        if nome:
            itemRec.atualizarItem("nome", nome)

        if unidade:
            itemRec.atualizarItem("unidade", unidade)

        if preco:
            itemRec.atualizarItem("preco", float(preco))

        if nota:
            itemRec.atualizarItem("nota", nota)

        import sqlite3
        conexao = sqlite3.connect("banco.db")
        cursor = conexao.cursor()

        if quantidade:
            cursor.execute("""
                UPDATE itens SET quantidade = ?
                WHERE idItem = ? AND idDonoItem = ?
            """, (int(quantidade), itemRec.idItem, itemRec.idDonoItem))

        if categoria:
            cursor.execute("""
                UPDATE itens SET idCategoria = ?
                WHERE idItem = ? AND idDonoItem = ?
            """, (categoria, itemRec.idItem, itemRec.idDonoItem))

        conexao.commit()
        conexao.close()

        return redirect(url_for("listas"))

    return render_template("item.html", itemRec=itemRec)

@app.route("/item/deletar/<idItem>", methods=["POST"])
def deletarItem(idItem):

    itemRec = Item.reconstruirItem(idItem)

    if itemRec:
        itemRec.removerItem()

    return redirect(url_for("listas"))

@app.route("/compartilhar/email/<idLista>", methods=["POST"])
def compartilhar_email(idLista):
 
    listaRec = Lista.recontruirLista(idLista)

    email = request.form.get("email")

    comp = compartilhamento(listaRec)
    comp.enviarEmail(email)

    return redirect(url_for("listas", idLista=idLista))


@app.route("/compartilhar/zap/<idLista>", methods=["POST"])
def compartilhar_zap(idLista):

    listaRec = Lista.recontruirLista(idLista)

    numero = request.form.get("numero")

    comp = compartilhamento(listaRec)
    comp.enviarZap(numero)

    return redirect(url_for("listas", idLista=idLista))

if __name__ == "__main__":
    app.run(debug=True)
