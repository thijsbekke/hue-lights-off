# Hue lights off
Do you have the same problem as me? You have your philips hue lights sync to your pc,
and when you shutdown your pc you have to manually switch of your lights? 

Well I had that "problem" to, that is why I created this simple Python script. When configures and added to your shutdown task your lights are turned off.

## Settings.yml

Maybe this step can be automated but for now: open _settings.yml_ and enter your 
- **username** and 
- **ip** 

of your bridge. 

See [https://developers.meethue.com](https://developers.meethue.com/develop/get-started-2/) on how to create an user and obtain those. 
You also need to specify which light (or zone/group) to turn off. 

The easiest way to know which light to turn off is to go the following url: 
- http://[ip of bridge]/debug/clip.html

In the url input field enter the following url 

```
/api/[apikey]
```

And now find the number of your group that you want to turn off.

Important, the format of your settings.yml has to be (notice the spaces before the values):

```
hue:
  username: XXXXXXXX
  ip: XXX.XXX.XXX.XXX
  light: X
```



## Requirements 

This script needs the following modules:
- requests
- PyYAML

```
pip install requests
pip install PyYAML
```

On Windows :

```
py -m pip install requests
py -m pip install PyYAML
```

## Installation

On Windows, to set up a script to run as soon as you shut down or logoff your computer do the following:


- open your Local Group Policy Editor by running ```gpedit.msc``` into the start menu or run dialog (Windows+R)
- Navigate to User Configuration - Windows Settings - Scripts (Logon/Logoff) - Logoff
- Click ```Add```
- Add an script and enter the following (for example, use your own paths here)
    - Scriptname: ```c:\python27\python.exe```
    - Script parameters: ```c:\Users\Thijs\PycharmProjects\hue-lights-off\app.py %*```


Now logoff or shutdown your pc and your lights will switch off
