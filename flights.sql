CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    flight_number VARCHAR(10) NOT NULL,
    origin VARCHAR(3),
    destination VARCHAR(3),
    status VARCHAR(20)
);
INSERT INTO flights (flight_number, origin, destination, status)
VALUES 
    (QF101, SYD, MEL, On Time),
    (QF202, MEL, BNE, Delayed),
    (QF303, SYD, PER, On Time);
SELECT * FROM flights WHERE status = Delayed;
UPDATE flights SET status = Boarding WHERE flight_number = QF101;
