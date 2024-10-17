-- This script creates a table named 'users' if it does not already exist.
-- The 'users' table includes the following columns:
-- 1. id: An integer that auto-increments and serves as the primary key. It cannot be null.
-- 2. email: A string (maximum 255 characters) that cannot be null and must be unique to enforce business rules.
-- 3. name: A string (maximum 255 characters) that can hold the user's name.
-- 4. country: An enumeration of countries (US, CO, TN) that cannot be null,
--    with the default value set to 'US'.

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
