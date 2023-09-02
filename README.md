# python-course-player

Hi everybody !

This program is designed to help you manage your tutorial viewing history. In today's rapidly evolving industry, learning something new every day is essential to stay competitive. However, keeping track of the last video you watched in a specific tutorial can be challenging. This program simplifies the process by allowing you to save your video-watching history, so you can focus on your tutorials without worrying about losing your place.

## Installation 

Before you get started, ensure that you have Python 3 installed on your computer. You can download and install Python from the official website by visiting the following link:

```shell
https://www.python.org/downloads/
```

### Once Python is installed, follow these steps to set up the program:

1 . Clone the repository from GitHub by running the following command in your terminal:

```shell
git clone https://github.com/sajjadabd/python-course-player.git
```

2 . To ensure you have the latest version of pip on your local machine, upgrade it by running the following command:
	
```shell
python.exe -m pip install --upgrade pip
```

3 . Install the necessary packages by running:

```shell
pip install -r requirements.txt
```


## Running the program 

This program supports video playback with various media players, including VLC media player, GOM Player, PotPlayer, mpv Player, and KMPlayer. You'll need to download and install the media player of your choice to open videos within the program. Here are the download links for each player:

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

After installing your preferred media player, make sure to add the player's location to your system's PATH environment variable. Here's how to do it on Windows:


* Right-click on "This PC" (or "My Computer") and select "Properties"
* go to "Advanced System Settings"
* Go to the "Advanced" tab
* Click "Environment Variables…"
* Look for "Path" in the "System variables" section, select it, and click "Edit"

For Windows 7:

* Add a semicolon (;) to the end of the variable and append the location of your video player. Click "OK" and apply the changes to every open window.

For Windows 10:

* Click "New" 
* Enter the path to the folder containing the video player
* Click "OK" to save the changes to your variables.

Once you've added the location to your system's PATH, place the `app.pyw` file wherever you prefer on your computer. To run the program, simply double-click `app.pyw` Enjoy your uninterrupted tutorial viewing experience!
