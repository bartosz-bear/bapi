CREATE TABLE counties (
  id SERIAL PRIMARY KEY,
  county_id INT NOT NULL UNIQUE,
  n_inhab INT NOT NULL,
  n_cities INT NOT NULL,
  urban_ratio DECIMAL(10, 2) NOT NULL,
  avg_salary MONEY NOT NULL,
  unemp_95 DECIMAL(10, 2) NOT NULL,
  unemp_96 DECIMAL(10, 2) NOT NULL,
  n_entr INT NOT NULL,
  crime_95 INT NOT NULL,
  crime_96 INT NOT NULL
);