CREATE DATABASE IF NOT EXISTS locadora;
USE locadora;

CREATE TABLE pessoa (
    id_pessoa INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(14) UNIQUE,
    email VARCHAR(100),
    telefone VARCHAR(20),
    endereco VARCHAR(200)
);

CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY,
    id_pessoa INT,
    pontos INT DEFAULT 0,
    tipo_de_cliente ENUM('ouro', 'prata', 'bronze') DEFAULT 'bronze',
    FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa)
);

CREATE TABLE funcionario (
    id_funcionario INT PRIMARY KEY,
    id_pessoa INT,
    data_de_contratacao DATE,
    salario DECIMAL(10,2),
    cargo VARCHAR(50),
    FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa)
);

CREATE TABLE veiculo (
    id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100),
    marca VARCHAR(100),
    ano INT,
    placa VARCHAR(10) UNIQUE,
    disponibilidade BOOLEAN DEFAULT TRUE
);

CREATE TABLE locacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_veiculo INT,
    id_funcionario INT,
    data_inicio DATE,
    data_fim DATE,
    valor_total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_veiculo) REFERENCES veiculo(id_veiculo),
    FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario)
);

INSERT INTO pessoa (nome, cpf, email, telefone, endereco) VALUES
('Pessoa 1', '000.000.000-01', 'pessoa1@email.com', '(11)90000-0001', 'Endereço 1'),
('Pessoa 2', '000.000.000-02', 'pessoa2@email.com', '(11)90000-0002', 'Endereço 2'),
('Pessoa 3', '000.000.000-03', 'pessoa3@email.com', '(11)90000-0003', 'Endereço 3'),
('Pessoa 4', '000.000.000-04', 'pessoa4@email.com', '(11)90000-0004', 'Endereço 4'),
('Pessoa 5', '000.000.000-05', 'pessoa5@email.com', '(11)90000-0005', 'Endereço 5'),
('Pessoa 6', '000.000.000-06', 'pessoa6@email.com', '(11)90000-0006', 'Endereço 6'),
('Pessoa 7', '000.000.000-07', 'pessoa7@email.com', '(11)90000-0007', 'Endereço 7'),
('Pessoa 8', '000.000.000-08', 'pessoa8@email.com', '(11)90000-0008', 'Endereço 8'),
('Pessoa 9', '000.000.000-09', 'pessoa9@email.com', '(11)90000-0009', 'Endereço 9'),
('Pessoa 10', '000.000.000-10', 'pessoa10@email.com', '(11)90000-0010', 'Endereço 10'),
('Pessoa 11', '000.000.000-11', 'pessoa11@email.com', '(11)90000-0011', 'Endereço 11'),
('Pessoa 12', '000.000.000-12', 'pessoa12@email.com', '(11)90000-0012', 'Endereço 12'),
('Pessoa 13', '000.000.000-13', 'pessoa13@email.com', '(11)90000-0013', 'Endereço 13'),
('Pessoa 14', '000.000.000-14', 'pessoa14@email.com', '(11)90000-0014', 'Endereço 14'),
('Pessoa 15', '000.000.000-15', 'pessoa15@email.com', '(11)90000-0015', 'Endereço 15'),
('Pessoa 16', '000.000.000-16', 'pessoa16@email.com', '(11)90000-0016', 'Endereço 16'),
('Pessoa 17', '000.000.000-17', 'pessoa17@email.com', '(11)90000-0017', 'Endereço 17'),
('Pessoa 18', '000.000.000-18', 'pessoa18@email.com', '(11)90000-0018', 'Endereço 18'),
('Pessoa 19', '000.000.000-19', 'pessoa19@email.com', '(11)90000-0019', 'Endereço 19'),
('Pessoa 20', '000.000.000-20', 'pessoa20@email.com', '(11)90000-0020', 'Endereço 20'),
('Pessoa 21', '000.000.000-21', 'pessoa21@email.com', '(11)90000-0021', 'Endereço 21'),
('Pessoa 22', '000.000.000-22', 'pessoa22@email.com', '(11)90000-0022', 'Endereço 22'),
('Pessoa 23', '000.000.000-23', 'pessoa23@email.com', '(11)90000-0023', 'Endereço 23'),
('Pessoa 24', '000.000.000-24', 'pessoa24@email.com', '(11)90000-0024', 'Endereço 24'),
('Pessoa 25', '000.000.000-25', 'pessoa25@email.com', '(11)90000-0025', 'Endereço 25'),
('Pessoa 26', '000.000.000-26', 'pessoa26@email.com', '(11)90000-0026', 'Endereço 26'),
('Pessoa 27', '000.000.000-27', 'pessoa27@email.com', '(11)90000-0027', 'Endereço 27'),
('Pessoa 28', '000.000.000-28', 'pessoa28@email.com', '(11)90000-0028', 'Endereço 28'),
('Pessoa 29', '000.000.000-29', 'pessoa29@email.com', '(11)90000-0029', 'Endereço 29'),
('Pessoa 30', '000.000.000-30', 'pessoa30@email.com', '(11)90000-0030', 'Endereço 30');

