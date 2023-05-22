-- Task 13 for MySQL Advanced
-- Stored procedure that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers
-- Edit Procedure body below
BEGIN
	DECLARE length INT DEFAULT 0;
	DECLARE counter INT DEFAULT 0;
	DECLARE total_score INT DEFAULT 0;
	DECLARE total_weight INT DEFAULT 0;
	DECLARE user_id INT DEFAULT 0;

	SELECT COUNT(*) FROM users INTO length;
        SET counter = 0;
        WHILE counter < length DO
	
	-- Loop begins here
	SET user_id = counter;
	SELECT SUM(corrections.score * projects.weight) INTO total_score
	FROM corrections
        INNER JOIN projects
        ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;
	
	SELECT SUM(projects.weight) INTO total_weight
	FROM corrections
	INNER JOIN projects
	ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;

	IF total_weight <= 0 THEN
		UPDATE users
		SET users.average_score = 0
		WHERE users.id = user_id;
	ELSE
		UPDATE users
		SET users.average_score = total_score / total_weight
		WHERE users.id = user_id;
	END IF;
	-- Loop ends here
	END WHILE;
END $$
DELIMITER ;
