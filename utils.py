
def match_url(urls, path):
  
  for url in urls:
    if url[0] == path:  # use regex here
      return url[1]
