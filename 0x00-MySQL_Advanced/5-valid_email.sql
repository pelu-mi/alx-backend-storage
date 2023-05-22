-- Task 5 for MySQL Advanced
-- SQL script: Trigger that resets the attribute valid_email
-- only when the email has been changed
DROP TRIGGER IF EXISTS valid_email_reset;
DELIMITER $$
CREATE TRIGGER valid_email_reset
BEFORE UPDATE ON users
FOR EACH ROW
-- Edit Trigger body below
BEGIN
	IF OLD.email != NEW.email THEN
		SET NEW.valid_email = 0;
	ELSE
		SET NEW.valid_email = NEW.valid_email;
	END IF;
END $$
DELIMITER ;
