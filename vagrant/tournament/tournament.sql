-- Table definitions for the tournament project.

--psql commands to create the database and connect to it:
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

DROP TABLE IF EXISTS MATCH;
CREATE TABLE MATCH(
	tournament INTEGER,	-- GUID for row in TOURNAMENT table
	round INTEGER,  -- identifies the tournament round this match belongs to
	p1 INTEGER,  -- GUID for row in REGISTRATION table for player 1
	score1 INTEGER,  -- score for player 1 in this match, NULL until match ourcome recoreded
	p2 INTEGER,  -- GUID for row in REGISTRATION table for player 2
	score2 INTEGER);  -- score for player 2 in this match, NULL until match ourcome recoreded

DROP TABLE IF EXISTS TOURNAMENT;
CREATE TABLE TOURNAMENT(
	id SERIAL UNIQUE,  -- GUID for this row
	name VARCHAR(128),	-- display name for this TOURNAMENT 
	round INTEGER);  -- identifies the current round to be played, NULL when done

DROP TABLE IF EXISTS REGISTRATION;
CREATE TABLE REGISTRATION(
	id SERIAL UNIQUE,  -- GUID for this row
	player INTEGER,  -- GUID for row in PERSON table - the person registered
	tournament INTEGER);	-- GUID for row in TOURNAMENT table - the tournament entered

DROP TABLE IF EXISTS PERSON;
CREATE TABLE PERSON(
	id SERIAL UNIQUE,  -- GUID for this row
	name VARCHAR(128),  -- display name for this PERSON
	born TIMESTAMP);	-- date this person was born

-- example use:
--
-- insert into tournament (name, round) values('test tournament',0);
-- insert into person (name,born) values('jan', '1959-01-08 00:00:00');
-- insert into person (name,born) values('richard', '1957-10-29 00:00:00');
-- insert into match values(0,0,0,null,1,null);
-- insert into registration (player,tournament) values(0,0);
-- insert into registration (player,tournament) values(1,0);
--
-- select t.name, t.round, p1.name, m.score1, p2.name, m.score2
-- 	from match m
-- 	join tournament t on m.tournament=t.id
-- 	join registration r1 on m.p1=r1.id
-- 	join person p1 on r1.player=p1.id
-- 	join registration r2 on m.p2=r2.id
-- 	join person p2 on r2.player=p2.id;
