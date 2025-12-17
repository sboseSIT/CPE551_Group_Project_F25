# CPE551_Group_Project_F25

Project Title:
Estimating Building Energy Usage, Temperature, and Humidity based on Occupancy, Building Type, and Time of Day

Student Names & emails:
Suraj Bose - sbose5@stevens.edu
Nicole Giardino - ngiardin@stevens.edu

Problem Description:
  A dataset (csv) is provided which consists of 7,200 records with detailed hourly (00:00 to 23:00) observations related to building energy consumption as temperature, humidity, building type, and occupancy changes. These observations are tied to 20 buildings with differing IDs, B001-B020, and the study was conducted for two full weeks. The team sets out to develop a python program capable of predicting the energy consumption of buildings under different conditions.

Program Structure:
  The first class that is defined and used is Building, which sets up the entire dataset using PANDAS. It stores lists of all the data for future use in the system. The next class, BuildingCalc, has a composition relationship with Building and calculates estimates for the data that can be acquired from the group's dataset: energy, temperature, and humidity. Here, time of day and temperature in Fahrenheit columns are made. A filter is created in this class for building type, occupancy level, and time period. This filter returns the values needed from the dataset, including the average, minimum, and maximum of the three values defined previously. A generator function is also defined to show the user rows that match their input criteria for building type, occupancy level, and time of day.
  In the main function, the user is prompted whether they would like to see the information summary for all buildings across the dataset using a while True loop. Then, a test section demonstrates the code's functionality by looking at the first few rows of the dataset, and also with a specific instance of the dataset. Next, a while True loop is set up to ask the user to enter the specific data they would like to see (building type, occupancy level, and time of day). The program then uses these inputs to print the values returned from BuildingCalc. These are displayed to the user through readable sentences.
  Then, the program loops through the filtered rows, appending each data point to its respective list of values, where a DataFrame is created. The list values are then sorted in place, and finally, using matplotlib, all of the data points (as well as horizontal asymptotes for the mean, max, and min) are plotted for the temperature, humidity, and energy for the user's entered conditions. Finally, a graph is displayed showing the three values on top of one another.

How to Use: 
  Upon hitting the run button, the user is prompted with the message: "Enter 'ALL' to see dataset stats ('X' or 'x' to exit)". Typing 'ALL' will display the total records for the dataset (7200 in this case) as well as the average energy use, temperature, and humidity across all data points. Once 'X' is entered, the user is provided with a test that demonstrates the functionality of the code. This test shows the first few rows of the DataFrame, with the added columns TimeOfDay and Temperature (F). Then, a test function is displayed showing the average energy, temperature, and humidity for the pre-defined test parameters: Industrial for Building, High for Occupancy, and afternoon for Time of Day.
  Next, the user is prompted with a series of questions allowing them to choose the results they would like to see displayed. The first question asks: "Enter a building type (1 - Industrial, 2 - Commercial, 3 - Residential, 4 - Educational) ('X' or 'x' to exit)". This allows the user to enter either the corresponding number or the name of the building type they would like to see (the numbers are included for additional user ease). The next question prompts the user about occupancy level (1 - High, 2 - Medium, 3 - Low). Finally, they are prompted about the time of day (1 - Morning, 2 - Afternoon, 3 - Evening, 4 - Night).
  After all of these questions are answered, the user is given a statement confirming the entries they provided. Then, they can read a series of sentences telling them the range (minimum and maximum values) and average for temperature, humidity, and energy. They are also provided with all rows that match their criteria in chronological order. Underneath, three graphs are displayed, one for each of the components, temperature energy and humidity, with horizontal asymptotes showing where the average, minimum, and maximum values fell along the graph. A fourth graph is also displayed, showing all three components on top of one another for further visualization.

Contributions of Each TeamMate:
Suraj- 
Nicole- 
