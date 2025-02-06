CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    whatsapp TEXT NOT NULL,
    avatar TEXT,
    password TEXT NOT NULL,
    status INTEGER DEFAULT 1,
    active INTEGER DEFAULT 0
);

INSERT INTO users (id, name, email, whatsapp, avatar, password, status, active)
VALUES
    ('e4eaaaf2-d142-11e1-b3e4-080027620cdd', 'Teste da Silva', 'teste@gmail.com', '123456789', 'avatar.png', '111111', 1, 0);
