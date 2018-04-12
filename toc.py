#!/usr/bin/env python3
#coding=utf-8

import os
import argparse

links = []

def toc(path):
    items = os.listdir(path)
    for item in sorted(items):
        link = f"- [{os.path.splitext(item)[0]}](#!{os.path.join(path,item)})\n"
        links.append(link)
        item = os.path.join(path, item)
        if os.path.isdir(item):
            links.pop()
            links.append(f"\n**{os.path.basename(item)}**\n\n".title())
            toc(item)

def gen_toc(path):
    toc(path)
    nav = f"nav-{path}.md"
    if os.path.exists(nav):
        os.unlink(nav)
    with open(nav,'a') as f:
        f.write(f'# {path}\n\n'.title())
        for link in links:
            f.write(link)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a TOC of the certain path')
    parser.add_argument('path', metavar='PATH', type=str,
                        help='directory path name')
    args = parser.parse_args()
    gen_toc(args.path)
