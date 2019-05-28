import praw
import re
from urllib.parse import *
import threading
import requests
import time
from bs4 import BeautifulSoup


posts = []
foundLinks = []
newLinks = []
workingLinks = []
threads = 0
maxThreads = 250
postsToLoad = 10
timeoutForTesting = 10

URL_REGEX = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""

blackList = ["ch0c",
             "pastebin.com",
             "anotherBlacklistedItem",
             "filepursuit",
             "github.com",
             "reddit.com",
             "shodan.io",
             "wikipedia",
             "the-eye",
             "twitter",
             "facebook",
             "youtube",
             "tumblr.com",
             "archive.org",
             "archive.org",
             "i.redd.it",
             "redditmedia.com",
             "rg.to",
             ]


# disabled
"""
"https://api.pushshift.io/reddit/search/submission?subreddit=opendirectories&limit=10000",
"""

# the number after before=  is the date in epoch format
# I found the values below by checking the last result at each link

pagesToCheckForLinks = [
    "https://api.pushshift.io/reddit/search/submission?subreddit=opendirectories&limit=1000&after=1543663785",
    "https://api.pushshift.io/reddit/search/submission?subreddit=opendirectories&limit=1000&before=1543663785",
    "https://api.pushshift.io/reddit/search/submission?subreddit=opendirectories&limit=1000&before=1526916567",
    "https://api.pushshift.io/reddit/search/submission?subreddit=opendirectories&limit=1000&before=1513931734",
    "https://api.pushshift.io/reddit/search/submission?subreddit=opendirectories&limit=1000&before=1497490290",
    "https://api.pushshift.io/reddit/search/submission?subreddit=opendirectories&limit=1000&before=1484223692",
    "https://api.pushshift.io/reddit/search/submission?subreddit=opendirectories&limit=1000&before=1460743035",
    "https://api.pushshift.io/reddit/search/submission?subreddit=opendirectories&limit=1000&before=1444658067",
    "https://api.pushshift.io/reddit/search/submission?subreddit=opendirectories&limit=1000&before=1440908907",
    "https://api.pushshift.io/reddit/search/submission?subreddit=opendirectories&limit=1000&before=1440996579",
    "https://api.pushshift.io/reddit/search/submission?subreddit=opendirectories&limit=1000&before=1440991337",
]

# reddit settings
bot = praw.Reddit(client_id='---',
                  client_secret='---',
                  user_agent='MySimpleBot v0.1',
                  username='---',
                  password='---')

print('logged in to Reddit as: ' + str(bot.user.me()))


# to read existing file
def updateTextInFileVar():
    global textInFile
    file = open("opendirectories.txt", "r")
    textInFile = file.read()
    file.close()


# function for sorting on domain and subdomain
def domain(link):
    try:
        netlocParts = urlsplit(link).netloc.split(".")
        sortTerm = netlocParts[-2]
        try:
            sub = netlocParts[-3]
            sortTerm += sub
        except:
            pass
        return sortTerm
    except:
        return link


def checkDirectory(linkToCheck):
    global workingLinks
    global threads
    netLoc = urlsplit(linkToCheck).netloc
    dirLinks = []

    try:
        page = requests.get(linkToCheck, timeout=timeoutForTesting).text

        if "</script>" in page and "bitdl" not in linkToCheck and 'bitdownload' not in linkToCheck and "Index of /" not in page:  # bitdl is an od with js
            print(linkToCheck, "has javascript. Skipping")
            raise ZeroDivisionError

        soup = BeautifulSoup(page, 'html.parser')

        for link in soup.findAll('a'):
            href = str(link.get('href'))

            if "?C" in href:  # skip sorting links
                continue

            fullLink = urljoin(linkToCheck, href)
            if "?C=" not in fullLink and len(fullLink) > len(link):
                if netLoc in fullLink and fullLink not in dirLinks:
                    dirLinks.append(fullLink)

        # print(len(dirLinks), "found on", linkToCheck)

        if len(dirLinks) >= 2:
            workingLinks.append(linkToCheck)
            if linkToCheck not in textInFile:
                print(linkToCheck, "is new")

                pFile = open("opendirectories.txt", "a")
                pFile.write(linkToCheck + "\n")
                pFile.close()

    except Exception as e:
        print(linkToCheck, "failed:")

    threads -= 1

# if there is 123.com/files/123 and 123.com/files keep only the shortest
def shortestPartialDuplicateLink(links):
    linksPerNetloc = {}

    for link in links:
        nl = urlsplit(link).netloc

        if nl not in linksPerNetloc:
            linksPerNetloc[nl] = []

        linksPerNetloc[nl].append(link)

    shortestLinks = []
    for key in linksPerNetloc:
        linksPerNetloc[key].sort(key=len)
        shortestLinks.append(linksPerNetloc[key][0])

    return shortestLinks


# read existing file
updateTextInFileVar()

postsToScan = []

# get posts
RedditPosts = bot.subreddit('opendirectories').new(limit=postsToLoad)


# add custom links content to posts
for link in pagesToCheckForLinks:
    postsToScan.append(requests.get(link).text)
    print("loaded 1000 posts from pushshift")

for post in RedditPosts:
    # postsToScan.append(post)
    pass

# search for links in each post
for post in postsToScan:

    try:
        text = post.selftext
    except:
        text = post

    try:
        text += " " + post.url
    except:
        pass

    posts.append(text)

    urls = re.findall(URL_REGEX, text)

    print(len(posts), "posts read. Found", len(urls), "links in this one")
    # print(urls)

    blackListed = False

    for url in urls:
        # don't add links that contain blacklist terms
        for term in blackList:
            if term.lower() in url.lower():
                print(term, "found in ", url)
                blackListed = True
                break
            else:
                blackListed = False

        if not url.endswith("/"):
            url += "/"

        nl = urlsplit(url).netloc

        if url not in foundLinks and not blackListed and nl not in textInFile:
            foundLinks.append(url)
            print("adding", url)
        else:
            # print("not adding", url)
            pass

print("foundlinks", foundLinks)

# start checking threads for each url
for url in foundLinks:
    while threads >= maxThreads:
        print(threads, "threads already running. Waiting...")
        time.sleep(1)

    if url not in textInFile and url not in newLinks:
        threading.Thread(target=checkDirectory, args=(url,)).start()
        threads += 1
        print("started new thread", threads, "threads running. ", len(workingLinks), "working directories found")
    else:
        print(url, "is already in the file")

# wait for threads to finish
while threads > 0:
    try:
        time.sleep(1)
        print("Waiting for {} threads to finish. ctrl+c to stop".format(threads))
    except KeyboardInterrupt:
        print("keyboard interrupt")
        break

# read links that have been added to the file
file = open("opendirectories.txt", "r")
urls = file.read().split("\n")
file.close()

# keep only the shortest link of each web server
urls = (shortestPartialDuplicateLink(urls))

# sort list on (sub) domain
urls.sort(key=domain)

# write sorted links to file
file = open("opendirectories.txt", "w+")
for url in urls:
    if len(url) > 5:
        file.write(url + "\n")
file.close()

print("Got {} working directories with links from {} posts with {} links".format(len(workingLinks), len(posts),
                                                                                 len(foundLinks)))
input("\nCOMPLETED\n")