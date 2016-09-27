"""

 * Project 1 : Movie Trailer Website
 * Full Stack Web Developer Nanodegree
 * 7/6/2015
 * Instructor - Kunal
 * Author - Aanya

"""

import media
import fresh_tomatoes


# Populating with movie information
# Valid ratings array: ["G", "PG", "PG-13", "R"] , defined in class Video

toy_story = media.Movie(media.Video
                       ("Toy Story", "81 mins"),
                       media.Video.VALID_RATINGS[0],
                       "A story of a boy and his toys that come alive",
                       "http://imgs.abduzeedo.com/files/articles/toystory3/toystory3_35.jpg",  # noqa
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(media.Video
                    ("Avatar", "2h 42m"),
                    media.Video.VALID_RATINGS[2],
                    "A marine on an alien planet",
                    "http://photos.imageevent.com/wrestlingfanaticactionfigures/jamescameronavatarthemovie/vertical-bmw-avatar-movie-high-definition-images-free-333798.jpg",  # noqa
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

lor_1 = media.Movie(media.Video
                   ("The Lord of the Rings: \
                    The Fellowship of the Ring", "3h 48m"),
                    media.Video.VALID_RATINGS[2],
                    "A tale of a hobbit who embark on \
                    dangerous journey to save the world ",
                    "http://image.tmdb.org/t/p/original/9HG6pINW1KoFTAKY3LdybkoOKAm.jpg",  # noqa
                    "https://www.youtube.com/watch?v=Pki6jbSbXIY")

lor_2 = media.Movie(media.Video
                    ("The Lord of the Rings: The Two Towers", "3h 55m"),
                     media.Video.VALID_RATINGS[2],
                     "The movie follows the continuing \
                     quest of Frodo and the Fellowship to \
                     destroy the One Ring",
                     "http://img4.wikia.nocookie.net/__cb20150203041214/lotr/images/9/98/The_two_tower.jpg",  # noqa
                     "https://www.youtube.com/watch?v=cG-1Gtus7KQ")

lor_3 = media.Movie(media.Video
                   ("The Lord of the Rings: \
                   The Return of the King", "3h 21m"),
                   media.Video.VALID_RATINGS[2],
                   "Presents the final confrontation between \
                   the forces of good and evil fighting for \
                   control of the future of Middle-earth.",
                   "http://www.gstatic.com/tv/thumb/movieposters/33156/p33156_p_v7_aa.jpg",  # noqa
                   "https://www.youtube.com/watch?v=rCZ3SN65kIs")

how_to_train_your_dragon = media.Movie(media.Video
                    ("How to Train Your Dragon", "1h 38m"),
                     media.Video.VALID_RATINGS[1],
                     "The story takes place in a mythical Viking \
                     world where a young Viking teenager named \
                     Hiccup aspires to follow his tribe's \
                     tradition of becoming a dragon slayer.",
                     "https://d12vb6dvkz909q.cloudfront.net/uploads/galleries/22024/how-to-train-your-dragon-poster-1.jpg",  # noqa
                     "https://www.youtube.com/watch?v=oKiYuIsPxYk")

# List of movie objects which is input to file fresh_tomatoes.py
movies = [toy_story, avatar, how_to_train_your_dragon, lor_1, lor_2, lor_3]

# Using freah_tomatoes.py file to display website
fresh_tomatoes.open_movies_page(movies)
