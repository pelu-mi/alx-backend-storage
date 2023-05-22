-- Task 2 for MySQL Advanced
-- SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
SELECT DISTINCT origin, SUM(fans) AS nb_fans
FROM metal_bands
ORDER BY nb_fans;
