# First Lego League Code
 Code for recommended initializing procedures as well as templates for FLL code ideas
 
 Code Documentation: https://docs.google.com/document/d/1L-vY9ZRlwiV9AIiR_AnPDOg0YfTWxm7PydY-MSLL1rA/edit?usp=sharing
 
 
 Initialization Programs
  - GyroChecker: The Gyro Sensor can drift if it is not held steady during power up. If the Gyro Sensor drifts, then it cannot be used to measure angles and to make the robot move in a straight line. With our Gyro_check program, you can fix the drift problem, if any, and ensure our missions are run perfectly. The steps for this program are:

    - Reset the Gyro Sensor
    - Wait for half a second
    - Read the Gyro into a variable
    - Wait for two seconds (in those two seconds, the Gyro sensor may drift)
    - Compare the new Gyro value with the old Gyro value
     - If both values are equal, print “Gyro Okay” on screen
     - If both values are not equal, print “Gyro Bad” on screen

  - Light Sensor Calibration: When in different areas, the reflective intensity of the black lines on the game mat vary. This variance in the reflective intensity of the lines in different locations can lead to incorrect light sensor inputs. Through the use of this program, you will be able to associate certain reflective intensity values with different colors, namely black and white.

  - NOTE: These programs must be run before each match.


QuickClick Program
  - Purpose: In between runs, you sometimes have to scroll through directories to find the program for you next run. This program solves this problem
  - main.py: This is where multiple run programs can be associated with different buttons.
  - RUNS Folder Copy and paste your code into these files in order to access it when clicking a button on the EV3 Brick.
  
  
     

