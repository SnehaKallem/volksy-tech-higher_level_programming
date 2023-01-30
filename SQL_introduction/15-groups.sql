-- total number of records
SELECT score, count(*) as number from second_table GROUP BY score ORDER BY number DESC;
