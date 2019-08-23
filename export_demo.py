import os
import re
import shutil
import sys


def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def replace_file_conent(filepath, source, target):
    # 替换内容
    f = open(filepath, "r", encoding='UTF-8')
    alllines = f.readlines()
    f.close()

    f = open(filepath, "w+", encoding='UTF-8')
    for eachline in alllines:
        a = re.sub(source, target, eachline)
        f.writelines(a)

    f.close()

    return True

pname=input("请输入你的项目名:")

while is_contain_chinese(pname):
    print("项目名中不能包含中文, 只能是英文,请重新输入项目名:")
    pname = input("请输入你的项目名:")
    
if os.path.exists(pname):

    print('改项目已经存在!')
    sys.exit(0)

shutil.copytree("s_demo", pname) # 复制一份项目出来

shutil.move(pname+"/gitchat", pname+"/"+pname) # 重命名项目

shutil.move(pname+"/"+pname+"/spiders/gitbook.py", pname +
            "/"+pname+"/spiders/"+pname+".py")  # 重命名文件


# 替换内容
replace_file_conent(pname+"/scrapy.cfg", 'gitchat', pname)
replace_file_conent(pname+"/"+pname+"/settings.py", 'gitchat', pname)

cap_pname = pname.capitalize()
replace_file_conent(pname+"/"+pname+"/settings.py",
                    'GitchatPipeline', cap_pname+'Pipeline')

replace_file_conent(pname+"/"+pname+"/pipelines.py",
                    'GitchatPipeline', cap_pname+'Pipeline')

replace_file_conent(pname+"/"+pname+"/pipelines.py",
                    'gitchat', pname)

replace_file_conent(pname+"/"+pname+"/items.py",
                    'GitchatItem', cap_pname+'Item')

replace_file_conent(pname+"/"+pname+"/middlewares.py",
                    'GitchatSpiderMiddleware', cap_pname+'SpiderMiddleware')


replace_file_conent(pname+"/"+pname+"/conf/mongo_config.py",
                    'gitbook', pname)

replace_file_conent(pname +
                    "/"+pname+"/spiders/"+pname+".py",
                    'GitbookSpider', cap_pname+'Spider')

replace_file_conent(pname+"/"+pname+"/spiders/"+pname+".py", 'gitbook', pname)


print('转换成功', pname+"/"+pname+"/spiders/"+pname+".py")
