import sqlite3
import uuid
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self,nomeItem, quantidade, unidade, precoUnitario,observacoesItem,categorias,idDonoItem,desconto,statusCompra,idItem=None):

        self.nomeItem = nomeItem
        self.quantidade = quantidade
        self.unidade = unidade
        self.precoUnitario = precoUnitario
        self.desconto = desconto
        self.observacoesItem = observacoesItem
        self.statusCompra = statusCompra
        self.idItem = idItem if idItem else str(uuid.uuid4())
        self.idDonoItem = idDonoItem
        self.categorias = categorias


    @abstractmethod
    def calcularPreco():
        pass

    @staticmethod
    def paraTuplas(linhas):
        if linhas[5] == 0 or linhas[5] is None:
                return ItemComum(linhas[1],linhas[2], linhas[3], linhas[4], linhas[8], linhas[9], linhas[7],linhas[5],linhas[6], linhas[0])

        else:
                return ItemPromocional(linhas[1],linhas[2], linhas[3], linhas[4], linhas[8], linhas[9], linhas[7],linhas[5],linhas[6], linhas[0])

    @staticmethod
    def reconstruirItem(idItem):
        conexao = sqlite3.connect("banco.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM itens WHERE idItem = ?", (idItem,))
        linha = cursor.fetchone()
        conexao.close()

        if not linha:
            return None

        itemRec = Item.paraTuplas(linha)
        return itemRec

    def atualizarItem(self,campo,valorNovo):
        
        conexao = sqlite3.connect("banco.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        
        if campo == "nome":
            cursor.execute("UPDATE itens SET nomeItem = ? WHERE idItem = ? AND idDonoItem = ?", (valorNovo,self.idItem,self.idDonoItem))
            conexao.commit()
            self.nomeItem = valorNovo
            

        elif campo == "nota":
            cursor.execute("UPDATE itens SET observacoesItem = ? WHERE idItem = ? AND idDonoItem = ?", (valorNovo,self.idItem,self.idDonoItem))
            conexao.commit()
            self.observacoesItem = valorNovo
            

        elif campo == "preco":
            cursor.execute("UPDATE itens SET precoUnitario = ? WHERE idItem = ? AND idDonoItem = ?", (valorNovo,self.idItem,self.idDonoItem))
            conexao.commit()
            self.precoUnitario = valorNovo
            
        
        elif campo == "unidade":
            cursor.execute("UPDATE itens SET unidade  = ? WHERE idItem = ? AND idDonoItem = ?", (valorNovo,self.idItem,self.idDonoItem))
            conexao.commit()
            self.unidade = valorNovo
            

        else:
            conexao.close()
            return
        
        conexao.close()
  
    def removerItem(self):
        conexao = sqlite3.connect("banco.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM itens WHERE idDonoItem = ? AND idItem = ?", (self.idDonoItem,self.idItem))

        conexao.commit()
        conexao.close()
    
    def quantidadeItem(self, opecacao):
        conexao = sqlite3.connect("banco.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("SELECT quantidade FROM itens WHERE idDonoItem = ? AND idItem = ?",(self.idDonoItem,self.idItem))
        item = cursor.fetchone()
        conexao.close()

        if item:
            quantidade = item[0]
        else:
            return None

        if opecacao == "+":
        
                conexao = sqlite3.connect("banco.db")
                cursor = conexao.cursor()

                quantidadeNova = quantidade + 1
                cursor.execute("UPDATE itens SET quantidade = ? WHERE idDonoItem = ? AND idItem = ?",
                                (quantidadeNova,self.idDonoItem, self.idItem))
                conexao.commit()
                conexao.close()

        elif opecacao == "-":
            
                if quantidade == 1:
                        
                    self.removerItem()

                elif quantidade > 1:

                    conexao = sqlite3.connect("banco.db")
                    cursor = conexao.cursor()

                    quantidadeNova = quantidade - 1
                    cursor.execute("UPDATE itens SET quantidade = ? WHERE idDonoItem = ? AND idItem = ?",
                                    (quantidadeNova,self.idDonoItem, self.idItem))
                    conexao.commit()
                    conexao.close()



class ItemComum(Item):
    def __init__(self,nomeItem, quantidade, unidade, precoUnitario,observacoesItem,categorias,idDonoItem,desconto,statusCompra,idItem=None):
        super().__init__(nomeItem, quantidade, unidade, precoUnitario,observacoesItem,categorias,idDonoItem,desconto,statusCompra,idItem=idItem)

    def calcularPreco(self):
        return self.quantidade * self.precoUnitario

class ItemPromocional(Item):
    def __init__(self,nomeItem, quantidade, unidade, precoUnitario,observacoesItem,categorias,idDonoItem,desconto,statusCompra,idItem=None):
        super().__init__(nomeItem, quantidade, unidade, precoUnitario,observacoesItem,categorias,idDonoItem,desconto,statusCompra,idItem=idItem)


        self.desconto = desconto

    def calcularPreco(self):
    
        if self.desconto >= 0:

            precoComDesconto = self.precoUnitario - self.desconto
            return self.quantidade * precoComDesconto
        
        else:
            valor = abs(self.desconto)

            x = int(valor // 1000)
            y = valor % 1000

            qtd_promo = self.quantidade  // x
            resto = self.quantidade - (x * qtd_promo)

            valorFinal = (resto * self.precoUnitario) + (qtd_promo * y)

            return valorFinal