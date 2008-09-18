# -*- coding: utf-8 -*-
# put hatebu data to db
from pyhatebu import *
from pysqlite2 import dbapi2 as sqlite

class db:
    def __init__(self, dbname):
        self.con = sqlite.connect(dbname)

    def __del__(self):
        self.con.close()

    def dbcommit(self):
        self.con.commit()

    def addbookmarks(self, user):
        print 'Saving ' + user + '\'s bookmarks'
        d = get_userposts(user)
        userid = self.getuserid(user)
        #print d
        for post in d:
            #get url id
            urlid = self.con.execute("select rowid from urls where url = '%s'"  \
                                     % post['link']).fetchone()
            if urlid == None:
                #something wrong
                ###
                #self.con.close()
                ###
                cur = self.con.execute("insert into urls(url)  \
                values ('%s')" % post['link'])
                #self.dbcommit()
                urlid = cur.lastrowid
                print 'urlid', urlid
            # put data(urlid, userid, tagids) to db
            cur = self.con.execute("insert into userposts(userid, urlid)  \
            values (%d, %d)" % (userid, urlid))
            upid = cur.lastrowid

            # get tag id
            tags = post['tags']
            tagids = []
            for tag in tags:
                tagid = self.con.execute("select rowid from tags  \
                where tag = '%s'" % tag).fetchone()
                if tagid != None:
                    cur = self.con.execute("insert into tags(name)  \
                    values ('%s')" % tag)
                    tagid = cur.lastrowid
                tagids.append(tagid)

            print 'tagids', tagids
            #put data(upid, tagid)
            for tagid in tagids:
                self.con.execute("insert into posttags(upid, tagid)  \
                values (%d, %d)" % (upid, tagid))
            self.commit()
            


    def getuserid(self, user):
        id = self.con.execute("select rowid from users where name = '%s'" % user).fetchone()
        if id != None:
            return id
        else:
            cur = self.con.execute("insert into users(name) values ('%s')" % user)
            self.dbcommit()
            return cur.lastrowid
            
        
    def selectall(self, table):
        print self.con.execute("select * from %s" % table).fetchone()
