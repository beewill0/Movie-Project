import fresh_tomatoes1
import media

#the list of movies we want to appear using our class Movie
friday = media.Movie("Friday",
                        "A story about Craig who has a bad friday",
                        "http://images.moviepostershop.com/friday-movie-poster-1995-1020196025.jpg",
                        "https://www.youtube.com/watch?v=gFmRiWu1Kv0")

inception = media.Movie("Inception",
                        "A man that goes into peoples dreams to help his family",
                        "http://3.bp.blogspot.com/_n7-Pz2d4T-U/TUW9lfRlCMI/AAAAAAAAAFk/RM-EIJOtdZU/s1600/Inception.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

he_got_game = media.Movie("He Got Game",
                          "A story about Basketball, Family, and College",
                          "https://img.yescdn.ru/2015/09/13/poster/He_Got_Game_1.jpg",
                          "https://www.youtube.com/watch?v=yIhthvNiPR4")

friday_after_next = media.Movie("Friday After Next",
                                "The final chapter of the friday series when craig is having another bad Friday.",
                                "https://upload.wikimedia.org/wikipedia/en/f/f6/Friday_After_Next_Poster.jpg",
                                "https://www.youtube.com/watch?v=H3g5QQynaJk")

paid_in_full = media.Movie("Paid In Full",
                           "A young man from Harlem, forced to cope with the 1980s drug scene", 
                           "https://upload.wikimedia.org/wikipedia/en/thumb/7/72/Paidinfullposter.jpg/220px-Paidinfullposter.jpg",
                           "https://www.youtube.com/watch?v=Y63NfERYsL4&oref=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DY63NfERYsL4&has_verified=1")

janky_promoters = media.Movie("Janky Promoters",
                              "Two shady concert promoters get in trouble when their chance to book a superstar rapper goes bad",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyNzA4Mzk4MV5BMl5BanBnXkFtZTgwNzk0MjA2MDE@._V1_UY268_CR9,0,182,268_AL_.jpg",
                              "https://www.youtube.com/watch?v=HZRH5M1fJtY&oref=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DHZRH5M1fJtY&has_verified=1")
                              

#Movies is the list of our movies we want to have
movies = [friday, inception, he_got_game, friday_after_next, paid_in_full, janky_promoters]

#This script will open html for our list above to be displayed on the web
fresh_tomatoes1.open_movies_page(movies)
