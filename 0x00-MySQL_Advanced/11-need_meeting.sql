-- Task 11 for MySQL Advanced
-- SQL script that creates a view need_meeting
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80
AND (last_meeting IS NULL OR
last_meeting < SUBDATE(CURRENT_DATE(), INTERVAL 1 MONTH));
