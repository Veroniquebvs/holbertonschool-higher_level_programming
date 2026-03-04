--  a script that uses the hbtn_0d_tvshows
-- database to lists all genres of the show Dexter
SELECT tvg.name
FROM tv_shows AS tvsh
INNER JOIN tv_show_genres AS tvsg ON tvsh.id = tvsg.show_id
INNER JOIN tv_genres AS tvg ON tvsg.genre_id = tvg.id
WHERE tvsh.title = 'Dexter'
ORDER BY tvg.name ASC;
