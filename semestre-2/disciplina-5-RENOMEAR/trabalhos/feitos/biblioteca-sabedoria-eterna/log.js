console.log(`
$node index.js  
Conectado ao MongoDB!

--- Questão 1: Adicionar um novo livro ---
Livro adicionado com sucesso! ID: 6... (aqui será um ID gerado automaticamente)

--- Questão 2: Listar livros de 'Patrick Rothfuss' ---
{
  "_id": ObjectId("..."),
  "titulo": "O Nome do Vento",
  "autor": "Patrick Rothfuss",
  "ano_publicacao": 2007,
  "genero": "Fantasia",
  "quantidade": 10
}
{
  "_id": ObjectId("..."),
  "titulo": "A Wise Man's Fear",
  "autor": "Patrick Rothfuss",
  "ano_publicacao": 2011,
  "genero": "Fantasia",
  "quantidade": 5
}

--- Questão 3: Atualizar a quantidade de 'O Nome do Vento' ---
1 documento(s) atualizado(s).

--- Questão 4: Remover livros do gênero 'Fantasia' ---
2 documento(s) removido(s).

Conexão com o MongoDB fechada.`);