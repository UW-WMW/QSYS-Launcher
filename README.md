# QSYS Designer Launcher

<!--
![screenshot](screenshots/screen2.PNG?raw=true)
 -->
 <p align="center">
  <img src="screenshots/screen2.PNG?raw=true" />
</p>

## Project Goals:

In addition to the functions of the well-known QSC-QSYS Launcher, it has the following features

- it shows not only the Designer versions from "PROGRAMFILES", but also from "PROGRAMFILES(x86)" (32 bit version below V.6.0)

- it lists the files in the correct numerical order (9.10 comes after 9.9 instead of 9.1)

- When launched with a *.qsys file as a parameter, it will display the version the file was created with to help you decide which Designer version to open.

- I have removed the function to also display a link to the UCI viewer and the the Administrator, because I very rarely need this

## Instructions

- [Download the latest release from GitHub](https://github.com/UW-WMW/QSYS-Launcher/releases)

- To use the application simply save the "QSYS-Launcher.exe" to the location of your choice. (This is considered a portable installation)

- Right click on a ".qsys" file and select open with.

- Navigate to the location of your "QSYS-Launcher.exe" and select it. Make sure to check "Always Open With" to allow the qsys files to open with the launcher every time.

- To open any file from that point simply double click the file and it will prompt you to select which version of Q-Sys Designer to use from your installed versions.

| :exclamation:  important:   |
|-----------------------------------------|
- If you install a new version of QSYS Designer, you may need to repeat the ‘Open with’ process because the installer will link the *.qsys files to the latest version of Designer again.

- If you decide to compile your own - I used auto-py-to-exe for this. (you may need to adjust the path to the icon file as auto-py-to-exe does not like relative paths)

## Thanks to:

Zach Lisko (mckay115).

His [QSC-QSYS Launcher](https://github.com/mckay115/QSC-QSYS-Launcher) was the first tool I used.

At first I wanted to make a fork to improve it a bit, but then I realised that the "PySimpleGUI" library

that he used is no longer free for commercial use, but costs $99.

So I decided to rewrite the tool from scratch.
