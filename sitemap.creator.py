#!/usr/bin/python
# -*- coding: UTF-8

"""
Author: Björn Wikström <bjorn@welcom.se>
Copyright 2013 Welcom Web i Göteborg AB

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import re
import sys
import urllib2
import time
from urlparse import urlparse

class Outputter:
	""" Outputter handles the writing of the sitemap, to a specified file """
	def __init__(self, filename):
		path = []
		path.append(os.getcwd())
		path.append(filename)
		
		self.handle = open(os.sep.join(path), 'w')

	def put(self, line):
		print >> self.handle, line

class Sitemap:
	""" Parses, reads and stores all anchor links to pages for the same domain as
		the entry point """
	def __init__(self, entry, outputter, timeout = False, verbose = False):
		self.entry = entry
		self.paths = [entry]
		self.output = outputter
		self.timeout = timeout
		self.verbose = verbose

		if self.verbose:
			print "Entry point: ", entry

	def start(self):
		self.find_next_path()

	def find_next_path(self):
		current = 0

		while True:
			if not self.timeout == False:
				time.sleep(float(self.timeout))

			self.read_path(self.paths[current])
			current = current + 1

			if current >= len(self.paths):
				break

	def read_path(self, path):
		try:
			page = urllib2.urlopen(path)

			if not page.getcode() == 200:
				return
			if self.verbose:
				print path, "200 OK. Reading..."

			self.output.put(path)

			content = page.read()
			page.close()

			if len(content) > 0:
				self.parse(content, path)

		except:
			if self.verbose:
				print path, "Error occurred. Skipping."

	def parse(self, content, path):
		matches = re.findall(r"<a.*?href=[\"|']([^ ]+)[\"|']", content)

		for match in matches:
			parsed = urlparse(match)

			if parsed.scheme == "":
				if match[0] == '?':
					continue
				
				parsed = urlparse(self.entry + match)

			if not parsed.scheme in ["http", "https", "shttp"]:
				continue
			
			current = urlparse(path)

			host = parsed.netloc
			if parsed.netloc == "":
				host = current.netloc

			if (host == current.netloc) and not parsed.geturl().rstrip('/') in self.paths:
				self.paths.append(parsed.geturl().rstrip('/'))

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "Usage: python sitemap.creator.py <HOST> <FILENAME> [TIMEOUT] [VERBOSE]"
	else:
		output = Outputter(sys.argv[2])

		timeout = False
		verbose = False

		if len(sys.argv) > 3 and not sys.argv[3].lower() == "false":
			timeout = sys.argv[3]
		if len(sys.argv) > 4 and sys.argv[4].lower() == "true":
			verbose = True

		creator = Sitemap(sys.argv[1], output, timeout, verbose)
		creator.start()
