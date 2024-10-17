-- Create a function to safely divide two integers.
-- This function SafeDiv takes two integers as arguments.
-- It returns 0 if the second argument is 0; otherwise, it returns the result of a divided by b.
CREATE FUNCTION SafeDiv(a INT, b INT) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    RETURN IF(b = 0, 0, a / b);
END //
