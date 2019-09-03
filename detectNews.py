# All the necessary information of news websites from the newsapi are stored here.
url = {
"BBC News": {"id" : "bbc-news", "url" : "bbc.co.uk", "headline_tag" : "story-body__h1", "headline_tag_2" : None, "content_tag" : "story-body__inner", "content_tag_2" : "p"},
"ABC News": {"id" : "abc-news", "url" : "abcnews.go.com", "headline_tag" : "article-header", "headline_tag_2" : "h1", "content_tag" : "article-copy", "content_tag_2" : "p"},
"The Wall Street Journal": {"id" : "the-wall-street-journal", "url" : "wsj.com", "headline_tag" : "bigTop__hed", "headline_tag_2" : None, "content_tag" : "wsj-snippet-body", "content_tag_2" : "p"}
}

# A module that detects which website the link sent by the user belongs.
# The parameter "link_user" is the link provided by user.
def sourceFinder(link_user):

	for i in list(url.keys()):
		if url[i]["url"] in link_user:
			return url[i]