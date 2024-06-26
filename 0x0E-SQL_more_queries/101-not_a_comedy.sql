--Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

SELECT DISTINCT  'title'
FROM 'tv_show_genres' AS t
INNER JOIN 'tv_show_genres' AS s
ON s. 'show_id' = t. '_id'

LEFT JOIN 'tv_genres' AS g
ON g. '_id' =  s. 'genre_id'
WHERE t. 'title' NOT IN (SELECT 'title'
FROM 'tv_show' AS t
INNER JOIN 'tv_show_genres' AS s
ON s. 'show_id' =  t. 'id'

INNER JOIN 'tv_genres' AS g
ON g. 'id' =  s. 'genre_id'
WHERE g. 'name' = "Comedy")
ORDER BY g. 'title' ;

