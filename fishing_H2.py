from imagesearch_2 import *

import os, sys, stat

# 引入 configparser 模組
import configparser


# 建立 ConfigParser
config = configparser.ConfigParser()

# 讀取 INI 設定檔
config.read('config.ini')

imgSeconds = float(config['setting']['ImgSeconds'])

KeySeconds1 = float(config['setting']['KeySeconds1'])
KeySeconds2 = float(config['setting']['KeySeconds2'])

StartFish = config['Key']['StartFish']

#targetPic = "FishImg.png"
targetPic = config['Game']['FishImg']
WindowsName= config['Game']['Name']

#imgSeconds = 
# Search for the github logo on the whole screen
# note that the search only works on your primary screen.

# search for the github logo continuously :
def matchPic_hwnd(hwnd):
    pos = imagesearch_hwnd_loop(targetPic, hwnd, imgSeconds)
    print("image found ", pos[0], pos[1])


if __name__ == "__main__":
    hwnd = FindWindow_bySearch(WindowsName)


# VK_Key_Code : http://www.kbdedit.com/manual/low_level_vk_list.html
    VK_KEY_F = 0x46
    
    VK_KEY_F1 = 0x70
    VK_KEY_5 = 0x35
    VK_KEY_6 = 0x36
    VK_KEY_7 = 0x37
    VK_KEY_8 = 0x38
    if StartFish=="F1":
        c = VK_KEY_F1
    if StartFish=="5":
        c = VK_KEY_5
    if StartFish=="6":
        c = VK_KEY_6
    if StartFish=="7":
        c = VK_KEY_7
    if StartFish=="8":
        c = VK_KEY_8

    ##VK_KEY_5 = StartFish
    #VK_KEY_F = UPFish
   
    while 1:
        matchPic_hwnd(hwnd)
        win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, VK_KEY_F , 0)
        time.sleep(KeySeconds1)
        win32gui.PostMessage(hwnd, win32con.WM_KEYUP, VK_KEY_F , 0)
        time.sleep(KeySeconds2)
        win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, c , 0)
        time.sleep(KeySeconds1) 
        win32gui.PostMessage(hwnd, win32con.WM_KEYUP, c , 0)

