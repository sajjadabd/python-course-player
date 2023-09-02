# python-course-player

Hi everybody , this program helping you to manage the history of tutorials you have been watched

nowadays each of us should learn something new everyday to compete in the fast growing industry

but it would be hard to manage what was your last video you watched in the special tutorial 

this program helps you to save the history of watching videos and you just focused on watching tutorials 

## Installation 

first of all you should have python3 installed on your computer , you can download and install python from the official python website : 

```shell
https://www.python.org/downloads/
```

after installing python you should just clone the repository from github :

```shell
https://github.com/sajjadabd/python-course-player.git
```

you can upgrade your pip to make sure that you have the latest version on your local machine :

```shell
python.exe -m pip install --upgrade pip
```

and now you can install the neccessary packages :

```shell
pip install -r requirements.txt
```


## Running the program 

This program can play videos with `VLC media player` , `GOM Player` , `PotPlayer` , `mpv Player` and `KMPlayer`

you should download and install the media player you want to open videos within your program , these links can help you download the right media player you need 

VLC media player :

```
https://www.videolan.org/vlc/
```

GOM Player :

```shell
https://www.gomlab.com/gomplayer-media-player/
```

PotPlayer :

```shell
https://potplayer.daum.net/
```

mpv Player :

```shell
https://mpv.io/
```

KMPlayer :

```shell
https://www.filehorse.com/download-kmplayer-64/
```

after installing your favorite media player make sure to add the location of your video player to path

in Windows to add the location of your application to the path do like this :


* Right click on This PC (My Comptuer) and go to Properties 
* go to Advanced System Settings 
* Go to the "Advanced" tab
* Click "Environment Variables…"
* look for "path" in System variables and select it and Click Edit

in Windows 7 :

* add semicolon (;) to end of the variable and add your video player location and click OK and Apply to every window you open

in Windows 10 :

* Click "New"
* Enter the path to the folder containing the video player 
* Click "OK" to save the changes to your variables


put `app.pyw` in place you want in your computer and you can double click the program to run 
