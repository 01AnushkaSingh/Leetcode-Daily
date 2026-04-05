WITH t1 AS (
    SELECT
    player_id,
    MIN(event_date) AS first_login_date
FROM 
    Activity
GROUP BY 
    player_id
)

SELECT 
    ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM 
    Activity a1
JOIN
    t1 t ON a1.player_id = t.player_id 
    AND a1.event_date = DATE_ADD(t.first_login_date , INTERVAL 1 DAY);