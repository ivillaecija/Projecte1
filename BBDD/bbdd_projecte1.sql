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


-- DATOS DE EJEMPLO
insert into player values ('12312313K', 'Humano1', 50, true);
insert into player values ('44444444A', 'Boot1', 40, false);
insert into player values ('34343434H', 'Humano2', 30, true);
insert into player values ('45129508N', 'Boot2', 50, false);
insert into cardgame values (001, 3, 1, '2022-01-16 16:00:00', '2022-01-16 20:00:00', 'ESP');
insert into cardgame values (002, 2, 2, '2022-01-16 16:00:00', '2022-01-16 20:00:00', 'ESP');
insert into cardgame values (003, 2, 2, '2022-01-16 10:00:00', '2022-01-16 10:05:00', 'ESP');	
insert into cardgame values (004, 2, 1, '2022-01-16 19:45:00', '2022-01-16 20:00:00', 'ESP');
insert into player_game values (003, '12312313K', '001', 20, 35);
insert into player_game values (003, '45129508N', 'E02', 20, 5);
insert into player_game values (004, '12312313K', 'E07', 20, 11);
insert into player_game values (004, '44444444A', 'E04', 20, 29);
insert into player_game values (001, '12312313K', '001', 20, 11);
insert into player_game values (002, '12312313K', '005', 20, 11);
insert into player_game values (001, '44444444A', '002', 20, 15);
insert into player_game values (002, '44444444A', '003', 20, 50);
insert into player_game values (001, '34343434H', '004', 20, 30);
insert into player_game_round values (001, 1, '12312313K', False, 5, 6, 20, 25);
insert into player_game_round values (001, 1, '44444444A', True, 0, 5.5, 20, 20);
insert into player_game_round values (001, 1, '34343434H', False, 5, 5, 20, 15);
insert into player_game_round values (002, 1, '12312313K', False, 5, 7.5, 20, 30);
insert into player_game_round values (002, 1, '44444444A', True, 0, 7, 20, 10);
insert into player_game_round values (002, 2, '12312313K', True, 0, 8, 30, 15);
insert into player_game_round values (002, 2, '44444444A', False, 15, 6, 15, 30);
insert into player_game_round values (003, 1, '12312313K', True, 0, 5.5, 20, 30);
insert into player_game_round values (003, 1, '45129508N', False, 10, 5, 20, 10);
insert into player_game_round values (003, 2, '12312313K', True, 0, 5.5, 30, 35);
insert into player_game_round values (003, 2, '45129508N', False, 5, 5, 10, 5);
insert into player_game_round values (004, 1, '44444444A', True, 0, 6.5, 20, 29);
insert into player_game_round values (004, 1, '12312313K', False, 9, 6, 20, 11);

-- VISTA PARA MOSTRAR LA TABLA DE RANKINGS
-- VISTA PARA FACILITAR LA CREACION DE LA TABLA FINAL DE RANKINGS
-- 1) VISTA PARA MOSTRAR LOS EARNINGS DE CADA JUGADOR EN CADA PARTIDA
create view player_earning_game as select distinct pg.player_id, pg.cardgame_id, (pg.ending_points - pg.starting_points) as earnings
from player_game pg
join player_game_round pgr on pg.player_id=pgr.player_id;

-- 2) VISTA PARA MOSTRAR LOS EARNINGS DE CADA JUGADOR
create view player_earnings as select distinct pg.player_id, 
(select sum(earnings) from player_earning_game where player_id=pg.player_id) as earnings
from player_earning_game pg;

-- 3) VISTA PARA MOSTRAR LOS MINUTOS DE CADA JUGADOR EN CADA PARTIDA
create view minutos_player_game as select pg.player_id, c.cardgame_id, TIMESTAMPDIFF(MINUTE,c.start_hour,c.end_hour) as minutos 
from cardgame c join player_game pg on c.cardgame_id=pg.cardgame_id

-- 4) VISTA PARA MOSTRAR LOS MINUTOS TOTALES DE CADA JUGADOR
create view player_minutes as select p.player_id, coalesce(null, (select sum(minutos) from minutos_player_game m 
where m.player_id=p.player_id), 0) as minutos from player p;

-- VISTA FINAL DE LA TABLA DE RANKINGS
create view tabla_ranking as select p.player_id, p.player_name, coalesce(null, e.earnings, 0) as earnings, 
(select count(*) from player_game where player_id=p.player_id) as games_played, m.minutos as minutes
from player p left join player_earnings e on e.player_id=p.player_id
join player_minutes m on m.player_id=p.player_id;


