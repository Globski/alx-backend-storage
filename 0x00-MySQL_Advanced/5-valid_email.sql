-- This script creates a trigger that resets the valid_email attribute
-- whenever the email of a user is updated.

DELIMITER //

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END; //

DELIMITER ;