INSERT INTO cliente (id_cliente, id_pessoa, pontos, tipo_de_cliente) VALUES
(1, 1, 1734, 'prata'),
(2, 2, 770, 'ouro'),
(3, 3, 1530, 'prata'),
(4, 4, 422, 'bronze'),
(5, 5, 1850, 'prata'),
(6, 6, 759, 'ouro'),
(7, 7, 1948, 'bronze'),
(8, 8, 1800, 'prata'),
(9, 9, 970, 'prata'),
(10, 10, 1358, 'prata'),
(11, 11, 1614, 'prata'),
(12, 12, 814, 'prata'),
(13, 13, 1605, 'bronze'),
(14, 14, 1915, 'bronze'),
(15, 15, 553, 'ouro'),
(16, 16, 1512, 'prata'),
(17, 17, 474, 'prata'),
(18, 18, 1022, 'bronze'),
(19, 19, 1093, 'ouro'),
(20, 20, 368, 'ouro');

INSERT INTO funcionario (id_funcionario, id_pessoa, data_de_contratacao, salario, cargo) VALUES
(1, 21, '2023-01-15', 4874.00, 'Cargo 1'),
(2, 22, '2022-09-15', 3781.00, 'Cargo 2'),
(3, 23, '2022-08-15', 2854.00, 'Cargo 3'),
(4, 24, '2020-08-15', 3613.00, 'Cargo 4'),
(5, 25, '2023-01-15', 4794.00, 'Cargo 5'),
(6, 26, '2022-07-15', 3146.00, 'Cargo 6'),
(7, 27, '2021-07-15', 3470.00, 'Cargo 7'),
(8, 28, '2024-09-15', 3119.00, 'Cargo 8'),
(9, 29, '2020-03-15', 2968.00, 'Cargo 9'),
(10, 30, '2021-02-15', 4846.00, 'Cargo 10');

INSERT INTO veiculo (modelo, marca, ano, placa, disponibilidade) VALUES
('Modelo 1', 'Marca 1', 2023, 'AAA0001', TRUE),
('Modelo 2', 'Marca 2', 2022, 'AAA0002', TRUE),
('Modelo 3', 'Marca 3', 2021, 'AAA0003', TRUE),
('Modelo 4', 'Marca 4', 2022, 'AAA0004', TRUE),
('Modelo 5', 'Marca 5', 2022, 'AAA0005', TRUE),
('Modelo 6', 'Marca 6', 2025, 'AAA0006', TRUE),
('Modelo 7', 'Marca 7', 2023, 'AAA0007', TRUE),
('Modelo 8', 'Marca 8', 2024, 'AAA0008', TRUE),
('Modelo 9', 'Marca 9', 2024, 'AAA0009', TRUE),
('Modelo 10', 'Marca 10', 2023, 'AAA0010', TRUE);

