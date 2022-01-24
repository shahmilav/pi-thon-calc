# Pi-Thon Calculator

![Calculator Screenshot](https://github.com/shahmilav/pi-thon-calc/blob/main/resources/pi-thon-calc-screenshot-new.png)

**This is a calculator made in Python using Tkinter.**

## Font Used
JetBrains Mono by, as expected, JetBrains.

## Known Bugs: 
- if ```0``` is the starting digit of the number entered, a ```Syntax Error``` will be shown.
  - example: ```052+8``` will return a ```Syntax Error```.
- if there is a syntax error caused in an expression that contains an x² or √, and the user deletes the error with _DEL_, then a different syntax will show.
  - for ```2²```, it will become ```2** 2```
  - for ```√(9)```, it will be ```sqrt(9)```.
