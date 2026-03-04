-- a script that lists all shows contained in hbtn_0d_tvshows
SELECT tvsh.title, genre_id
FROM tv_shows AS tvsh
INNER JOIN tv_show_genres AS tvg ON tvg.show_id = tvsh.id
ORDER BY tvsh.title ASC, tvg.genre_id ASC;