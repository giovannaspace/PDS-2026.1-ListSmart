# 🛒 ListSmart – Gerenciador de Compras

Repositório desenvolvido para a disciplina de **Projeto de Software** – UFAL.

O **ListSmart** é um gerenciador de compras que ajuda o usuário a organizar listas de supermercado de forma simples, prática e eficiente.

---
## Implementação de design pattern criacional BUILDER (em andamento...)
👉 O Builder permite a construção de diferentes tipos de objetos passo a passo, a partir do mesmo código de construção.  
* Pode ser utilizado como uma opção mais compacta em relação ao construtor presente na relação de herança, assim como gerenciar as funções do banco de dados.
```
class Item(ABC)
class ItemComum(Item)
class ItemPromocional(Item)
```
* A implementação de uma **classe Builder** 



## 🚀 Funcionalidades

1. **Cadastro e Login**
   Permite criar conta e autenticar usuários no sistema.

2. **Criação de Listas**
   Possibilidade de nomear listas (ex: "Churrasco", "Compras do mês").

3. **Adição de Itens**
   Inserção de itens com nome, preço, quantidade e categoria.

4. **Marcar como Comprado**
   Alterna o status de compra dos itens.

5. **Categorias Automáticas**
   Sugestão de categorias pré-definidas.

6. **Compartilhamento**
   Envio da lista formatada por e-mail.

7. **Quantidade e Unidade**
   Definição de unidades de medida (kg, litro, unidade, etc.).

8. **Sugestões Inteligentes**
   Sugestão de itens com base em dados previamente cadastrados.

9. **Cálculo de Valores**

   * Total geral
   * Total de itens comprados
   * Total de itens pendentes

10. **Atualização de Dados**
    Permite editar informações de listas e itens.

---

## ⭐ Recursos Extras

### 💸 Sistema de Descontos

O usuário pode escolher entre:

* Item Comum
* Item Promocional

Tipos de desconto disponíveis:

* Porcentagem
* "Leve X e pague Y"

---

### 💰 Teto Orçamentário

Permite definir um valor máximo de gasto para a lista.

O sistema informa automaticamente:

* 🔴 Ultrapassou o limite
* 🟡 Atingiu exatamente o limite
* 🟢 Dentro do Orçamento

---

### 📲 Compartilhamento via WhatsApp

Além do envio por e-mail, o sistema permite compartilhar a lista diretamente pelo WhatsApp.

A lista é formatada automaticamente e enviada através de um link, facilitando o envio rápido para outras pessoas.

---

## 🧠 Conceitos de POO Aplicados

### 🔷 Herança

```python
class Item(ABC)
class ItemComum(Item)
class ItemPromocional(Item)
```

A classe `Item` é uma **classe abstrata**, ou seja, ela serve como base para outras classes e não pode ser instanciada diretamente.

Ela define atributos comuns como:

* nome
* quantidade
* preço
* categoria
* status

Além disso, define o método abstrato:

```python
calcularPreco()
```

Isso **obriga** as classes filhas (`ItemComum` e `ItemPromocional`) a implementarem esse método.

Cada classe filha especializa o comportamento:

* `ItemComum`: calcula preço normalmente (quantidade × preço)
* `ItemPromocional`: aplica regras de desconto (porcentagem ou leve X pague Y)

👉 Ou seja, a herança permite **reutilizar código e especializar comportamentos**.

---

### 🔷 Polimorfismo

O polimorfismo acontece quando diferentes objetos respondem ao **mesmo método de formas diferentes**.

No sistema, isso ocorre com:

```python
objetoItem.calcularPreco()
```

Mesmo chamando o mesmo método, o resultado depende do tipo do objeto:

* Se for `ItemComum` → cálculo simples
* Se for `ItemPromocional` → cálculo com desconto

Esse comportamento é usado principalmente na classe `Lista`, nos métodos:

* `calcularTotalGeral()`
* `calcularTotalMarcados()`
* `calcularTotalPendentes()`

Exemplo simplificado:

```python
for item in lista:
    total += item.calcularPreco()
```

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Flask
* **Banco de Dados:** SQLite3
* **Frontend:** HTML, CSS

---

## 📌 Roadmap

* 🔄 Sincronização entre usuários
  Permitir que múltiplos usuários editem a mesma lista em tempo real.
  
