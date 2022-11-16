<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/115161827/202196829-fc71bc02-73b0-40a4-a02a-1e1ac9cad13e.jpg"/>  

# Insert YouTube logo

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a> •
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/import-images)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/import-images)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/import-images.png)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/import-images.png)](https://supervise.ly)

</div>

# Overview

App iterates over all images in directory (in Team Files) and creates new images with YouTube button in the center alongside. App is useful for developers who prepare screenshots and videos for `README.md` files.

Typical use case is the following: you have a video on youtube, and you would like to add it to readme and make it clearly visible in both Supervisely Ecosystem and github page. Currently GitHub does not support youtube player embedding, but it is possible to insert clickable image to readme

This app supports any widely used image format, and is not tied to any aspect ratio or resolution.

# How to Run

1. Go to Team Files

<img src="https://user-images.githubusercontent.com/115161827/202218609-485003e6-e295-4d3b-9bd5-fa302e43eea2.png">

2. Create an empty directory
<img src="https://user-images.githubusercontent.com/115161827/202220220-ff76d5d4-20b1-40ac-a0b3-8e2416131c4e.gif">

3. Upload images into new directory using drag-and-drop
  <img src="https://user-images.githubusercontent.com/115161827/202231709-a964351f-390f-41be-a685-4489d9845c33.gif">

4. Right click to directory and run the app from the context menu
<img src="https://user-images.githubusercontent.com/115161827/202220693-788ba804-6fc5-4ddd-87b3-494f459374d9.png">


## Result

As a result of running this app, images with youtube button will be created in the same directory with modified names (`_youtube` will be added to the file names)

<img src="https://user-images.githubusercontent.com/48913536/178972113-4d53f0dc-6323-4721-9ec2-f09de16ad0bc.png" width="80%" style='padding-top: 10px'>

Then you can add the following code snippet to your README (do not forget to replace links in example):

```
<a data-key="sly-embeded-video-link" href="https://youtu.be/e47rWdgK-_M" data-video-code="e47rWdgK-_M">
    <img src="https://i.imgur.com/sJdEEkN.png" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;">
</a>
```

Once you added it to your readme, it will be shown nicely in both Supervisely platform and GitHub.


In Supervisely  |  In GitHub
:-------------------------:|:-----------------------------------:
<img src="https://user-images.githubusercontent.com/115161827/202243190-fe28997c-2c70-46dd-9f15-9122b4ce9ad4.png" style="max-height: 300px; width: auto;"/>  |  <img src="https://user-images.githubusercontent.com/115161827/202243009-3e17cd2a-08ef-4636-9ed0-109b662dfe63.png" style="max-height: 300px; width: auto;"/>