CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    whatsapp TEXT NOT NULL,
    avatar TEXT,
    password TEXT NOT NULL,
    status INTEGER DEFAULT 1
);

INSERT INTO users (id, name, email, whatsapp, avatar, password, status)
VALUES
    ('e4eaaaf2-d142-11e1-b3e4-080027620cdd', 'Administrador', 'admin@gmail.com', '199999999', '', '111111', 1);
