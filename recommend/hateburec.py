# -*- coding: utf-8 -*-
# get hatebu data
from pyhatebu import get_popular, get_userposts, get_urlposts
import time

# get user data and put data in a dict
def initializeUserDict(tag, count = 5):
    user_dict = {}
    # get the top count' popular posts 
    for p1 in get_popular(tag=tag)[0:count]:
        # find all users who posted this 
        for p2 in get_urlposts(p1['url']):
            user=p2['user']
            user_dict[user]={}
    print user_dict
    return user_dict

# get post data of each users and put data in the dict
def fillItems(user_dict):
    all_items = {}
    for user in user_dict:
        print 'user: '+user
        for i in range(3):
            try:
                posts = get_userposts(user)
                break
            except:
                print "Failed user " + user + ", retrying"
                time.sleep(4)
        for post in posts:
            #print post
            url = post['link']
            user_dict[user][url] = 1.0
            all_items[url] = 1
    for ratings in user_dict.values():
        for item in all_items:
            if item not in ratings:
                ratings[item] = 0.0

