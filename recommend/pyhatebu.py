# -*- coding:utf-8 -*-
import feedparser
import time
from BeautifulSoup import *

base_url = 'http://b.hatena.ne.jp/'


def get_popular(tag='', threshold='5'):
    url = base_url+'keyword/'+tag+'?mode=rss&sort=hot&threshold='+threshold
    d = feedparser.parse(url)
    entries = []
    for entry_data in d.entries:
        entry = dict()
        # URL
        entry['url'] = entry_data.id
        # Description
        entry['description'] = entry_data.summary_detail.value.encode('utf-8')
        # user id
        comment_page = feedparser.parse('http://b.hatena.ne.jp/entry/rss/'+entry['url']).entries
        user_ids = []
        for user in comment_page:
            user_ids.append(user.title)
        entry['user'] = user_ids
        entries.append(entry)

    return entries
        

# return all posts of the user
# url, tags
def get_userposts(user):
    url = base_url + user + '/rss?of='
    page = 0
    entries = []
    #while(page < 25):
    while(page < 2):
        entry = dict()
        d = feedparser.parse(url+str(page*20))
        if (not d.entries): break
        time.sleep(0.2)
        for entry_data in d.entries:
            entry['link'] = entry_data.link
            # tag data
            tags = []
            if entry_data.has_key('tags'):
                tags = entry_data.tags
            entry['tags'] = tags
            entries.append(entry)
        #t
        print 'crowled: '+str(page*20)
        page += 1
    return  entries

#return description, username
def get_urlposts(url):
    bm_url = base_url+'entry/rss/'+url
    d = feedparser.parse(bm_url)
    posts = []
    for entry in d.entries:
        post = dict()
        # description
        post['description'] = entry.summary_detail.value.encode('utf-8')
        # username
        post['user'] = entry.title
        posts.append(post)
    return posts

#return url, tags, title
def get_hotentry():
    url = base_url+'hotentry?mode=rss'
    d = feedparser.parse(url)
    entries = []
    for entry in d.entries:
        entrydata = dict()
        entrydata['title'] = entry.title.encode('utf-8')
        entrydata['url'] = entry.link
        tags = []
        # tag data
        for tag in entry.tags:
            tags.append(tag.term.encode('utf-8'))
            entrydata['tags'] = tags
        entries.append(entrydata)
    return entries



#get_userposts
#entry_data.keys()
#['summary_detail', 'updated_parsed', 'links', 'title', 'author', 'updated', 'summary', 'content', 'title_detail', 'link', 'id']

#get_hotentry
#print d.feed.keys()
#['subtitle', 'links', 'title', 'rdf_seq', 'rdf_li', 'subtitle_detail', 'title_detail', 'link', 'entries']
#print d.keys()
#['feed', 'status', 'updated', 'version', 'encoding', 'bozo', 'headers', 'etag', 'href', 'namespaces', 'entries']

