-- script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tvsh.title, tvg.genre_id
FROM tv_shows AS tvsh
LEFT JOIN tv_show_genres AS tvg ON tvsh.id = tvg.show_id
ORDER BY tvsh.title ASC, tvg.genre_id ASC
