## First Lego League Code
 #Code for recommended initializing procedures as well as templates for FLL code ideas
 
 #Initialization Programs
  - GyroChecker: The Gyro Sensor can drift if it is not held steady during power up. If the Gyro Sensor drifts, then it cannot be used to measure angles and to make the robot move in a straight line. The steps for this program are:

Reset the Gyro Sensor
Wait for half a second
Read the Gyro into a variable
Wait for two seconds (in those two seconds, the Gyro sensor may drift)
Compare the new Gyro value with the old Gyro value
If both values are equal, print “Gyro Okay” on screen
If both values are not equal, print “Gyro Bad” on screen
      
With our Gyro_check program, we can fix the drift problem, if any, and ensure our missions are run perfectly.

