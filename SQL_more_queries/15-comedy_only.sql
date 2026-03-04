-- a script that lists all Comedy
-- shows in the database hbtn_0d_tvshows
SELECT tvsh.title
FROM tv_shows AS tvsh
INNER JOIN tv_show_genres AS tvsg ON tvsh.id = tvsg.show_id
INNER JOIN tv_genres AS tvg ON tvg.id = tvsg.genre_id
WHERE tvg.name = 'Comedy'
ORDER BY tvsh.title ASC
