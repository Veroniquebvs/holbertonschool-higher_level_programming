-- script that lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each
SELECT tvg.name AS genre, COUNT(tvsh.show_id) AS number_of_shows
FROM tv_genres AS tvg
JOIN tv_show_genres AS tvsh ON tvg.id = tvsh.genre_id
GROUP BY tvg.id, tvg.name
ORDER BY number_of_shows DESC;