''''''''''''''''
Written by Suraj Bose & Nicole Giardino for 12/17/2025 submission for AAI/CPE/EE 551 WS/WS1 Final Group Project
This test file contains pytests for the Building and BuildingCalc classes.
'''''''''''''''
import pytest # three pytest trials are seen below
import pandas as pd

from Bose_Giardino_buildingClass import Building
from Bose_Giardino_buildingCalcClass import BuildingCalc

@pytest.fixture 
def fake_data(): # used for tests 1 and 2
    return pd.DataFrame({
        "Timestamp": [
            "2025-01-01 07:00:00",  # morning example
            "2025-01-01 13:00:00",  # afternoon example
            "2025-01-01 19:00:00",  # evening example
        ],
        "Energy_Usage (kWh)": [10, 20, 30],
        "Temperature (C)": [12, 24, 36],
        "Humidity (%)": [40, 45, 50],
        "Occupancy_Level": ["Low", "Medium", "High"],
        "Building_Type": ["Industrial", "Commercial", "Residential"]
    })

@pytest.fixture
def fail_fake_data(): # used for test 3
    return pd.DataFrame({
    "Timestamp": [
            "2025-01-01 07:00:00",
            "2025-01-01 13:00:00",
            "2025-01-01 19:00:00",
        ],
        #has different cases of invalid data
        "Energy_Usage (kWh)": [10, "NA", 30],
        "Temperature (C)": ["cold", 24, 36], 
        "Humidity (%)": [40, None, 50], 
        "Occupancy_Level": ["Low", "Medium", "High"],
        "Building_Type": ["Industrial", "Commercial", "Residential"]
    })


# test number one: pass
def test_timeofdaycategory(fake_data):
    #Ensure BuildingCalc Class creates a new column and creates timestep categories.
    #Must utilize both classes to test this functionality
    a = Building(fake_data)
    b = BuildingCalc(a)

    #Using assert to test for the timeofday categorization.
    assert "TimeOfDay" in b.df.columns
    assert b.df.loc[0, "TimeOfDay"] == "morning" 
    assert b.df.loc[1, "TimeOfDay"] == "afternoon"
    assert b.df.loc[2, "TimeOfDay"] == "evening"


# test number two: pass
def test_numeric_columns_valid(fake_data):
    #Check all expected number columns are numeric WITH VALID DATASET (expecting to work).
    a = Building(fake_data)
    b = BuildingCalc(a)

    numeric_columns = [
        "Temperature (C)",
        "Temperature (F)",
        "Humidity (%)",
        "Energy_Usage (kWh)"]


# test number three: fail
def test_numeric_columns_invalid(fail_fake_data):
    #Check all expected number columns are numeric WITH INVALID DATASET (expecting to fail).
    a = Building(fail_fake_data)
    b = BuildingCalc(a)

    numeric_columns = [
        "Temperature (C)",
        "Temperature (F)",
        "Humidity (%)",
        "Energy_Usage (kWh)"]