@echo off
setlocal enabledelayedexpansion
set file=D:\gitchat\s_demo\scrapy.cfg
set file_tmp=D:\gitchat\s_demo\scrapy_tmp.cfg
set file_bak=D:\gitchat\s_demo\scrapy_bak.cfg
set source1=gitchat

set /p replaced1=please input your projectname:

for /f "delims=" %%i in (%file%) do (
    set str=%%i
        set "str=!str:%source1%=%replaced1%!"
        echo !str!>>%file_tmp%
)
copy "%file%" "%file_bak%" >nul 2>nul
move "%file_tmp%" "%file%"



set file=D:\gitchat\s_demo\gitchat\settings.py
set file_tmp=D:\gitchat\s_demo\gitchat\settings_tmp.cfg
set file_bak=D:\gitchat\s_demo\gitchat\settings_bak.cfg
set source1=gitchat

set /p replaced1=please input your projectname:

for /f "delims=" %%i in (%file%) do (
    set str=%%i
        set "str=!str:%source1%=%replaced1%!"
        echo !str!>>%file_tmp%
)
copy "%file%" "%file_bak%" >nul 2>nul
move "%file_tmp%" "%file%"
pause