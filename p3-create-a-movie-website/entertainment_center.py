# -*- coding: utf-8 -*-
# Intro to Programming Nanodegree
# Project 3 - Create a Movie Website
# Ricardo Yoshitomi

import media
import fresh_tomatoes

eternal_sunshine = media.Info("Eternal Sunshine of the Spotless Mind", 
						"When their relationship turns sour, a couple undergoes a procedure to have each other erased from their memories. But it is only through the process of loss that they discover what they had to begin with. (IMDb website)", 
						"https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg", 
						"https://www.youtube.com/watch?v=rb9a00bXf-U",
						"Michel Gondry", 
						"Charlie Kaufman (story), Michel Gondry (story), Pierre Bismuth (story), Charlie Kaufman (screenplay)",
						"Jim Carrey, Kate Winslet, Tom Wilkinson",
						"2004",
						"Drama, Fantasy, Romance",
						"1h 48min",
						"USA",
						"English",
						"March 19, 2004 (USA)")

the_hobbit = media.Info("The Hobbit: An Unexpected Journey", 
						"A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug. (IMDb website)", 
						"https://upload.wikimedia.org/wikipedia/en/thumb/b/b3/The_Hobbit-_An_Unexpected_Journey.jpeg/220px-The_Hobbit-_An_Unexpected_Journey.jpeg", 
						"https://www.youtube.com/watch?v=SDnYMbYB-nU",
						"Peter Jackson", 
						"Fran Walsh	(screenplay), Philippa Boyens (screenplay), Peter Jackson (screenplay), Guillermo del Toro (screenplay), J.R.R. Tolkien (novel)",
						"Ian McKellen, Martin Freeman, Richard Armitage",
						"2012",
						"Adventure, Fantasy",
						"2h 49min",
						"USA | New Zealand",
						"English",
						"December 12, 2012 (New Zealand)")						

harry_potter = media.Info("Harry Potter and the Prisoner of Azkaban", 
						"It's Harry's third year at Hogwarts; not only does he have a new 'Defense Against the Dark Arts' teacher, but there is also trouble brewing. Convicted murderer Sirius Black has escaped the Wizards' Prison and is coming after Harry. (IMDb website)", 
						"http://ia.media-imdb.com/images/M/MV5BMTY4NTIwODg0N15BMl5BanBnXkFtZTcwOTc0MjEzMw@@._V1_SY1000_CR0,0,676,1000_AL_.jpg", 
						"https://www.youtube.com/watch?v=R69laoH02xg",
						"Alfonso Cuarón", 
						"J.K. Rowling (novel), Steve Kloves (screenplay)",
						"Daniel Radcliffe, Emma Watson, Rupert Grint",
						"2004",
						"Adventure, Family, Fantasy",
						"2h 22min",
						"UK | USA",
						"English",
						"May 31, 2004 (UK)")

wall_e = media.Info("Wall-e", 
						"In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind. (IMDb website)", 
						"https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg", 
						"https://www.youtube.com/watch?v=alIq_wG9FNk",
						"Andrew Stanton", 
						"Andrew Stanton (original story by), Pete Docter (original story by), Andrew Stanton (screenplay), Jim Reardon (screenplay)",
						"Ben Burtt, Elissa Knight, Jeff Garlin",
						"2008",
						"Animation, Adventure, Family ",
						"1h 38min",
						"USA",
						"English",
						"June 27, 2008 (USA)")

the_lion_king = media.Info("The Lion King", 
						"Lion cub and future king Simba searches for his identity. His eagerness to please others and penchant for testing his boundaries sometimes gets him into trouble. (IMDb website)", 
						"https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg", 
						"https://www.youtube.com/watch?v=nQIhEMnseYk",
						"Roger Allers, Rob Minkoff", 
						"Irene Mecchi (screenplay), Jonathan Roberts (screenplay)",
						"Matthew Broderick, Jeremy Irons, James Earl Jones",
						"1994",
						"Animation, Adventure, Drama ",
						"1h 29min",
						"USA",
						"English",
						"June 15, 1994 (USA)")

iron_man = media.Info("Iron Man", 
						"After being held captive in an Afghan cave, a billionaire engineer creates a unique weaponized suit of armor to fight evil. (IMDb website)", 
						"https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG", 
						"https://www.youtube.com/watch?v=8hYlB38asDY",
						"Jon Favreau", 
						"Mark Fergus (screenplay), Hawk Ostby (screenplay), Art Marcum (screenplay), Matt Holloway (screenplay), Stan Lee (characters), Don Heck (characters), Larry Lieber (characters), Jack Kirby (characters)",
						"Robert Downey Jr., Gwyneth Paltrow, Terrence Howard",
						"2008",
						"Action, Adventure, Sci-Fi",
						"2h 6min",
						"USA",
						"English",
						"April 30, 2008 (USA)")


movies = [eternal_sunshine, the_hobbit, harry_potter, wall_e, the_lion_king, iron_man]
fresh_tomatoes.open_movies_page(movies)
