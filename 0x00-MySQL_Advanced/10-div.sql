-- Create a function to safely divide two integers
-- Defines a function SafeDiv that takes two integers.
-- Returns 0 if the second argument is 0; otherwise, it returns the division of a by b.
CREATE FUNCTION SafeDiv(a INT, b INT) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    RETURN IF(b = 0, 0, a / b);
END //

DELIMITER ;
