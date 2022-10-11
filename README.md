# WOTV multiquests autoclicker

Simple autoclicker for WOTV multi quests, including scripts for guests, hosting with 0 to 4 guests and hosting with at least one guest - Made in Python  


---  
<br>

Platforms:
* **Android** for the platform running the game (Either on an android device or an android emulator that supports adb)

* **Windows, Linux** and probably **macOS** (Tested on Manjaro linux only)  

<br>

## Usage instructions:
All files must be on the same folder  
* Insert into the `variables.yml` or `varcel.yml` files the coordinates of the buttons described in the files, you can use either one or both if you use more than one device (I might provide a visual guide in the future)
* Connect to the device running the game using adb (this is outside the scope of this guide, my recommended resource is: https://manpages.ubuntu.com/manpages/bionic/man1/adb.1.html)
* **MUST** be connected to only one device - check using the following command on a terminal (Future versions may include the option to choose which device (connected via adb) to run the script on) :  
```$ adb devices```  
* On a terminal, navigate to the folder the script is in and run:  
```$ ./WOTVscriptchooser.py```
* When prompted, choose `Emulator`, if you input the coordinates on the file `variables.yml` ou `Cellphone`, if you input the coordinates into the file `varcel.yml`

The three scripts MultiGuest.sh, MultiHostLT4.sh and MultiHostSolo.sh can also be used by themselves, on a terminal.  
The syntax for usage is,:  

```$ ./MultiGuest.py <platform>```  
```$ ./MultiHostSolo.py <platform>```  
```$ ./MultiHostLT4.py <platform>```  

Where the platform is either:
* `emu`, if you input the coordinates into the file `variables.yml` or
* `cel`, if you input the coordinates into the file `varcel.yml`

Delay between the clicks can be changed by modifying the `sleeptime` and `doubletime` variables in the `variables.yml` and `varcel.yml` files
