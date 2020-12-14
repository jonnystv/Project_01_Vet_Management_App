DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

-- CREATE TABLE animals (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255),
--     type VARCHAR(255),
--     dob VARCHAR(255),
--     age VARCHAR(255),
--     notes TEXT,
--     owner VARCHAR(255),
--     owner_tel VARCHAR(255),
--     owner_email VARCHAR(255),
--     vet_id INT REFERENCES vets(id)
--     );