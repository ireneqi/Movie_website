# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

#defined the instances of movies
forrest_gump = media.Movie("Forrest Gump", \
"Forrest gump (Tom Hanks) is at the end of world war ii was born in the United States shortly after the south Alabama a block town,\
he congenital weak-minded, IQ is only 75, but his mother is a personality strong woman, she often encourages forrest gump, stupid is as stupid does to him.",\
 "http://r1.ykimg.com/051600005992AC78ADBA1F04C20BF0FF",\
 "http://v.youku.com/v_show/id_XNzQ4NzQ3NzI4.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")
#print (toy_story.storyline)
wrestling_dad = media.Movie("Wrestling! Dad",\
 "Mahavia was once a promising wrestler, and after giving up his career,\
  his greatest regret was that he could not win a gold medal for his country. Mahavia pinned the hope on his unborn son, who knew that his wife had given him two daughters,\
  named gitta and babita. Let ops did not think of, the two girls showed excellent wrestling talent, awaken to let him, even a girl,\
  standing in the game can also be self-respect, to countries and their own glory. In this way, under the guidance of mahavia,\
  geta and babbita began to train hard, and the two men made rapid progress, and soon became a local celebrity because of their winning in the competition.\
  In order to get more opportunities, gita went to the national institute of physical education, where she will face greater temptation and more choices.",\
  "http://g2.ykimg.com/051600005902B3A1ADBAC3F67B05AB38",\
  "http://v.youku.com/v_show/id_XMjczOTQ2MjQ4NA==.html?spm=a2h1n.8261147.around_2.5~5~5~5~A")
#print (avatar.storyline)
#forrest_gump.show_trailer()
sherlock = media.Movie('Sherlock', \
 "Sherlock regular plot setting is Arthur Conan Doyle original story moved to the modern society,\
 this special article by clever plot Settings, let the characters through back to the original Victorian era,\
 without the story of the last season. On the streets of Victorian London, the husband was surprised to see his wife return in a wedding dress in a wedding dress, \
 but the wife committed suicide a few hours before, whether it was a haunting or a blood feud. From the fog of lime house to the depths of the abandoned church,\
 Sherlock Holmes (Benedict Chambers batch), Watson (Martin freeman) and their friends had to try their best to deal with this from the grave to climb out of the enemy,\
 but the ultimate truth took everyone by surprise...",\
 "http://r1.ykimg.com/051600005A192AE9ADBDD3053603EC36",\
 "http://v.youku.com/v_show/id_XMzIxMDE3NDEyMA==.html")
#sherlock.show_trailer()
#list instances in movies
movies = [forrest_gump, wrestling_dad, sherlock]
#call back the function of open_movies_page to generate the view
fresh_tomatoes.open_movies_page(movies)
