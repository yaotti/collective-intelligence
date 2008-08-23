#something wrong
#doesn't work well
def writedict(filename, data):
    fw = open(filename, 'w')
    for key in dict.keys():
        print >> key, ':' 
        for post in dict[key]:
            print >> post
    fw.close()

def disp(dict):
    for key in dict.keys():
        print key, ':'
        for post in dict[key]:
            print post
