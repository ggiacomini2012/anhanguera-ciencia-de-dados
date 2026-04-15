const { MongoClient } = require('mongodb');

// URI de conexão com o seu banco de dados MongoDB
const uri = "mongodb://localhost:27017"; // Altere para a sua URI, se necessário
const client = new MongoClient(uri);

async function run() {
  try {
    // Conecte-se ao cliente do MongoDB
    await client.connect();
    console.log("Conectado ao MongoDB!");

    const database = client.db("biblioteca");
    const livros = database.collection("livros");

    // --- 1. CREATE: Adicionar um novo livro ---
    console.log("\n--- Questão 1: Adicionar um novo livro ---");
    const novoLivro = {
      titulo: "A Wise Man's Fear",
      autor: "Patrick Rothfuss",
      ano_publicacao: 2011,
      genero: "Fantasia",
      quantidade: 5
    };

    const resultadoCreate = await livros.insertOne(novoLivro);
    console.log(`Livro adicionado com sucesso! ID: ${resultadoCreate.insertedId}`);

    // --- 2. READ: Consultar livros de um autor específico ---
    console.log("\n--- Questão 2: Listar livros de 'Patrick Rothfuss' ---");
    const queryRead = { autor: "Patrick Rothfuss" };
    const cursor = livros.find(queryRead);

    if ((await livros.countDocuments(queryRead)) === 0) {
      console.log("Nenhum livro encontrado para este autor.");
    } else {
      await cursor.forEach(doc => console.log(doc));
    }

    // --- 3. UPDATE: Atualizar a quantidade de livros ---
    console.log("\n--- Questão 3: Atualizar a quantidade de 'O Nome do Vento' ---");
    const filtroUpdate = { titulo: "O Nome do Vento" };
    const atualizacao = { $inc: { quantidade: 3 } };

    const resultadoUpdate = await livros.updateOne(filtroUpdate, atualizacao);
    console.log(`${resultadoUpdate.modifiedCount} documento(s) atualizado(s).`);

    // --- 4. DELETE: Remover livros de um determinado gênero ---
    console.log("\n--- Questão 4: Remover livros do gênero 'Fantasia' ---");
    const filtroDelete = { genero: "Fantasia" };

    const resultadoDelete = await livros.deleteMany(filtroDelete);
    console.log(`${resultadoDelete.deletedCount} documento(s) removido(s).`);

  } finally {
    // Garanta que o cliente se feche após a conclusão/erro
    await client.close();
    console.log("Conexão com o MongoDB fechada.");
  }
}

run().catch(console.dir);
