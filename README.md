# ArduinoXY
Processing3 Python Mode plotting image used for Instructables.com project by High Voltage Fun.
https://www.instructables.com/id/Arduino-XY-Oscilloscope-Shield/

Data XY Point file formatted according to High Voltage Fun's Arduino Sketch.
file xy.txt in the same directory as the Processing3 Python sketch.

xy.txt file should contain data formatted according to the example data below.
The number of point pairs on each line is optional.
-------------------------------------------------------------------------------------

41, 85, 40, 92, 41, 101, 43, 110,<br>
 46, 118, 49, 126, 54, 134, 60, 141,<br>
 67, 146, 74, 152, 82, 156, 90, 159,<br>
 99, 160, 108, 161, 117, 160, 125, 158,<br>
 133, 156, 141, 152, 148, 147, 155, 141,<br>
 158, 138,<br>
255,<br>
 153, 137, 152, 138, 146, 144, 139, 148,<br>
 132, 152, 124, 155, 116, 156, 108, 157,<br>
 99, 157, 91, 155, 83, 152, 76, 148,<br>
 69, 143, 63, 138, 57, 131, 52, 124,<br>
 49, 117, 46, 109, 45, 100, 44, 92,<br>
 44, 88,<br>
255,<br>
 63, 45, 69, 40, 76, 35, 84, 31,<br>
 91, 29, 100, 27, 108, 26, 116, 27,<br>
 124, 29, 132, 32, 140, 36, 147, 40,<br>
 153, 46, 158, 52, 163, 59, 166, 67,<br>
 169, 75, 171, 83, 171, 92, 171, 96,<br>

-------------------------------------------------------------------------------------
Each 255 will move the plot point to the next X1,Y1 without drawing a line.  The next line
will be drawn from that X1,Y1 point to the following X2,Y2 point.
