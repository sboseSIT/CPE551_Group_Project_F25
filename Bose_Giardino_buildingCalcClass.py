''''''''''''''''
Written by Suraj Bose & Nicole Giardino for 12/17/2025 submission for AAI/CPE/EE 551 WS/WS1 Final Group Project
This class file contains the BuildingCalc class that performs calculations on building data.
'''''''''''''''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class BuildingCalc:
    """
    This class has a composition relationship with the Building class. 
    Ex. Week 12 Composition Slides: "has-a" relationship
    Class function is to calculate estimates for energy, temp, humidity based
    on inputs of: building type, occupancy level, and time
    """
    def __init__(self, building):
        #this is a constructor.
        #Storing the building instance in this separate class.
        self.building = building #composition within this class to the previous class
        # dataframe from the building instance.
        df = self.building.df.copy()
        #Filtering the data to create a new timeofday column (separates timestamps)
        df["TimeOfDay"] = df["Timestamp"].apply(self._categorize_time)
        # getting the data in Fahrenheit rather than Celcius 
        df["Temperature (F)"] = [temp * 9/5 + 32 for temp in df["Temperature (C)"]] # list comprehension
        self.df = df
        

    def _categorize_time(self, ts):
        #This function works by sorting the timestamps into morning, afternoon, evening, night
        hour = pd.to_datetime(ts).hour

        if 6 <= hour < 12:
            return "morning"
        elif 12 <= hour < 17:
            return "afternoon"
        elif 17 <= hour < 23:
            return "evening"
        else:
            return "night"
        
    #Determines the avg energy, temp, humidity given the:
    #Building type, occupancy level, and time period
    def estimate(self, building_type, occupancy_level, time_period, show_rows = False):
        #Process details:
        #Select all rows which fulfill the filter requirements
        # Use filter + lambda to select matching rows
        # See Week 14 – filter, lambda
        filtered = pd.DataFrame(
            #Filter is an example of a built in module/functionality
            filter(
                lambda row: 
                (row["Building_Type"] == building_type and row["Occupancy_Level"] == occupancy_level and row["TimeOfDay"] == time_period), self.df.to_dict("records"))
        )

        #State there is no data for this case, if there is no match- using valueerror
        if filtered.empty:
            raise ValueError("No data available for the given parameters.")
        

        #This if statement is for testing to ensure the correct data rows are used for testing
        #if show_rows:
        #    print("Filtered DataFrame used for calculation:")
        #    print(filtered)
        #    print()

        #Calc the average of filtered datasets
        return {
            "Estimated Temperature (C)": filtered["Temperature (C)"].mean(),

            "Estimated Temperature (F)": filtered["Temperature (F)"].mean(),
            "Temperature Minimum (F)": filtered["Temperature (F)"].min(),
            "Temperature Maximum (F)": filtered["Temperature (F)"].max(),

            "Estimated Humidity (%)": filtered["Humidity (%)"].mean(),
            "Humidity Minimum (%)": filtered["Humidity (%)"].min(),
            "Humidity Maximum (%)": filtered["Humidity (%)"].max(),

            "Estimated Energy (kWh)": filtered["Energy_Usage (kWh)"].mean(),
            "Energy Minimum (kWh)": filtered["Energy_Usage (kWh)"].min(),
            "Energy Maximum (kWh)": filtered["Energy_Usage (kWh)"].max()
        } 
    def row_check(self, building_type, occupancy_level, time_period):
        #Generator function to show rows matching criteria input by user
        for row in self.df.to_dict("records"):
            if (
                row["Building_Type"] == building_type and 
                row["Occupancy_Level"] == occupancy_level and 
                row["TimeOfDay"] == time_period
            ):
                yield row