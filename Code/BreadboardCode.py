# first install circuit python please!

import board
import usb_cdc
import busio as bus
import digitalio as IO
import time

usb_cdc.enable(console = True, data = True)

usb = usb_cdc.data
uart = bus.UART(tx=board.D2, rx=board.D1, baudrate=115200)

#setting up pins used for bootloader
IO2 = IO.DigitalInOut(board.D0)
IO8 = IO.DigitalInOut(board.D4)
IO9 = IO.DigitalInOut(board.D5)
EN = IO.DigitalInOut(board.D3)

IO2.direction = IO.Direction.OUTPUT
IO8.direction = IO.Direction.OUTPUT
IO9.direction = IO.Direction.OUTPUT
EN.direction = IO.Direction.OUTPUT

#setting bootloader mode to UART and resetting MCU
IO2.value = True
IO8.value = True
IO9.value = False

EN.value = False
EN.value = True

while True:
    if usb.in_waiting>0:
        data = usb.read(usb.in_waiting)
        uart.write(data)


    if uart.in_waiting>0:
        data = uart.read(uart.in_waiting)
        usb.write(data)