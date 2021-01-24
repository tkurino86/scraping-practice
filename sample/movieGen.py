import requests
from bs4 import BeautifulSoup
import time
import re
import sys
import os
import cv2 #動画編集ライブラリ　https://www.tech-teacher.jp/blog/python-opencv/
import glob
import numpy as np
frame_rate = 0.7  #FPS 秒間に使用するフレーム数（コマ数）の静止画が記録されているかという数値
width = 1920
height = 1080

def main():
    argv = sys.argv
    if(len(argv)<2):
        print("python3 main.py $名前$\n と入力してね")
        return
    name = sys.argv[1]
    path = './pic/'+name  #生成先パス+フォルダ名
    if not os.path.isdir(path):
        os.makedirs(path)
        c = 0
        for i in range(100):
            urlName = "https://prcm.jp/list/"+name+"?page={}".format(i+1)
            url = requests.get(urlName)
            soup = BeautifulSoup(url.content, "html.parser")
#img_list = soup.select('div.entry > ul > li > a > div > img') selector into DOM
            img_list = soup.select('div>ul>li>a>div>img')
            for img in img_list:
                img_url = (img.attrs['src'])
                img_url = re.sub('_.*jpeg','.jpeg',img_url)
                img_url = re.sub('_.*png','.png',img_url)
                print(img_url)
                download_img(img_url,path+'/img{}.png'.format(c))
                c+=1
# making movie
    movie_path = './video/'
    if not os.path.isdir(movie_path):
        os.makedirs(movie_path)
        images = sorted(glob.glob(path+"/*.png"))
        timelaps(images,movie_path+name)

def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)
def timelaps(images,path):
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    video = cv2.VideoWriter(path+'.mp4', fourcc, frame_rate, (width, height))
    print("動画変換中...")
    for image in images:
        print(image)
        img = cv2.imread(image)
        dst_img = np.zeros((height, width, 3), dtype = np.uint8)
        top = 0
        left = 0
        h, w, c = img.shape
        if(height/h<width/w):
            img=cv2.resize(img,(height*w//h,height))
        else:
            img=cv2.resize(img,(width,h*width//w))
        print(img.shape)
        h, w, c = img.shape
        dst_img[0:h, 0:w] = img
        video.write(dst_img)
    video.release()
    print("動画変換完了")
    
if __name__ == '__main__':
    main()
