#!/usr/bin/env python3
# 为未整理的文件记录链接便于查看

import os, send2trash
	
def generate_toc(foldername):
	dir = './{}'.format(foldername)
	toc = 'nav-{}.md'.format(foldername)
	send2trash.send2trash(data)
	for folderName, subfolders, filenames in os.walk(dir):
		for filename in filenames:
		    url = '#!{0}/{1}'.format(foldername, filename)
		    link = '- [{0}]({1})\n'.format(filename, url)
		    file = open(toc, 'a')
		    file.write(link)
	file.close()
	
generate_toc('notes')
generate_toc('linux')
generate_toc('others')
generate_toc('front-end')
