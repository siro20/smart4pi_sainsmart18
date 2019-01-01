## Sainsmart18 TFT on Raspberry Pi 3 using Smart4Pi

Here you can find systemd scripts and files to display the current
power readings of [smart4pi](https://shop.enerserve.eu/smartpi/)
on a [Sainsmart18](https://www.sainsmart.com/products/1-8-tft-spi-lcd-screen-with-microsd-socket)
TFT display.

## Connect the smart4pi power reading hardware
The smart4pi hardware connects over i2c using the connector that ships with the adapter board.

## Connecting the display
The Sainsmart18 TFT has to be connected over SPI.

    VCC -> 5V
    GND -> GND
    LED -> 3.3V
    CLK -> GPIO11 (SCLK)
    SDI -> GPIO10 (MOSI)
    RS -> GPIO 12
    RST _> GPIO 25
    CS -> GPIO8 (CE0)

## Install
* Install python and python-tkinter
* Install smart4pi tools

## Copy files
Copy the files in `systemd/` to `/usr/lib/systemd/system`.
Copy display.py and 99-fbdev.conf to `/home/pi`.

Run `systemctl daemon-reload` and then

    systemctl enable smartpi_nodered.service
    systemctl enable smartpi_readout.service
    systemctl enable smartpi_server.service
    systemctl enable tft.service

And start the services:

    systemctl start smartpi_nodered.service
    systemctl start smartpi_readout.service
    systemctl start smartpi_server.service
    systemctl start tft.service

## Running
### tft.service
This service does:
* `modprobe fbtft_device custom name=sainsmart18 gpios=reset:25,dc:12 width=128 height=160 rotate=90 speed=16000000`
  to spawn a `/dev/fb1` device
* start a new X11 server on fbdev `/dev/fb1`
* run `python /home/pi/display.py`
  which renders to `/dev/fb1` and connects to the smartpi server on localhost using TCP

### smartpi_readout.service
Runs /usr/local/sbin/smartpireadout

### smartpi_nodered.service
Runs /usr/bin/node-red

### smartpi_server.service
Runs /usr/local/sbin/smartpiserver

## Final result

![smart4pi_tft](https://raw.githubusercontent.com/siro20/smart4pi_sainsmart18/master/smart4pi_tft.jpg)
