# Bluestacks_Tap
 A simple script to tap in bluestacks incrementally or decrementally

 Bluestacks uses a percentage value to determine the location on the screen.

 You can set your resolution in the program and then use the in-built bluestacks scripting function to find the percentages on the screen

 The X and Y values in the array are paired.

 With every press, the locations are looped through incrementally or decrementally.

 I wrote this because it would be much easier to have a button or key to cycle through (for instance, weapons) rather than having every location attached to a keybind

 Bluestacks doesn't have this function inherently in all the reseach I did

 Make sure you're running this file in the adb directory. as you should have adb.exe installed

 Bluestacks should also have debug mode enabled from the settings and run use adb to run ".\adb.exe connect localhost:5555" 

then you can run this script