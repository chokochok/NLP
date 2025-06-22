CREATE TABLE IF NOT EXISTS input_data (
    id SERIAL PRIMARY KEY,
    prompt TEXT,
    response_a TEXT,
    response_b TEXT
);

CREATE TABLE IF NOT EXISTS predicted_data (
    id INTEGER PRIMARY KEY REFERENCES input_data(id),
    preferred TEXT
);
