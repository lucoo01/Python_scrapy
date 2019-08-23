# -*- coding: utf-8 -*-


class Common:

    def readlist(self):
        f = open('urllist.txt', 'r', encoding="utf-8")
        urls = f.readlines()
        f.close()

        allurls = [item.strip() for item in urls]

        return allurls
    





