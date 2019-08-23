# -*- coding: utf-8 -*-
import re
import time
import hashlib

from bs4 import BeautifulSoup

class BsExtend:

    # 解析图片, 并替换图片链接
    def parse_img(self, content, response):
        # 生成soup对象
        soup = BeautifulSoup(content, 'lxml')

        imgs = []

        for img in soup.find_all('img'):
            src = img.get('src')
            src = response.urljoin(src)
            # 加上协议头部
            if src.find('https:') == -1 and src.find('http:') == -1 and src.find('//') == 0:
                src = 'https:'+src

            dirname = time.strftime('%Y%m%d%M', time.localtime())

            imgname = src.split('/')[-1];
            ext = imgname.split('.')[-1];

            if ext:
                pass
            else:
                ext = 'jpg'
            
            
            tarname = hashlib.md5(imgname.encode(encoding='UTF-8')).hexdigest()
            tarname += ".{ext}".format(ext=ext) # 补上文件类型
            
            # 要用中括号 不要用点语法
            img["src"] = '/attachments/{dirname}/{tarname}'.format(dirname=dirname, tarname=tarname)

            imgs.append({
                'src': src,
                'dirname':dirname,
                'tarname':tarname
            })

        return {
            'imgs': imgs,
            'content': str(soup)
        }
    
    # 替换链接, 收集链接, 替换关键词
    def parse_content(self, content, host='runoob.com', curlink=None):
        # 生成soup对象
        soup = BeautifulSoup(content, 'lxml')

        pname = ''

        #本地链接
        if curlink:
            curlink = curlink.replace('https:','')
            curlink = curlink.replace('http:','')
            curlink = curlink.replace('//www.'+host+'/','')
            curlink = curlink.replace('//'+host+'/','')

            pname = curlink.split('/')[0]

        links = []
        locallinks = []
        innerlinks = []
        tryrunlinks = []
        otherlinks = []

        for link in soup.find_all('a'):
            href = link.get('href')
            if href is None:
                continue

            if href.find('//') == 0:
                href = 'https:'+href

            if href.find('https:') >= 0 or href.find('http:') >= 0:
                
                if href.find(host) >= 0:
                    
                    href = href.replace('https:','')
                    href = href.replace('http:','')
                    href = href.replace('//www.'+host,'')
                    href = href.replace('//'+host,'')

                    #是不是当前手册的链接
                    if pname != '' and href.find('/'+pname+'/')>=0:
                        innerlinks.append(href)
                    elif href.find('/try/') >= 0:
                        tryrunlinks.append(href)
                    else:
                        locallinks.append(href)
        
                    link['href'] = href
                else:
                    otherlinks.append(href)
                    #其他网站的链接
            else:
                #本地链接
                if href.find("/") != 0:
                    href = "/"+pname+"/"+href

                #是不是当前手册的链接
                if pname != '' and href.find('/'+pname+'/')>=0:
                    innerlinks.append(href)
                elif href.find('/try/') >= 0:
                    tryrunlinks.append(href)
                else:
                    locallinks.append(href)
                #locallinks.append(href)
        # soup.prettify()
        return {
            'locallinks': locallinks,
            'innerlinks': innerlinks,
            'tryrunlinks': tryrunlinks,
            'otherlinks': otherlinks,
            'content': str(soup)
        }
    





