-- Lists score and name of second_table rows that have a name, top first
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
