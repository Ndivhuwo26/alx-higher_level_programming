--  this will Lists all shows contained in the database hbtn_0d_tvshows.
-- this will Displays NULL for shows without genres.
-- the will be Recorded and ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
