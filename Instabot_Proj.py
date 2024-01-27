#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import instabot library
from instabot import Bot


# In[ ]:


#post a Photo
bot = Bot()
bot.login(username="your_userid", password="your_password")
img = "photo.jpg"   # give the path and name if it is in different directory
bot.upload_photo(img, caption="(...")


# In[ ]:


#follow users
from instabot import Bot

bot = Bot()

bot.login(username="your_userid", password="your_password")

# To follow a single user.
bot.follow("username")
# To follow more users.
list_of_user = ["userId1", "userId2", "userId3", "...."] bot.follow_users(list_of_user)


# In[ ]:


#to unfollow user
bot = Bot()
bot.login(username="your_username", password="your_password")

# To unfollow a single user.
bot.unfollow("username")
# To unfollow more users.
unfollow_list = ["userId1", "userId2", "userId3", "..."]
bot.unfollow_users(unfollow_list)


# In[ ]:


#To unfollow Everyone
bot = Bot()
bot.login(username="your_username", password="your_password")

# To unfollow everyone use:
# Please Note that using this will remove all your followings
bot.unfollow_everyone()


# In[ ]:


#count the number of followers for a user
bot = Bot()
bot.login(username="your_username", password="your_password")

# Count number of followers
followers = bot.get_user_followers("username")
print("Total number of followers:")
print(len(followers))


# In[ ]:


#like and comment on a post
bot = Bot()
bot.login(username="your_username", password="your_password")

post_link = "https://www.instagram.com/p/CWqleONFg4/"   # enter the post link
post = bot.get_media_id_from_link(post_link)

# like
bot.like(post)

# comment
bot.comment(post, "Comments ..")


# In[ ]:


bot = Bot()
bot.login(username="your_username", password="your_password")

# To send messages to a single user.
message = "Hello, Thanks for the gift"
bot.send_message(message, "username")

