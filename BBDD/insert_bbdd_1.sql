use projecte1;

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
-- create table card (
-- 	card_id char(3) primary key,
--     card_name varchar(25),
--     card_value decimal(3,1),
--     card_priority tinyint,
--     card_real_value tinyint,
--     deck_id char(3),
--     constraint deck_id foreign key (deck_id) references deck(deck_id))
-- ;

-- cartas = {"ESP":{
-- "O01": { "literal" : "As de Oros" , "value" : 1, "priority" : 4, "realValue" : 1},
-- "O02": { "literal" : "Dos de Oros" , "value" : 2, "priority" : 4, "realValue" : 2},
-- "O03": { "literal" : "Tres de Oros" , "value" : 3, "priority" : 4, "realValue" : 3},
-- "O04":{"literal" : "Cuatro de Oros" , "value" : 4, "priority" : 4, "realValue" : 4},
-- "O05":{"literal" : "Cinco de Oros" , "value" : 5, "priority" : 4, "realValue" : 5},
-- "O06":{"literal" : "Seis de Oros" , "value" : 6, "priority" : 4, "realValue" : 6},
-- "O07":{"literal" : "Siete de Oros" , "value" : 7, "priority" : 4, "realValue" : 7},
-- "O08":{"no literal" : "Ocho de Oros" , "value" : 8, "priority" : 4, "realValue" : 0.5},
-- "O09":{"no literal" : "Nueve de Oros" , "value" : 9, "priority" : 4, "realValue" : 0.5},
-- "O10":{"no literal" : "Diez de Oros" , "value" : 10, "priority" : 4, "realValue" : 0.5},
-- "O11":{"no literal" : "Once de Oros" , "value" : 11, "priority" : 4, "realValue" : 0.5},
-- "O12":{"no literal" : "Doce de Oros" , "value" : 12, "priority" : 4, "realValue" : 0.5},

-- "E01": { "literal" : "As de Espadas" , "value" : 1, "priority" : 3, "realValue" : 1},
-- "E02": { "literal" : "Dos de Espadas" , "value" : 2, "priority" : 3, "realValue" : 2},
-- "E03": { "literal" : "Tres de Espadas" , "value" : 3, "priority" : 3, "realValue" : 3},
-- "E04":{"literal" : "Cuatro de Espadas" , "value" : 4, "priority" : 3, "realValue" : 4},
-- "E05":{"literal" : "Cinco de Espadas" , "value" : 5, "priority" : 3, "realValue" : 5},
-- "E06":{"literal" : "Seis de Espadas" , "value" : 6, "priority" : 3, "realValue" : 6},
-- "E07":{"literal" : "Siete de Espadas" , "value" : 7, "priority" : 3, "realValue" : 7},
-- "E08":{"no literal" : "Ocho de Espadas" , "value" : 8, "priority" : 3, "realValue" : 0.5},
-- "E09":{"no literal" : "Nueve de Espadas" , "value" : 9, "priority" : 3, "realValue" : 0.5},
-- "E10":{"no literal" : "Diez de Espadas" , "value" : 10, "priority" : 3, "realValue" : 0.5},
-- "E11":{"no literal" : "Once de Espadas" , "value" : 11, "priority" : 3, "realValue" : 0.5},
-- "E12":{"no literal" : "Doce de Espadas" , "value" : 12, "priority" : 3, "realValue" : 0.5},

-- "C01": { "literal" : "As de Copas" , "value" : 1, "priority" : 2, "realValue" : 1},
-- "C02": { "literal" : "Dos de Copas" , "value" : 2, "priority" : 2, "realValue" : 2},
-- "C03": { "literal" : "Tres de Copas" , "value" : 3, "priority" : 2, "realValue" : 3},
-- "C04":{"literal" : "Cuatro de Copas" , "value" : 4, "priority" : 2, "realValue" : 4},
-- "C05":{"literal" : "Cinco de Copas" , "value" : 5, "priority" : 2, "realValue" : 5},
-- "C06":{"literal" : "Seis de Copas" , "value" : 6, "priority" : 2, "realValue" : 6},
-- "C07":{"literal" : "Siete de Copas" , "value" : 7, "priority" : 2, "realValue" : 7},
-- "C08":{"no literal" : "Ocho de Copas" , "value" : 8, "priority" : 2, "realValue" : 0.5},
-- "C09":{"no literal" : "Nueve de Copas" , "value" : 9, "priority" : 2, "realValue" : 0.5},
-- "C10":{"no literal" : "Diez de Copas" , "value" : 10, "priority" : 2, "realValue" : 0.5},
-- "C11":{"no literal" : "Once de Copas" , "value" : 11, "priority" : 2, "realValue" : 0.5},
-- "C12":{"no literal" : "Doce de Copas" , "value" : 12, "priority" : 2, "realValue" : 0.5},

-- "B01": { "literal" : "As de Bastos" , "value" : 1, "priority" : 1, "realValue" : 1},
-- "B02": { "literal" : "Dos de Bastos" , "value" : 2, "priority" : 1, "realValue" : 2},
-- "B03": { "literal" : "Tres de Bastos" , "value" : 3, "priority" : 1, "realValue" : 3},
-- "B04":{"literal" : "Cuatro de Bastos" , "value" : 4, "priority" : 1, "realValue" : 4},
-- "B05":{"literal" : "Cinco de Bastos" , "value" : 5, "priority" : 1, "realValue" : 5},
-- "B06":{"literal" : "Seis de Bastos" , "value" : 6, "priority" : 1, "realValue" : 6},
-- "B07":{"literal" : "Siete de Bastos" , "value" : 7, "priority" : 1, "realValue" : 7},
-- "B08":{"no literal" : "Ocho de Bastos" , "value" : 8, "priority" : 1, "realValue" : 0.5},
-- "B09":{"no literal" : "Nueve de Bastos" , "value" : 9, "priority" : 1, "realValue" : 0.5},
-- "B10":{"no literal" : "Diez de Bastos" , "value" : 10, "priority" : 1, "realValue" : 0.5},
-- "B11":{"no literal" : "Once de Bastos" , "value" : 11, "priority" : 1, "realValue" : 0.5},
-- "B12":{"no literal" : "Doce de Bastos" , "value" : 12, "priority" : 1, "realValue" : 0.5},
-- },"POK":{
-- "D01":{"literal" : "As de Diamantes" , "value" : 1, "priority" : 4, "realValue" : 1},
-- "D02":{"literal" : "Dos de Diamantes" , "value" : 2, "priority" : 4, "realValue" : 2},
-- "D03":{"literal" : "Tres de Diamantes" , "value" : 3, "priority" : 4, "realValue" : 3},
-- "D04":{"literal" : "Cuatro de Diamantes" , "value" : 4, "priority" : 4, "realValue" : 4},
-- "D05":{"literal" : "Cinco de Diamantes" , "value" : 5, "priority" : 4, "realValue" : 5},
-- "D06":{"literal" : "Seis de Diamantes" , "value" : 6, "priority" : 4, "realValue" : 6},
-- "D07":{"literal" : "Siete de Diamantes" , "value" : 7, "priority" : 4, "realValue" : 7},
-- "D08":{"no literal" : "Ocho de Diamantes" , "value" : 8, "priority" : 4, "realValue" : 0.5},
-- "D09":{"no literal" : "Nueve de Diamantes" , "value" : 9, "priority" : 4, "realValue" : 0.5},
-- "D10":{"no literal" : "Diez de Diamantes" , "value" : 10, "priority" : 4, "realValue" : 0.5},
-- "D11":{"no literal" : "Jota de Diamantes" , "value" : 11, "priority" : 4, "realValue" : 0.5},
-- "D12":{"no literal" : "Reina de Diamantes" , "value" : 12, "priority" : 4, "realValue" : 0.5},
-- "D13":{"no literal" : "Rey de Diamantes" , "value" : 13, "priority" : 4, "realValue" : 0.5},

-- "P01":{"literal" : "As de Picas" , "value" : 1, "priority" : 3, "realValue" : 1},
-- "P02":{"literal" : "Dos de Picas" , "value" : 2, "priority" : 3, "realValue" : 2},
-- "P03":{"literal" : "Tres de Picas" , "value" : 3, "priority" : 3, "realValue" : 3},
-- "P04":{"literal" : "Cuatro de Picas" , "value" : 4, "priority" : 3, "realValue" : 4},
-- "P05":{"literal" : "Cinco de Picas" , "value" : 5, "priority" : 3, "realValue" : 5},
-- "P06":{"literal" : "Seis de Picas" , "value" : 6, "priority" : 3, "realValue" : 6},
-- "P07":{"literal" : "Siete de Picas" , "value" : 7, "priority" : 3, "realValue" : 7},
-- "P08":{"no literal" : "Ocho de Picas" , "value" : 8, "priority" : 3, "realValue" : 0.5},
-- "P09":{"no literal" : "Nueve de Picas" , "value" : 9, "priority" : 3, "realValue" : 0.5},
-- "P10":{"no literal" : "Diez de Picas" , "value" : 10, "priority" : 3, "realValue" : 0.5},
-- "P11":{"no literal" : "Jota de Picas" , "value" : 11, "priority" : 3, "realValue" : 0.5},
-- "P12":{"no literal" : "Reina de Picas" , "value" : 12, "priority" : 3, "realValue" : 0.5},
-- "P13":{"no literal" : "Rey de Picas" , "value" : 13, "priority" : 3, "realValue" : 0.5},

-- "C01":{"literal" : "As de Corazones" , "value" : 1, "priority" : 2, "realValue" : 1},
-- "C02":{"literal" : "Dos de Corazones" , "value" : 2, "priority" : 2, "realValue" : 2},
-- "C03":{"literal" : "Tres de Corazones" , "value" : 3, "priority" : 2, "realValue" : 3},
-- "C04":{"literal" : "Cuatro de Corazones" , "value" : 4, "priority" : 2, "realValue" : 4},
-- "C05":{"literal" : "Cinco de Corazones" , "value" : 5, "priority" : 2, "realValue" : 5},
-- "C06":{"literal" : "Seis de Corazones" , "value" : 6, "priority" : 2, "realValue" : 6},
-- "C07":{"literal" : "Siete de Corazones" , "value" : 7, "priority" : 2, "realValue" : 7},
-- "C08":{"no literal" : "Ocho de Corazones" , "value" : 8, "priority" : 2, "realValue" : 0.5},
-- "C09":{"no literal" : "Nueve de Corazones" , "value" : 9, "priority" : 2, "realValue" : 0.5},
-- "C10":{"no literal" : "Diez de Corazones" , "value" : 10, "priority" : 2, "realValue" : 0.5},
-- "C11":{"no literal" : "Jota de Corazones" , "value" : 11, "priority" : 2, "realValue" : 0.5},
-- "C12":{"no literal" : "Reina de Corazones" , "value" : 12, "priority" : 2, "realValue" : 0.5},
-- "C13":{"no literal" : "Rey de Corazones" , "value" : 13, "priority" : 2, "realValue" : 0.5},

-- "T01":{"literal" : "As de Treboles" , "value" : 1, "priority" : 1, "realValue" : 1},
-- "T02":{"literal" : "Dos de Treboles" , "value" : 2, "priority" : 1, "realValue" : 2},
-- "T03":{"literal" : "Tres de Treboles" , "value" : 3, "priority" : 1, "realValue" : 3},
-- "T04":{"literal" : "Cuatro de Treboles" , "value" : 4, "priority" : 1, "realValue" : 4},
-- "T05":{"literal" : "Cinco de Treboles" , "value" : 5, "priority" : 1, "realValue" : 5},
-- "T06":{"literal" : "Seis de Treboles" , "value" : 6, "priority" : 1, "realValue" : 6},
-- "T07":{"literal" : "Siete de Treboles" , "value" : 7, "priority" : 1, "realValue" : 7},
-- "T08":{"no literal" : "Ocho de Treboles" , "value" : 8, "priority" : 1, "realValue" : 0.5},
-- "T09":{"no literal" : "Nueve de Treboles" , "value" : 9, "priority" : 1, "realValue" : 0.5},
-- "T10":{"no literal" : "Diez de Treboles" , "value" : 10, "priority" : 1, "realValue" : 0.5},
-- "T11":{"no literal" : "Jota de Treboles" , "value" : 11, "priority" : 1, "realValue" : 0.5},
-- "T12":{"no literal" : "Reina de Treboles" , "value" : 12, "priority" : 1, "realValue" : 0.5},
-- "T13":{"no literal" : "Rey de Treboles" , "value" : 13, "priority" : 1, "realValue" : 0.5},
-- }}