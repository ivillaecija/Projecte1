drop database if exists projecte1;
create database projecte1;
use projecte1;


-- CREACION DE TABLAS
create table player (
	player_id varchar(25) primary key,
    player_name varchar(40),
    player_risk tinyint,
    human tinyint(1))
;

create table deck (
	deck_id char(3) primary key,
    deck_name varchar(25))
;
create table card (
	card_id char(3) primary key,
    card_name varchar(25),
    card_value decimal(3,1),
    card_priority tinyint,
    card_real_value tinyint,
    deck_id char(3),
    constraint deck_id foreign key (deck_id) references deck(deck_id))
;
create table cardgame (
	cardgame_id int primary key,
    players tinyint,
    rounds tinyint,
    start_hour datetime,
    end_hour datetime,
    deck_id char(3),
    constraint card_deck_id foreign key (deck_id) references deck(deck_id)
);
create table player_game (
	cardgame_id int,
    player_id varchar(25),
    initial_card_id char(3),
    starting_points tinyint,
    ending_points tinyint,
    constraint player_cardgame_id foreign key 
		(cardgame_id) references cardgame(cardgame_id),
	constraint player_id foreign key (player_id) references 
		player(player_id))
;
create table player_game_round (
	cardgame_id int,
    round_num tinyint,
    player_id varchar(25),
    is_bank tinyint(1),
    bet_points tinyint,
    cards_value decimal(4,1),
    starting_round_points tinyint,
    ending_round_points tinyint,
    constraint player_game_round_cardgame_id foreign key (cardgame_id) references 
		cardgame(cardgame_id),
	constraint player_game_round_player_id foreign key (player_id) references 
		player(player_id)
    );
    

-- INSERTS
-- TABLA DECK
insert into deck values ('ESP', 'Baraja Española');
insert into deck values ('POK', 'Poker deck');

-- TABLA CARD
-- Baraja española
-- Oros
insert into card values ('001', 'As de Oros', 1, 4, 1, 'ESP');
insert into card values ('002', 'Dos de Oros', 2, 4, 2, 'ESP');
insert into card values ('003', 'Tres de Oros', 3, 4, 3, 'ESP');
insert into card values ('004', 'Cuatro de Oros', 4, 4, 4, 'ESP');
insert into card values ('005', 'Cinco de Oros', 5, 4, 5, 'ESP');
insert into card values ('006', 'Seis de Oros', 6, 4, 6, 'ESP');
insert into card values ('007', 'Siete de Oros', 7, 4, 7, 'ESP');
insert into card values ('008', 'Ocho de Oros', 8, 4, 0.5, 'ESP');
insert into card values ('009', 'Nueve de Oros', 9, 4, 0.5, 'ESP');
insert into card values ('010', 'Diez de Oros', 10, 4, 0.5, 'ESP');
insert into card values ('011', 'Once de Oros', 11, 4, 0.5, 'ESP');
insert into card values ('012', 'Doce de Oros', 12, 4, 0.5, 'ESP');

-- Espadas
insert into card values ('E01', 'As de Espadas', 1, 3, 1, 'ESP');
insert into card values ('E02', 'Dos de Espadas', 2, 3, 2, 'ESP');
insert into card values ('E03', 'Tres de Espadas', 3, 3, 3, 'ESP');
insert into card values ('E04', 'Cuatro de Espadas', 4, 3, 4, 'ESP');
insert into card values ('E05', 'Cinco de Espadas', 5, 3, 5, 'ESP');
insert into card values ('E06', 'Seis de Espadas', 6, 3, 6, 'ESP');
insert into card values ('E07', 'Siete de Espadas', 7, 3, 7, 'ESP');
insert into card values ('E08', 'Ocho de Espadas', 8, 3, 0.5, 'ESP');
insert into card values ('E09', 'Nueve de Espadas', 9, 3, 0.5, 'ESP');
insert into card values ('E10', 'Diez de Espadas', 10, 3, 0.5, 'ESP');
insert into card values ('E11', 'Once de Espadas', 11, 3, 0.5, 'ESP');
insert into card values ('E12', 'Doce de Espadas', 12, 3, 0.5, 'ESP');

