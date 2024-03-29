-- The script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT a.name
FROM tv_genres AS a
INNER JOIN tv_show_genres AS b
ON a.id = b.genre_id
INNER JOIN tv_shows AS c
ON c.id = b.show_id
WHERE c.title = 'Dexter'
ORDER BY a.name ASC;
