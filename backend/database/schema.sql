CREATE TABLE university
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE department
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    code VARCHAR(20),
    created_at TIMESTAMP DEFAULT now(),
    university_id INTEGER NOT NULL REFERENCES university
    (id) ON
    DELETE CASCADE
);

CREATE TABLE faculty
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100),
    email VARCHAR(150) UNIQUE,
    phone VARCHAR(50),
    created_at TIMESTAMP DEFAULT now(),
    department_id INTEGER NOT NULL REFERENCES department
        (id) ON
        DELETE
        SET NULL
);


CREATE TABLE student
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100),
    email VARCHAR(150) UNIQUE,
    roll_number VARCHAR(50) UNIQUE,
    created_at TIMESTAMP DEFAULT now(),
    department_id INTEGER REFERENCES department
            (id)
);


CREATE TABLE classroom
(
    id SERIAL PRIMARY KEY,
    room_no VARCHAR(100),
    capacity INTEGER,
    location VARCHAR(100),
    created_at TIMESTAMP DEFAULT now()
);
