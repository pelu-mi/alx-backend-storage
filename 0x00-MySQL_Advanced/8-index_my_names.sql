-- Task 8 for MySQL Advanced
-- Create an index idx_name_first on the table names
-- and the first letter of name
DROP INDEX IF EXISTS idx_name_first_score;
CREATE INDEX idx_name_first_score
ON names (LEFT(name), score);
