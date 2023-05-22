-- Task 7 for MySQL Advanced
-- Stored procedure that computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
-- Edit Procedure body below
BEGIN
	DECLARE avg_score FLOAT DEFAULT 0.0;
	SELECT AVG(score) INTO avg_score FROM corrections
	WHERE corrections.user_id = user_id;
	UPDATE users
	SET users.average_score = avg_score
	WHERE users.id = user_id;
END $$
DELIMITER ;
