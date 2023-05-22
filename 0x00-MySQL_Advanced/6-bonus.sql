-- Task 6 for MySQL Advanced
-- Stored procedure that computes and store the average score for a student
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus (IN user_id INT, INOUT project_name VARCHAR(255), IN score INT)
-- Edit Procedure body below
BEGIN
	DECLARE proj_id INT DEFAULT 0;
	IF SELECT EXISTS(SELECT * FROM projects WHERE name = project_name) THEN
		INSERT INTO projects (name)
		VALUES (project_name);
	END IF;
	SELECT id INTO proj_id FROM projects WHERE name = project_name;
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, @proj_id, score);
END $$
DELIMITER ;