-- Copas
insert into card values ('C01', 'As de Copas', 1, 2, 1, 'ESP');
insert into card values ('C02', 'Dos de Copas', 2, 2, 2, 'ESP');
insert into card values ('C03', 'Tres de Copas', 3, 2, 3, 'ESP');
insert into card values ('C04', 'Cuatro de Copas', 4, 2, 4, 'ESP');
insert into card values ('C05', 'Cinco de Copas', 5, 2, 5, 'ESP');
insert into card values ('C06', 'Seis de Copas', 6, 2, 6, 'ESP');
insert into card values ('C07', 'Siete de Copas', 7, 2, 7, 'ESP');
insert into card values ('C08', 'Ocho de Copas', 8, 2, 0.5, 'ESP');
insert into card values ('C09', 'Nueve de Copas', 9, 2, 0.5, 'ESP');
insert into card values ('C10', 'Diez de Copas', 10, 2, 0.5, 'ESP');
insert into card values ('C11', 'Once de Copas', 11, 2, 0.5, 'ESP');	
insert into card values ('C12', 'Doce de Copas', 12, 2, 0.5, 'ESP');

-- Bastos
insert into card values ('B01', 'As de Bastos', 1, 1, 1, 'ESP');
insert into card values ('B02', 'Dos de Bastos', 2, 1, 2, 'ESP');
insert into card values ('B03', 'Tres de Bastos', 3, 1, 3, 'ESP');
insert into card values ('B04', 'Cuatro de Bastos', 4, 1, 4, 'ESP');
insert into card values ('B05', 'Cinco de Bastos', 5, 1, 5, 'ESP');
insert into card values ('B06', 'Seis de Bastos', 6, 1, 6, 'ESP');
insert into card values ('B07', 'Siete de Bastos', 7, 1, 7, 'ESP');
insert into card values ('B08', 'Ocho de Bastos', 8, 1, 0.5, 'ESP');
insert into card values ('B09', 'Nueve de Bastos', 9, 1, 0.5, 'ESP');
insert into card values ('B10', 'Diez de Bastos', 10, 1, 0.5, 'ESP');
insert into card values ('B11', 'Once de Bastos', 11, 1, 0.5, 'ESP');	
insert into card values ('B12', 'Doce de Bastos', 11, 1, 0.5, 'ESP');


-- Baraja de poker
-- Diamantes 
insert into card values ('D01', 'As de Diamantes', 1, 4, 1, 'POK');
insert into card values ('D02', 'Dos de Diamantes', 2, 4, 2, 'POK');
insert into card values ('D03', 'Tres de Diamantes', 3, 4, 3, 'POK');
insert into card values ('D04', 'Cuatro de Diamantes', 4, 4, 4, 'POK');
insert into card values ('D05', 'Cinco de Diamantes', 5, 4, 5, 'POK');
insert into card values ('D06', 'Seis de Diamantes', 6, 4, 6, 'POK');
insert into card values ('D07', 'Siete de Diamantes', 7, 4, 7, 'POK');
insert into card values ('D08', 'Ocho de Diamantes', 8, 4, 0.5, 'POK');
insert into card values ('D09', 'Nueve de Diamantes', 9, 4, 0.5, 'POK');
insert into card values ('D10', 'Diez de Diamantes', 10, 4, 0.5, 'POK');
insert into card values ('D11', 'Jota de Diamantes', 11, 4, 0.5, 'POK');	
insert into card values ('D12', 'Reina de Diamantes', 12, 4, 0.5, 'POK');
insert into card values ('D13', 'Rey de Diamantes', 13, 4, 0.5, 'POK');

