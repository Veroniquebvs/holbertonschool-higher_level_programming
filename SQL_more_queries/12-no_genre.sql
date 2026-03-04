-- script that lists all shows contained in
-- hbtn_0d_tvshows without a genre linked
SELECT tvsh.title, tvg.genre_id
FROM tv_shows AS tvsh
LEFT JOIN tv_show_genres AS tvg ON tvsh.id = tvg.show_id
WHERE tvg.genre_id IS NULL
ORDER BY tvsh.title ASC, tvg.genre_id ASC;
