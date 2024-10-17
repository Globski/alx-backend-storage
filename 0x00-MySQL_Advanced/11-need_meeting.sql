-- Create a view to list students with scores under 80
-- and either no last_meeting date or last_meeting more than 1 month ago.
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
