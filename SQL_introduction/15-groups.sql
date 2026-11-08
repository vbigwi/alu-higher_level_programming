-- Counts records per score in second_table, most frequent first
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