-- Picas
insert into card values ('P01', 'As de Picas', 1, 3, 1, 'POK');
insert into card values ('P02', 'Dos de Picas', 2, 3, 2, 'POK');
insert into card values ('P03', 'Tres de Picas', 3, 3, 3, 'POK');
insert into card values ('P04', 'Cuatro de Picas', 4, 3, 4, 'POK');
insert into card values ('P05', 'Cinco de Picas', 5, 3, 5, 'POK');
insert into card values ('P06', 'Seis de Picas', 6, 3, 6, 'POK');
insert into card values ('P07', 'Siete de Picas', 7, 3, 7, 'POK');
insert into card values ('P08', 'Ocho de Picas', 8, 3, 0.5, 'POK');
insert into card values ('P09', 'Nueve de Picas', 9, 3, 0.5, 'POK');
insert into card values ('P10', 'Diez de Picas', 10, 3, 0.5, 'POK');
insert into card values ('P11', 'Jota de Picas', 11, 3, 0.5, 'POK');	
insert into card values ('P12', 'Reina de Picas', 12, 3, 0.5, 'POK');
insert into card values ('P13', 'Rey de Picas', 13, 3, 0.5, 'POK');

-- Corazones
insert into card values ('V01', 'As de Corazones', 1, 2, 1, 'POK');
insert into card values ('V02', 'Dos de Corazones', 2, 2, 2, 'POK');
insert into card values ('V03', 'Tres de Corazones', 3, 2, 3, 'POK');
insert into card values ('V04', 'Cuatro de Corazones', 4, 2, 4, 'POK');
insert into card values ('V05', 'Cinco de Corazones', 5, 2, 5, 'POK');
insert into card values ('V06', 'Seis de Corazones', 6, 2, 6, 'POK');
insert into card values ('V07', 'Siete de Corazones', 7, 2, 7, 'POK');
insert into card values ('V08', 'Ocho de Corazones', 8, 2, 0.5, 'POK');
insert into card values ('V09', 'Nueve de Corazones', 9, 2, 0.5, 'POK');
insert into card values ('V10', 'Diez de Corazones', 10, 2, 0.5, 'POK');
insert into card values ('V11', 'Jota de Corazones', 11, 2, 0.5, 'POK');	
insert into card values ('V12', 'Reina de Corazones', 12, 2, 0.5, 'POK');
insert into card values ('V13', 'Rey de Corazones', 13, 2, 0.5, 'POK');

-- Treboles
insert into card values ('T01', 'As de Treboles', 1, 1, 1, 'POK');
insert into card values ('T02', 'Dos de Treboles', 2, 1, 2, 'POK');
insert into card values ('T03', 'Tres de Treboles', 3, 1, 3, 'POK');
insert into card values ('T04', 'Cuatro de Treboles', 4, 1, 4, 'POK');
insert into card values ('T05', 'Cinco de Treboles', 5, 1, 5, 'POK');
insert into card values ('T06', 'Seis de Treboles', 6, 1, 6, 'POK');
insert into card values ('T07', 'Siete de Treboles', 7, 1, 7, 'POK');
insert into card values ('T08', 'Ocho de Treboles', 8, 1, 0.5, 'POK');
insert into card values ('T09', 'Nueve de Treboles', 9, 1, 0.5, 'POK');
insert into card values ('T10', 'Diez de Treboles', 10, 1, 0.5, 'POK');
insert into card values ('T11', 'Jota de Treboles', 11, 1, 0.5, 'POK');	
insert into card values ('T12', 'Reina de Treboles', 12, 1, 0.5, 'POK');
insert into card values ('T13', 'Rey de Treboles', 13, 1, 0.5, 'POK');

-- TABLA PLAYER
insert into player values ('12312313K', 'Humano1', 50, true);
insert into player values ('44444444A', 'Boot1', 40, false);
insert into player values ('34343434H', 'Humano2', 30, true);
insert into player values ('45129508N', 'Boot2', 50, false);