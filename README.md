# SitemapCreator - a web page scraper in Python

## About
SitemapCreator is a Python tool to scrape a domain for all active links that points to the same domain. All URLs are written to a sitemap file, which in turn is ready to be uploaded to Google for faster indexing of the domain.

## Usage
Clone the repository:

    $ git clone https://github.com/WelcomWeb/SitemapCreator.git

Run SitemapCreator and write all domain-local URLs of `http://www.MyDomain.com` to a file called `MySitemap.txt`:

    $ cd SitemapCreator
    $ python sitemap.creator.py http://www.mydomain.com MySitemap.txt

## Argument list

    sitemap.creator.py <HOST> <FILENAME> [TIMEOUT=False] [VERBOSE=False]

### The optional arguments
Some servers are configured to block a high amount of hits from one and the same IP (to prevent DoS attacks), so by sending SitemapCreator a timeout value we can delay each request to prevent the tool from being blocked by the server. The specified timeout should be in seconds, so with the following parameters SitemapCreator delays each request by 0.5 seconds (500ms):

    $ python sitemap.creator.py http://www.mydomain.com MySitemap.txt 0.5

By default SitemapCreator is silent, and doesn't tell you what it's doing - but by adding a parameter we can tell it to be verbose;

    $ python sitemap.creator.py http://www.mydomain.com MySitemap.txt 0.5 true

[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/c9c9680aafd0e7cd4f3f763b50e5b691 "githalytics.com")](http://githalytics.com/WelcomWeb/SitemapCreator)
