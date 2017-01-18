-- Project 4 in FSND track, Jan 18 2017


DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;
\c tournament

create table players (
    id SERIAL primary key,
    name text

);


create table matches (
    match_id SERIAL primary key,
    winner_id SERIAL REFERENCES Players,
    loser_id SERIAL REFERENCES Players

);
