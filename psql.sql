CREATE DATABASE minecraft_calculator;
\connect minecraft_calculator;
CREATE SCHEMA MPC;
CREATE USER mpc_acc WITH LOGIN PASSWORD 'mpc_acc';
REASSIGN OWNED BY (select current_user) to mpc_acc;
GRANT ALL PRIVILEGES ON DATABASE minecraft_calculator TO mpc_acc;
GRANT ALL PRIVILEGES ON ALL TABLES ON SCHEMA MPC;

CREATE TABLE IF NOT EXISTS MPC.SELLS(
	CD SERIAL PRIMARY KEY NOT NULL UNIQUE,
	ITEM TEXT NOT NULL,
	QTD  INT  NOT NULL DEFAULT 1,
	VL_CURRENCY MONEY NOT NULL,
	DT_TM_SELL TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE OR REPLACE VIEW MPC.AGV_PRICES AS
SELECT ITEM, AVG(VL_CURRENCY::NUMERIC(10, 2))::NUMERIC(10, 2) AS PRICE FROM MPC.SELLS GROUP BY ITEM ORDER BY PRICE;
