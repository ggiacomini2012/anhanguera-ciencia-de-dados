
-- Tabela de Clientes
-- Informações básicas sobre os clientes.
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

-- Tabela de Endereços de Entrega
-- Armazena os locais para onde os pedidos serão enviados.
CREATE TABLE IF NOT EXISTS enderecos (
    endereco_id INT PRIMARY KEY AUTO_INCREMENT,
    rua VARCHAR(255) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    cep VARCHAR(10) NOT NULL,
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

-- Tabela de Produtos
-- Catálogo de produtos da floricultura.
CREATE TABLE IF NOT EXISTS produtos (
    produto_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2) NOT NULL,
    tipo VARCHAR(50) NOT NULL
);

-- Tabela de Pedidos
-- Registra os pedidos feitos pelos clientes.
CREATE TABLE IF NOT EXISTS pedidos (
    pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    data_pedido DATETIME NOT NULL,
    status VARCHAR(50) NOT NULL,
    cliente_id INT,
    endereco_id INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
    FOREIGN KEY (endereco_id) REFERENCES enderecos(endereco_id)
);

-- Tabela de Relacionamento entre Pedidos e Produtos (Tabela Associativa)
-- Permite que um pedido tenha múltiplos produtos e um produto esteja em múltiplos pedidos.
CREATE TABLE IF NOT EXISTS pedido_produtos (
    pedido_id INT,
    produto_id INT,
    quantidade INT NOT NULL,
    PRIMARY KEY (pedido_id, produto_id),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
);