-- VISTAS INFORME
-- 1) CARTA INICIAL MAS REPETIDA DE LOS PLAYERS CON 3 GAMES O MÁS.
-- Para hacer esta vista he utilizado otras vista ya que no conseguia hacerla de una sola.
-- 1.1) VISTA QUE ME DEVUELVE TODAS LAS INITIAL_CARD_ID QUE HAN SALIDO CON OTRAS FILAS COMO QUIEN LA HA SACADO, 
-- CUANTAS VECES LA HA SACADO, CUANTAS PARTIDAS HA JUGADO, A QUE BARAJA PERTENECE I QUE PRIORIDAD TIENE LA CARTA.(DECK Y PRIORITY ES PARA SACAR EL PALO DE
create view initial_cards as select distinct pg.player_id, pg.initial_card_id, cg.deck_id as baraja, c.card_priority as priority, 
count(pg.initial_card_id) as repeticions, 
(select count(*) from player_game where player_id=pg.player_id) as games_played
from player_game pg
join cardgame cg on cg.cardgame_id = pg.cardgame_id
join card c on pg.initial_card_id = c.card_id
group by pg.player_id, pg.initial_card_id, cg.deck_id, c.card_priority;

-- 1.2) VISTA FINAL
create view initial_card_most_repeated_player as select i.player_id, 
	CONCAT_WS('',
			IF(i.baraja = 'ESP' and i.priority = 4, 'Oros', ''),
            IF(i.baraja = 'ESP' and i.priority = 3, 'Espadas', ''),
            IF(i.baraja = 'ESP' and i.priority = 2, 'Copas', ''),
            IF(i.baraja = 'ESP' and i.priority = 1, 'Bastos', ''),
            IF(i.baraja = 'POK' and i.priority = 4, 'Diamantes', ''),
            IF(i.baraja = 'POK' and i.priority = 3, 'Picas', ''),
            IF(i.baraja = 'POK' and i.priority = 2, 'Corazones', ''),
            IF(i.baraja = 'POK' and i.priority = 1, 'Treboles', '')
		) as palo,
i.initial_card_id, i.repeticions, 
(select count(*) from player_game where i.player_id=player_id) as games_played
from initial_cards i
where i.repeticions in (select max(repeticions) from initial_cards where player_id = i.player_id)
order by i.player_id;


-- 2) APUESTA MAS ALTA 
create view apuesta_mas_alta as 
select player_id as player, cardgame_id as partida, bet_points as apuesta 
from player_game_round where bet_points like (select max(bet_points) from player_game_round);

-- 3) APUESTA MAS BAJA
create view apuesta_mas_baja as 
select player_id as player, cardgame_id as partida, bet_points as apuesta 
from player_game_round where bet_points like (select min(bet_points) from player_game_round);

-- 4) 
-- NO ESTA ACABADA

-- 5) PARTIDAS GANADAS POR BOTS
create view victorias_bots as 
select c.cardgame_id as partida, (pg.ending_points - pg.starting_points) as puntos_ganados
from player_game pg
join player p on p.player_id=pg.player_id
join cardgame c on c.cardgame_id=pg.cardgame_id
where p.human is False and pg.ending_points > pg.starting_points;

-- 6) RONDAS GANADAS POR LA BANCA EN CADA PARTIDA
create view rondas_ganadas_banca as 
select distinct c.cardgame_id as partida, 
(select count(*) from player_game_round where is_bank is True and
(pgr.ending_round_points > pgr.starting_round_points) and cardgame_id=c.cardgame_id) as rondas_ganadas
from player_game_round pgr
join cardgame c on c.cardgame_id=pgr.cardgame_id
where pgr.is_bank is True;

-- 7) USUARIOS QUE HAN SIDO BANCA EN CADA PARTIDA
create view usuarios_banca_partida as 
select distinct c.cardgame_id as partida, 
(select count(*) from player_game_round where is_bank is True and cardgame_id=c.cardgame_id) as usuarios_banca
from player_game_round pgr
join cardgame c on c.cardgame_id=pgr.cardgame_id;

-- 8) APUESTA MEDIA POR PARTIDA
create view apuesta_media_partida as 
select distinct c.cardgame_id as partida, (select avg(bet_points) from player_game_round where cardgame_id=c.cardgame_id) as media
from player_game pgr
join cardgame c on c.cardgame_id=pgr.cardgame_id;

-- 9) APUESTA MEDIA EN LA PRIMERA RONDA DE CADA PARTIDA
create view apuesta_media_ronda1 as 
select distinct c.cardgame_id as partida, 
(select avg(bet_points) from player_game_round where cardgame_id=c.cardgame_id and round_num = 1) as media
from player_game pgr
join cardgame c on c.cardgame_id=pgr.cardgame_id;


-- 10) APUESTA MEDIA EN LA ULTIMA RONDA DE CADA PARTIDA
create view apuesta_media_ultima_ronda as 
select distinct c.cardgame_id as partida, 
(select avg(bet_points) from player_game_round where cardgame_id=c.cardgame_id and round_num = c.rounds) as media
from player_game pgr
join cardgame c on c.cardgame_id=pgr.cardgame_id;
