CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100),
    unique_id VARCHAR(100)
);

CREATE TABLE vital_signs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    pulse_rate INT,
    oxygen_level INT,
    temperature FLOAT,
    accelerometer_data VARCHAR(100),
    gyroscope_data VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
