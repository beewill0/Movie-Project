import fresh_tomatoes1
import media
# The list of movies we want to appear using our class Movie
friday = media.Movie("Friday",
                     "A story about Craig who has a bad friday",
                     "https://i.ytimg.com/vi/sWucZKHdKLw/hqdefault.jpg",
                     "https://www.youtube.com/watch?v=gFmRiWu1Kv0")

inception = media.Movie("Inception",
                        "A man that goes into peoples dreams to help family",
                        "http://www.impawards.com/2010/posters/inception_ver6.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

he_got_game = media.Movie("He Got Game",
                          "A story about Basketball, Family, and College",
                          "https://img.yescdn.ru/2015/09/13/poster/He_Got_Game_1.jpg",
                          "https://www.youtube.com/watch?v=yIhthvNiPR4")

friday_after_next = media.Movie("Friday After Next",
                                "The final chapter of the friday series.",
                                "http://oi63.tinypic.com/348how9.jpg",
                                "https://www.youtube.com/watch?v=H3g5QQynaJk")

paid_in_full = media.Movie("Paid In Full",
                           "A young man forced to cope with the 1980s drug scene",
                           "http://images3.static-bluray.com/movies/covers/77735_front.jpg",
                           "https://www.youtube.com/watch?v=d9vC9gUnTTc")

janky_promoters = media.Movie("Janky Promoters",
                              "Two promoters in trouble when their chance to book a rapper goes bad",
                              "http://www.dvd-covers.org/d/96051-3/Janky_Promoters_-_English_f.jpg",
                              "https://www.youtube.com/watch?v=xWfE7KSbtwU")
# Movies is the list of our movies we want to have
movies = [friday, inception, he_got_game, friday_after_next, paid_in_full, janky_promoters]

# This script will open html for our list above to be displayed on the web
fresh_tomatoes1.open_movies_page(movies)
