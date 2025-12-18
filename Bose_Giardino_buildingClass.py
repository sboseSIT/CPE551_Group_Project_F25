''''''''''''''''
Written by Suraj Bose & Nicole Giardino for 12/17/2025 submission for AAI/CPE/EE 551 WS/WS1 Final Group Project
This class file contains the Building class that stores building data.
'''''''''''''''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Building:
    def __init__(self, dataframe):
        # sets up the full dataset rather than just the selected one
        #PANDAS Dataframe is mutable
        self.df = dataframe.copy()

        # storing lists of all the data - looks at columns and pulls them as attributes
        self.timestamps = self.df["Timestamp"]
        self.energy = pd.to_numeric(self.df["Energy_Usage (kWh)"], errors="coerce")
        self.temperature = pd.to_numeric(self.df["Temperature (C)"], errors="coerce")
        self.humidity = pd.to_numeric(self.df["Humidity (%)"], errors="coerce")
        self.occupancy = self.df["Occupancy_Level"]
        self.building_type = self.df["Building_Type"]
        
    def __len__(self): #operator overloading for len() function
        return len(self.df)

    def __str__(self): # returns a readable string summarizing dataset for checking, #len() is also a built in module/library
        return (
            f"Total records: {len(self)}\n"
            f"Average Energy Usage: {self.energy.mean():.2f}\n"
            f"Average Temperature: {self.temperature.mean():.2f}\n"
            f"Average Humidity: {self.humidity.mean():.2f}"
        )
