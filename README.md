# 🛒 ListSmart – Gerenciador de Compras

Repositório desenvolvido para a disciplina de **Projeto de Software** – UFAL.

O **ListSmart** é um gerenciador de compras que ajuda o usuário a organizar listas de supermercado de forma simples, prática e eficiente.
---
## Implementação de design pattern criacional Builder
 O **Builder**  permite a construção de diferentes tipos de objetos passo a passo, a partir do mesmo código de construção.  
* Sua estrutura é feita através de uma herança abstrata, classes responsáveis pela declaração e implementação dos métodos desejados e um Director que coordena a construção do produto final. Para este caso, o builder substitui o uso do método `adicionar_item` da classe `Lista`.  
* Para esse projeto, a implementação do Builder além de modularizar o código, une todas as possibilidades para criação de um item na lista em um conjunto de classes, facilitando também possíveis alterações futuras. Também substituiu o `adicionarItem()` que possuía um grande número de parâmetros para administrar.

## Implementação de design pattern estrutural Facade  
O facade age como uma interface em um sistema de classes ou bibliotecas.
* Sua estrutura é feita por uma ou mais classes principais, dependendo da complexidade, que possui todas as chamadas de funções principais daquele(s) sistema(s).
* Para esse projeto, a implementação do Facade serviu como um intermediário entre o `app.py`, onde estavam as rotas utilizadas pelo Flask, e o `backend.py`, onde estão as implementações das funções. Portanto, houve uma divisão de responsabilidades. O `app.py` agora possui apenas as funções com as rotas Flask e as chamadas do facade, que admnistra de forma organizada a comunicação entre o backend e a entrada de dados pelo usuário.
Para implementações futuras, basta editar o facade e apenas adicionar a chamada junto da rota específica.

## Implementação de design pattern comportamental Observer
O observer é utilizado dentro de uma relação de um para muitos, ou seja, quando um evento/mudança em um determinado objeto, por exemplo, precisa ser notificado e/ou refletido para outros objetos ou sistemas.
* Sua estrutura é feita através de uma herança abstrata, classes responsáveis por identificar o Observer (observador) e o Subject (assunto) com as declarações e implementações dos metodos relacionados a cada um dentro do contexto do sistema.
* Para esse projeto, o observer muda a arquitetura do código na funcionalidade de compartilhamento, também de forma a facilitar a adição de outros canais de compartilhamento.


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

