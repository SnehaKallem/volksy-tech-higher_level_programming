-- dump database and display in descending order oftv shows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows RIGHT JOIN tv_show_genres ON tv_shows_genres.genre_id = tv_shows.id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