INSERT INTO locacao (id_cliente, id_veiculo, id_funcionario, data_inicio, data_fim, valor_total) VALUES
(1, 1, 1, '2024-01-01', '2024-01-06', 500.00),
(2, 2, 2, '2024-01-04', '2024-01-10', 520.00),
(3, 3, 3, '2024-01-07', '2024-01-14', 540.00),
(4, 4, 4, '2024-01-10', '2024-01-15', 560.00),
(5, 5, 5, '2024-01-13', '2024-01-19', 580.00),
(6, 6, 6, '2024-01-16', '2024-01-23', 600.00),
(7, 7, 7, '2024-01-19', '2024-01-24', 620.00),
(8, 8, 8, '2024-01-22', '2024-01-28', 640.00),
(9, 9, 9, '2024-01-25', '2024-02-01', 660.00),
(10, 10, 10, '2024-01-28', '2024-02-02', 680.00),
(11, 1, 1, '2024-01-31', '2024-02-06', 500.00),
(12, 2, 2, '2024-02-03', '2024-02-10', 520.00),
(13, 3, 3, '2024-02-06', '2024-02-11', 540.00),
(14, 4, 4, '2024-02-09', '2024-02-15', 560.00),
(15, 5, 5, '2024-02-12', '2024-02-19', 580.00),
(16, 6, 6, '2024-02-15', '2024-02-20', 600.00),
(17, 7, 7, '2024-02-18', '2024-02-24', 620.00),
(18, 8, 8, '2024-02-21', '2024-02-28', 640.00),
(19, 9, 9, '2024-02-24', '2024-02-29', 660.00),
(20, 10, 10, '2024-02-27', '2024-03-04', 680.00),
(1, 1, 1, '2024-03-01', '2024-03-08', 500.00),
(2, 2, 2, '2024-03-04', '2024-03-09', 520.00),
(3, 3, 3, '2024-03-07', '2024-03-13', 540.00),
(4, 4, 4, '2024-03-10', '2024-03-17', 560.00),
(5, 5, 5, '2024-03-13', '2024-03-18', 580.00),
(6, 6, 6, '2024-03-16', '2024-03-22', 600.00),
(7, 7, 7, '2024-03-19', '2024-03-26', 620.00),
(8, 8, 8, '2024-03-22', '2024-03-27', 640.00),
(9, 9, 9, '2024-03-25', '2024-03-31', 660.00),
(10, 10, 10, '2024-03-28', '2024-04-04', 680.00),
(11, 1, 1, '2024-03-31', '2024-04-05', 500.00),
(12, 2, 2, '2024-04-03', '2024-04-09', 520.00),
(13, 3, 3, '2024-04-06', '2024-04-13', 540.00),
(14, 4, 4, '2024-04-09', '2024-04-14', 560.00),
(15, 5, 5, '2024-04-12', '2024-04-18', 580.00),
(16, 6, 6, '2024-04-15', '2024-04-22', 600.00),
(17, 7, 7, '2024-04-18', '2024-04-23', 620.00),
(18, 8, 8, '2024-04-21', '2024-04-27', 640.00),
(19, 9, 9, '2024-04-24', '2024-05-01', 660.00),
(20, 10, 10, '2024-04-27', '2024-05-02', 680.00),
(1, 1, 1, '2024-04-30', '2024-05-06', 500.00),
(2, 2, 2, '2024-05-03', '2024-05-10', 520.00),
(3, 3, 3, '2024-05-06', '2024-05-11', 540.00),
(4, 4, 4, '2024-05-09', '2024-05-15', 560.00),
(5, 5, 5, '2024-05-12', '2024-05-19', 580.00),
(6, 6, 6, '2024-05-15', '2024-05-20', 600.00),
(7, 7, 7, '2024-05-18', '2024-05-24', 620.00),
(8, 8, 8, '2024-05-21', '2024-05-28', 640.00),
(9, 9, 9, '2024-05-24', '2024-05-29', 660.00),
(10, 10, 10, '2024-05-27', '2024-06-02', 680.00);


