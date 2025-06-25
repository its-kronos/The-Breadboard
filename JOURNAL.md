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

