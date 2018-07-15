## 8-bit Pixel Art Display Project

#### Required components


- A microSD card
- A microSD card reader (some computers have these built in, but if not I use something like [this](https://www.amazon.com/IOGEAR-MicroSD-Reader-Writer-GFR204SD/dp/B0046TJG1U/ref=sr_1_9?ie=UTF8&qid=1531610754&sr=8-9&keywords=microSd+card+reader)).

http://www.thealmightyguru.com/Games/Hacking/Wiki/index.php/NES_Palette






1. **Download [Raspbian](https://www.raspberrypi.org/downloads/raspbian/), the Raspberry Pi operating system**. 

	A direct link to the latest stable 'lite' build can be found [here](https://downloads.raspberrypi.org/raspbian_lite_latest).

2. **Put the image on a microSD card**. 
		
	Basically, this involves creating a bootable microSD card from the Raspbian image downloaded above. As an OS X user, my preferred method for doing this is using [ApplePi-Baker](https://www.tweaking4all.com/software/macosx-software/macosx-apple-pi-baker/). Follow the link to see instructions on its use, but basically you'll select the microSD card from the menu, choose the IMG file in the 'Pi-Ingredients: IMG Recipe' box, and click on 'Restore Backup'. 
	
	I used version 1.9.4 of ApplePi-Baker, which can be downloaded directly [here](https://www.tweaking4all.com/?wpfb_dl=94).

3. Set up the Raspberry Pi
	
	Make sure that the Raspberry Pi isn't plugged in. Pop in the microSD card,  then make sure that the unit is connected via HDMI to a monitor and connected via USB to a keyboard. Plug the Power cable to the 5V plug on the HAT and allow the unit to boot to the login. The default username is `pi` and the password is `raspberry`. This should get you to the linux command line.
	
	
	The first step is to run the following command, which will bring up the Raspberry Pi configuration menu:
	
	`sudo raspi-config`
	
	1. Unless you are in Great Britain at which point you can skip this step, via the arrow keys and enter, navigate to `4 Localisation Options` (as you change each option you'll be dropped back into the top-level menu, so navigate back to the sub-menu).

		Select `I1 Change Locale`, and choose your local via the spacebar, confirming with enter (for the US that would be `en_US.UTF-8 UTF-8`. Confirm that you want this as the default for the system environment.
		
		Select `I2 Change Timezone` and select your region then timezone.
		
		Select `I3 `. If you're in the US, you'll most likely want to pick `Generic 104-key PC` > `other` > `English (US)` > `English (US)` > `The default for the keyboard layout` > `No compose key`
		
	2. Navigate to `7 Advanced Options` and select `A2 Overscan` > `No` > `Ok`. (This makes the display fill the entire screen).

	3. Set up wi-fi by selecting `2 Network Options` > `N2 Wi-fi` and following the instructions. You'll also want to set up the Pi's SSH server so that you'll be able to log into the Raspberry Pi from another PC (such that the Pi doesn't have to be connected to a display or keyboard) by navigating to `5 Interfacing Options` and selecting `P2 SSH` > `Yes` > `Ok`.

	4. Navigate to `Finish` then type `sudo reboot` to reboot the Raspberry Pi. Login as before.


		
		
		
		
		
		 	 
	
	

 