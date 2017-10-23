BEGIN TRANSACTION;
DROP TABLE IF EXISTS `match`;
CREATE TABLE IF NOT EXISTS `match` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`date`	TEXT NOT NULL,
	`heure`	TEXT,
	`equipe_1`	INTEGER NOT NULL,
	`equipe_2`	INTEGER NOT NULL,
	`score_1`	INTEGER,
	`score_2`	INTEGER,
	`cote_1`	NUMERIC,
	`cote_N`	NUMERIC,
	`cote_2`	NUMERIC,
	`competition`	INTEGER NOT NULL,
	FOREIGN KEY(`equipe_1`) REFERENCES `equipe`(`id`),
	FOREIGN KEY(`equipe_2`) REFERENCES `equipe`(`id`),
	FOREIGN KEY(`competition`) REFERENCES `competition`(`id`)
);
DROP TABLE IF EXISTS `equipe`;
CREATE TABLE IF NOT EXISTS `equipe` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`nom`	TEXT NOT NULL,
	`pays`	TEXT
);
DROP TABLE IF EXISTS `competition`;
CREATE TABLE IF NOT EXISTS `competition` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`nom`	TEXT NOT NULL,
	`type`	INTEGER
);
COMMIT;
