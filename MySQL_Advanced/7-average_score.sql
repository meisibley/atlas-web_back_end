-- Write a SQL script that creates a stored procedure
-- ComputeAverageScoreForUser that computes and store the average score
-- for a student. Note: An average score can be a decimal
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE av_score FLOAT;
    SET av_score = (SELECT AVG(score) FROM corrections
                    WHERE corrections.user_id = user_id);
    UPDATE users
        SET average_score = av_score
        WHERE users.id = user_id;
END; $$
DELIMITER ;