-- a script that lists all shows
-- and all genres linked to that show
SELECT tvsh.title, tvg.name
FROM tv_shows AS tvsh
LEFT JOIN tv_show_genres AS tvsg ON tvsh.id = tvsg.show_id
LEFT JOIN tv_genres AS tvg ON tvg.id = tvsg.genre_id
ORDER BY tvsh.title ASC, tvg.name ASC;
