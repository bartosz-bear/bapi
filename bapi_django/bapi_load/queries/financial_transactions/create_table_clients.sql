CREATE TABLE clients (
  id SERIAL PRIMARY KEY,
  client_id INT NOT NULL UNIQUE,
  account_id INT NOT NULL UNIQUE,
  gender VARCHAR(50) NOT NULL CHECK (gender IN ('M', 'F')),
  birth_dt DATE NOT NULL,
  active INT NOT NULL,
  loan INT NOT NULL,
  county_id INT NOT NULL,
  set_split VARCHAR(50) NOT NULL CHECK (set_split IN ('TEST', 'TRAIN'))
);