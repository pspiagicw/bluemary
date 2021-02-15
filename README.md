# BlueMary

A TUI Based tool which uses bluetoothctl in the background to provide a ncurses interface to connect and control bluetooth devices.

Currently this is just a new project and has a lot of bugs and is not for daily use.
!! Use at your own risk !!.

## Installation
This must be installed using setup.py
```sh
python setup.py install
```
After I submit this on PyPI you could install by 
```sh
pip install bluemary
```


## Usage
It has a interface with just 3 screens.
The first form is a summary form with the list of paired devices and then option to choose Connect or Disconnect.
You choose the then press OK.
It takes you to the required screen.
After that it is just matter of selecting the device shown and pressing OK.Which takes you back to the summary screen.
Press Ctrl-C to exit.

## Contributing
If you want to contribute you can contribute by filing a bug report.



