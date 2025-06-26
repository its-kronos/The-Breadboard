# Journal

# Information
- Title: "The Breadboard"
- Author: An. D. (its_kronos)
- Description: Breadboard, but microcontroller (AKA custom devboard) *probably change later*
- Creation Date: 6/24/2025
- Total Time (before building): - 

# 6/24/2025

- Did a lot of unfocused researched, and also hopped in a huddle (voicechat) with @Cyao and asked a lot of questions about incorperating RF into a design
- Confirmed what exactly I wanted to build, which would be a devboard with the 2350B MCU for maximum GPIO and a routing challenge. I would also want to include WIFI connectivity like the PI Pico W, which would make it useful in projects that require things like API calls based on peripherals.

**Time: Untimed, especially since this research was unfocused**

# 6/25/2025

* did some research about the PI235x chips with the hardware guide
* downloaded footprint for RP2350B
* created schematic part for the VREG

![image](https://github.com/user-attachments/assets/2da23498-85c1-4c00-875b-4e9df5356662)


* made custom footprint for the inductor, which recommended a specific part to ensure correct coiling for minimal interferance

![image](https://github.com/user-attachments/assets/ef40a38a-5f6b-4a9a-96e1-944912b26bc9)


* sourced components needed for the VREG
* Made schematic for and sourced all parts needed for the USB connection, including parts like an LDO, which was pretty easy since this is the second time doing it for me

![image](https://github.com/user-attachments/assets/d1e8e4bb-9f0f-4053-9510-2f34f432481e)


* made the schematic for and sourced parts required for decoupling capacitors for the power pins

![image](https://github.com/user-attachments/assets/61debbe0-ebfb-4067-b006-c1bbf4b9f808)


* in the hardware guide for the rp235x series chips, it includes a resistor with value 0 ohms for the QSPI_SS pin, so I researched why there wasn't a direct connection and learned that it can be used as a "jumper wire" on a pcb

![image](https://github.com/user-attachments/assets/1b900ae6-95dd-4f24-a72c-8a1fba96c165)

* finished schematic for the flash memory for the chip

![image](https://github.com/user-attachments/assets/d81e52d5-0797-4207-80ed-3a545993abe8)


* finished schematic for the crystal

![image](https://github.com/user-attachments/assets/c8072dcb-63ff-4bae-b3fc-23d0c1280476)


- And here is the running component list (most of which are either basic or extended preferred parts, which took a bit of time to find, but nothing too serious)!

![image](https://github.com/user-attachments/assets/902b7856-4243-45de-bd03-334c5ceb2df2)


- overall this part of the schematic was pretty easy and didn't require too much challenge, and I believe that the main part of the challenge will come when actually routing the board

**TIME: 2h30m**

* I was done with the RP chip wiring from last session, so now the next logical step would be for me to wire the pin headers, but I was unable to decide which nets/GPIOs should go to which pin on the headers, but I did add a boot button to RUN and some more headers for debugging

![image](https://github.com/user-attachments/assets/944420b2-67c0-4f00-bf80-fd934d120c2c)

* I instead decided to try and add the RF/WIFI IC for the wifi support that I wanted to add, and I looked at the documentation for the CC2500 transceiver by TI, but this only led to me being increasingly confused and spending a lot of time pretty much getting nowhere
* My main question would be how the RP2350 chip would communicate with the CC2500 to control what packets of data or being sent out, or what mode the chip is in.


**time: 1h**

# 6/26/2025

* Using another MCU (the wroom c3) as a way to add wifi connectivity at the cost of 1 UART interface when being used
* decided to start routing the board so that I can know which pins are ideal to use for what purpose, so i assigned all the footprints

![image](https://github.com/user-attachments/assets/9298c907-adc1-4508-9a1d-cd949ea0405e)


* I had trouble routing because the pins were too close together, so I changed the main MCU to the RP2040 and double checked that everything was according to the different hardware guide

![image](https://github.com/user-attachments/assets/3628c8ea-95b3-43e8-b645-53cbb77f72dc)


* i had to replace a few of the parts of the schematics to fit with the RP2040, and then I reselected all the footprints and started routing

![image](https://github.com/user-attachments/assets/22a9316c-8716-49b5-8ddf-000d00cae4c3)


* here is the routing I have so far, and I tried my best to make sure that sensitive components would be out of the way from traces that would disrupt them, but what I did realize is that I need to find a new ESD protection IC since the current one would pretty much make it impossible to route
* It was pretty time consuming due to the numerous decoupling capacitors needed in many locations, and I might have to compromise on a few of them 


**Time: 2h**

