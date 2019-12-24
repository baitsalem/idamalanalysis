
import httplib

def _getOnlineMsdnContent(keyword):
        """
        This functions downloads content from the MSDN website. It does not return the
        information instantly but provides it through a callback that can be registered
        with the function I{registerDataReceiver}.
        @param keyword: the keyword to look up in MSDN
        @type keyword: str
        @return: (str) a waiting message if the keyword has been queried or a negative answer if
            there are no entries in MSDN
        """
        feed_url = "https://social.msdn.microsoft.com/search/en-US/feed?format=RSS&query=%s" % keyword
        feed_content = download(feed_url)
        if not feed_content:
            return "<p>Could not access the MSDN feed. Check your Internet connection.</p>"
        msdn_url = _getFirstMsdnLink(feed_content)
        
        if msdn_url != "":
            #print("Download : {}".format(msdn_url))
            return _cleanupDownloadedHtml(download(msdn_url))
            # FIXME: should threading in IDA ever work, use this...
            # self.downloader.setDownloadUrl(msdn_url)
            # self.downloader.downloadStoredUrl
            # self.ida_proxy.execute_sync(self.downloader.downloadStoredUrl, self.ida_proxy.MFF_FAST)
            # return "<p>Fetching information from online MSDN, please wait...</p>"
        else:
            return "<p>Even MSDN can't help you on this one.</p>"

def _getFirstMsdnLink(feed_content):
        """
        Parses the first MSDN URL from a RSS feed.
        @param feed_content: a rss feed output
        @type feed_content: str
        @return: (str) the first MSDN url if existing.
        """
        while feed_content.find("<link>") > -1:
            start_index = feed_content.find("<link>")
            end_index = feed_content.find("</link>")
            link_url = feed_content[len("<link>") + start_index:end_index]
            #print(link_url)            
            if "docs.microsoft.com" in link_url:
                return link_url
            else:
                feed_content = feed_content[feed_content.find("</link>") + 7:]
            return ""



def download(url):
        """
        Start a blocking download. Will return the downloaded content when done.
        @param url: The URL to download from.
        @type url: str
        @return: (str) the downloaded content.
        """
        # print "Downloader.download(): type of received parameter: ", type(url)
        host = url[8:url.find("/", 8)]
        path = url[url.find("/", 8):]
        try:
            conn = httplib.HTTPSConnection(host)
            conn.request("GET", path)
            response = conn.getresponse()
            if response.status == 200:
                print "[+] Downloaded from: %s" % (url)
                _data = response.read()
            else:
                print "[-] Download failed: %s (%s %s)" % (url, response.status, response.reason)
                _data = "Download failed (%s %s)!" % (response.status, response.reason)
            conn.close()
        except Exception as exc:
            print ("[!] Downloader.download: Exception while downloading: %s" % exc)
            _data = None
        return _data



def _cleanupDownloadedHtml(content):
        content = content[content.find("<div class=\"hasSideBar\"")] #:content.find("<div id=\"contentFeedback\"")]
        print(content)
        #content = "".join(s for s in content if s in self.string.printable)
        return content



_getOnlineMsdnContent("getfiletype");

