-- Task 10 for MySQL Advanced
-- SQL script that creates a function SafeDiv
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
-- Edit Function body below
BEGIN
	DECLARE div FLOAT DEFAULT 0.0;
	IF b != 0 THEN
		SET div = a / b;
	END IF;
	RETURN div;
END $$
DELIMITER ;
