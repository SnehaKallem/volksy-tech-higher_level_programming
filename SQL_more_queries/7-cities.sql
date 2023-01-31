-- foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT, state_id INT NOT NULL,name VARCHAR(256) NOT NULL,FOREIGN KEY(id) REFERENCES states(id));
