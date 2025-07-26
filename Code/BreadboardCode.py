# first install circuit python please!
BOOTLOADER = True


import board
import usb_cdc
import adafruit_pio_uart as bus
import digitalio as IO
import time

usb = usb_cdc.data
uart = bus.UART(tx=board.GP2, rx=board.GP1, baudrate=9600)

#setting up pins used for bootloader
IO2 = IO.DigitalInOut(board.GP0)
IO8 = IO.DigitalInOut(board.GP4)
IO9 = IO.DigitalInOut(board.GP5)
EN = IO.DigitalInOut(board.GP3)

IO2.direction = IO.Direction.OUTPUT
IO8.direction = IO.Direction.OUTPUT
IO9.direction = IO.Direction.OUTPUT
EN.direction = IO.Direction.OUTPUT

#setting bootloader mode to UART and resetting MCU

if BOOTLOADER:
    IO2.value = True
    IO8.value = True
    IO9.value = False

    EN.value = False
    time.sleep(0.05)
    EN.value = True
    time.sleep(0.05)


print("Communication started!")
while True:
    if usb.in_waiting>0:
        #print("USB data found")
        data = usb.read(usb.in_waiting)
        #print(data)
        #print("\n")
        uart.write(data)


    if uart.in_waiting>0:
        #print("UART data found")
        data = uart.read(uart.in_waiting)
        #print(data)
        #print("\n")
        usb.write(data)
