create database fullstack;

use fullstack;

create table usertype(
usertype_id int not null auto_increment,
type varchar (15),
primary key (usertype_id)
);

create table user(
user_id int not null auto_increment,
name varchar(60) not null,
email varchar(60),
usertype_id integer,
password varchar(16),
is_active tinyint(1) not null,
cpf_cnpj varchar(14) unique,
phone char(11),
primary key (user_id),
CONSTRAINT fk_tipo FOREIGN KEY (usertype_id) REFERENCES usertype (usertype_id)
);

create table lab(
lab_id int not null auto_increment,
andar char(1),
lab char(6),
description varchar(60),
is_active tinyint(1) not null,
PRIMARY KEY (lab_id)
);

INSERT INTO usertype (type) VALUES ("Administrador");
INSERT INTO usertype (type) VALUES ("Aluno");
INSERT INTO usertype (type) VALUES ("Professor");