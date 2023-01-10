create database projecte1;
use projecte1;

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
