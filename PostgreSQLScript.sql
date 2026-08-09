CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE,
    email VARCHAR UNIQUE,
    hashed_password VARCHAR
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    title VARCHAR,
    amount DOUBLE PRECISION NOT NULL,
    type VARCHAR NOT NULL,
    category VARCHAR,
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    owner_id INTEGER,

    CONSTRAINT fk_transactions_owner
        FOREIGN KEY (owner_id)
        REFERENCES users(id)
);

CREATE INDEX idx_transactions_owner_id
    ON transactions(owner_id);