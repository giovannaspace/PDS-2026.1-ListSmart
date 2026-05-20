from abc import ABC, abstractmethod
from classes_dados import ItemComum,ItemPromocional

######################## IMPLEMENTAÇÃO DESIGN PATTERN CRIACIONAL BUILDER ########################

# ETAPA 1: DEFINIÇÃO DOS MÉTODOS DE ACORDO COM OS ATRIBUTOS DO ITEM -> INTERFACE DO BUILDER
class metodosBuilder(ABC):
    @abstractmethod
    def definir_nome(self, nome):
        pass

    @abstractmethod
    def definir_quantidade(self,quantidade):
        pass

    @abstractmethod
    def definir_unidade(self,unidade):
        pass

    @abstractmethod
    def definir_preco(self,preco):
        pass

    @abstractmethod
    def definir_desconto(self,desconto):
        pass

    @abstractmethod
    def definir_observacoes(self,observacoes):
        pass

    @abstractmethod
    def definir_status(self,status):
        pass

    @abstractmethod  
    def definir_dono(self,dono):  
        pass

    @abstractmethod
    def definir_categoria(self,categoria):
        pass


    @abstractmethod
    def get_itemComum(self):
        pass

    @abstractmethod
    def get_itemPromo(self):
        pass


'''
    @abstractmethod
    def definir_x(self,x):
        pass
    
    @abstractmethod
    def definir_y(self,y):
        pass
    
    @abstractmethod
    def definir_porcentagem(self,porcentagem):
        pass

    @abstractmethod
    def definir_tipoDesconto(self,tipo_desconto):
        pass
'''

# ETAPA 2: IMPLEMENTAÇÃO DOS MÉTODOS

class itemBuilder(metodosBuilder):

    def __init__(self):
        self.nome = None
        self.quantidade = None
        self.unidade = None
        self.preco = None
        self.desconto = None
        self.observacoes = None
        self.status = None
        self.dono = None
        self.categoria = None

    
    def definir_nome(self,nome):
        self.nome = nome
        return self
    
    def definir_quantidade(self,quantidade):
        self.quantidade = quantidade
        return self

    def definir_unidade(self,unidade):
        self.unidade = unidade
        return self

    def definir_preco(self,preco):
        self.preco = preco
        return self

    def definir_desconto(self,desconto):
        self.desconto = desconto
        return self

    def definir_observacoes(self,observacoes):
        self.observacoes = observacoes
        return self

    def definir_status(self,status):
        self.status = status
        return self

    def definir_dono(self,dono):  #duvida
        self.dono = dono
        return self

    def definir_categoria(self,categoria):
        self.categoria = categoria
        return self
    
    def get_itemComum(self):
        return ItemComum(self.nome,self.quantidade,self.unidade,self.preco,self.observacoes,self.categoria,self.dono,0,self.status)
    
    def get_itemPromo(self):
        return ItemPromocional(self.nome,self.quantidade,self.unidade,self.preco,self.observacoes,self.categoria,self.dono,self.desconto,self.status)


'''
    def definir_x(self,x):
        self.x = x
        return self
    
    def definir_y(self,y):
        self.y = y
        return self
    
    def definir_porcentagem(self,porcentagem):
        self.porcentagem = porcentagem
        return self
    
    def definir_tipoDesconto(self,tipo_desconto):
        self.tipo_desconto = tipo_desconto
        return self
'''

    

# ETAPA 3: ESTABELECER AS CONSTRUÇÕES (ordem da chamada dos métodos etc)

class builderDirector():

    # recebe o builder criado pelo client
    def __init__(self,builder,nome,quantidade,unidade,preco,observacao,categoria,dono,desconto,status):
        self.builder = builder # uso dos metodos implementados
        self.nome = nome
        self.quantidade = quantidade
        self.unidade = unidade
        self.preco = preco
        self.observacao = observacao
        self.categoria = categoria
        self.dono = dono
        self.desconto = desconto
        self.status = status
    
    def get_Comum(self):
        # retornar resultado para o client
        return self.builder.definir_nome(self.nome)\
            .definir_quantidade(self.quantidade)\
            .definir_unidade(self.unidade)\
            .definir_preco(self.preco)\
            .definir_observacoes(self.observacao)\
            .definir_status(self.status)\
            .definir_dono(self.dono)\
            .definir_categoria(self.categoria)\
            .get_itemComum()

    def get_Promo(self):
        # retornar resultado para o client
        return self.builder.definir_nome(self.nome)\
            .definir_quantidade(self.quantidade)\
            .definir_unidade(self.unidade)\
            .definir_preco(self.preco)\
            .definir_desconto(self.desconto)\
            .definir_observacoes(self.observacao)\
            .definir_status(self.status)\
            .definir_dono(self.dono)\
            .definir_categoria(self.categoria)\
            .get_itemPromo()
        
