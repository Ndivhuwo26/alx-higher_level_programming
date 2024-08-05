--Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
  SELECT g. 'name' AS 'genre' ,
FROM 'tv_shows' AS g
LEFT JOIN 'tv_show_genres' AS s
ON g. 'id' = s. 'genre_id'
LEFT JOIN 'tv_show_genres' AS t
ON t. 'id' = s. 'show_id'
WHERE t. 'titile' = "Dexter"
ORDER BY g. 'name' ;