/* 1. Crie uma consulta que retorne todos os clientes que possuem mais de 1000 pontos e são do tipo 'prata' ou 'ouro'. */
select pes.nome, cliente.pontos,cliente.tipo_de_cliente
from pessoa pes
join cliente on pes.id_pessoa= cliente.id_pessoa
where pontos >1000
and tipo_de_cliente="prata" or  tipo_de_cliente="ouro" and pontos>1000;


/* 2. Crie uma consulta que retorne todos os veículos que estão disponíveis para locação e foram fabricados após 2020. */
    select modelo
    from veiculo
    where  ano>2020 and disponibilidade=TRUE;

/* 3. Crie uma consulta que retorne todos os funcionários que foram contratados após 2022 e têm um salário maior que 3000. */
select pes.nome,func.data_de_contratacao,func.salario
from pessoa pes
join funcionario func on pes.id_pessoa=func.id_funcionario
where salario>3000 and data_de_contratacao>'2022-12-31';

/* 4. Crie uma consulta que retorne todas as locações realizadas entre 01/01/2024 e 31/03/2024, ordenadas pela data de início da locação. */
select data_inicio
from locacao
where data_inicio>'2024-01-01'
and data_inicio<'2024-03-31'
order by data_inicio;
/* 6. Adicione um novo veículo à tabela de veículos com as seguintes informações: modelo 'Modelo 11', marca 'Marca 11', ano 2025, placa 'AAA0011' e disponibilidade TRUE. */
insert INTO veiculo(modelo,marca,ano,placa,disponibilidade)
VALUES("modelo 11","marca 11",2025,"AAA0011",TRUE);

/* 7. Atualize o status de disponibilidade do veículo com placa 'AAA0001' para FALSE. */
update veiculo
set disponibilidade=FALSE
where placa="AAA0001";

/* 8. Delete a locação com ID 5 da tabela de locações. */
delete from locacao
where id=5;

/* 9. Crie uma consulta que retorne o total de locações realizadas por cada cliente, ordenadas pelo total de locações em ordem decrescente. */
select pes.nome,count(lo.id) as quantidade_de_locacoes
from locacao lo
join cliente cli on lo.id_cliente=cli.id_cliente
join pessoa pes on pes.id_pessoa=cli.id_cliente
group by pes.nome;
order by quantidade_de_locacoes desc, pes.nome;

/* 10. Crie uma consulta que retorne o total de receita gerada por cada veículo, ordenadas pela receita em ordem decrescente. */
select lo.id_veiculo,sum(lo.valor_total) as Quantidade_por_carro
from pessoa pes
join cliente cli on cli.id_pessoa=pes.id_pessoa
join locacao lo on lo.id_cliente=cli.id_cliente
group by lo.id_veiculo
order by Quantidade_por_carro desc,lo.id_veiculo;

/* 11. Crie uma consulta que retorne o total de locações realizadas por cada funcionário, ordenadas pelo total de locações em ordem decrescente. */
select pes.nome,count(lo.id_funcionario)
from pessoa pes
join funcionario fun on fun.id_pessoa=pes.id_pessoa
join locacao lo on lo.id_funcionario=fun.id_funcionario
group by lo.id_funcionario
order by count(lo.id_funcionario) desc;

/* 12. Crie uma consulta que retorne todos os veículos, a quantidade de locações realizadas e a receita total gerada por cada veículo, ordenadas pela receita em ordem decrescente. */
select ve.modelo,count(lo.id_veiculo)as quantidade_de_locacoes,sum(lo.valor_total) as valor_por_carro
from veiculo ve
join locacao lo on lo.id_veiculo=ve.id_veiculo
group by lo.id_veiculo,ve.modelo
order by valor_por_carro desc;



