import numpy as np 
import pandas as pd 
from scipy import stats
from scipy.stats import ks_2samp
import matplotlib.pyplot as plt
from statistics import mean
from statistics import pstdev
import random
   
def general_info_port(data):
    """
    Returns mean and standard deviation of port ship hours for an input port, 
    aggregated either monthly, yearly, or quarterly (seasonal)
    """
    monthly=[]
    seasonal=[]
    yearly=[]
    for i in range(len(data)):
        monthly.append(data[i])
    for i in range(len(data)):
        if (i+1)%3==0:
            seasonal.append(data[i])
    for i in range(len(data)):
        if (i+1)%12==0:
            yearly.append(data[i])

    return mean(monthly),pstdev(monthly), mean(seasonal),pstdev(seasonal), mean(yearly),pstdev(yearly)

def prediction(position,data):
    """
    Returns predicted traffic data for an input date
    """
    monthly_avg, monthly_std, seasonal_avg, seasonal_std, yearly_avg, yearly_std=general_info_port(data[:,2])
    monthly_predict=data[position-1,2]+monthly_avg
    seasonal_predict=data[position-3,2]+seasonal_avg
    yearly_predict=data[position-12,2]+yearly_avg

    return monthly_predict,monthly_std,seasonal_predict, seasonal_std, yearly_predict, yearly_std

def abnormal_detection(position,data,true_value):
    """
    Checks if a given instance of ship traffic data is abnormal or not for that port
    for that time of year
    """
    monthly_predict,monthly_std,seasonal_predict, seasonal_std, yearly_predict, yearly_std=prediction(position,data)
    
    std_tolerance=1
    
    monthly_low=monthly_predict-monthly_std*std_tolerance
    monthly_high=monthly_predict+monthly_std*std_tolerance
    if true_value<monthly_low or true_value>monthly_high:
        print("Alert-monthly: was expecting ", monthly_low, " to ", monthly_high, ", but is ", true_value)
    else:
        print("Normal-monthly")
    
    
    seasonal_low=seasonal_predict-seasonal_std*std_tolerance
    seasonal_high=seasonal_predict+seasonal_std*std_tolerance
    if true_value<seasonal_low or true_value>seasonal_high:
        print("Alert-seasonal: was expecting ", seasonal_low, " to ", seasonal_high, ", but is ", true_value)
    else:
        print("Normal-seasonal")


    yearly_low=yearly_predict-yearly_std*std_tolerance
    yearly_high=yearly_predict+yearly_std*std_tolerance
    if true_value<yearly_low or true_value>yearly_high:
        print("Alert-yearly: was expecting ", yearly_low, " to ", yearly_high, ", but is ", true_value)
    else:
        print("Normal-yearly")


def get_port_data(all_data, name):
    """
    Generates synthetic data for main function. Data follows a random walk trend 
    so that values near each other have similar values
    """
    features=3
    coefficient=100
    year_number=10
    data = []
    scale_feature1 = 100
    scale_feature2 = 60
    scale_feature3 = 30
    
    for _ in range(year_number*12):
        data.append([scale_feature1, scale_feature2, scale_feature3])
        scale_feature1 = abs(scale_feature1 + random.randrange(-4, 7))
        scale_feature2 = abs(scale_feature2 + random.randrange(-2, 6))
        scale_feature3 = abs(scale_feature3 + random.randrange(-4, 8))
    return np.array(data)

def main():
    """"
    Serves as the interface for accessing the other functions. Takes in 
    query input from the user and provides the specifiec functionality
    """
    print("Select desired port to get information:")
    port_name = input()
    print("- Selected port:", port_name)
    port_data = get_port_data([], port_name)
    
    while True:
        print("Select one of the follow commands: 'port_info', 'prediction', 'abnormal_detection', or 'quit'")
        command = input()
        if command == 'port_info':
            monthly_avg, monthly_std, seasonal_avg, seasonal_std, yearly_avg, yearly_std = general_info_port(port_data[:,2])
            print("Monthly average traffic: ", round(monthly_avg,2), " ship hours")
            print("Monthly change in traffic: ±", round(monthly_std,2), " ship hours")
            print("Seasonal average traffic:", round(seasonal_avg,2), " ship hours")
            print("Seasonal change in traffic: ±", round(seasonal_std,2), " ship hours")
            print("Yearly average traffic:", round(yearly_avg,2), " ship hours")
            print("Yearly change in traffic: ±", round(yearly_std,2), " ship hours")
            print()
        elif command == 'prediction':
            while True:
                print("Enter a desired month in format YYYY.MM starting from 2012.01 (please don't select month in 2012)")
                position = input()
                try:
                    year = int(position.split(".")[0])
                    month = int(position.split(".")[1])
                    if month > 12:
                        print("Invalid month...")
                    elif year < 2012:
                        print("Invalid year...")
                    else:
                        position = (year - 2012) * 12 + (month - 1)
                        monthly_predict,monthly_std,seasonal_predict, seasonal_std, yearly_predict, yearly_std = prediction(position, port_data)
                        print("Monthly predicted traffic: ", round(monthly_predict, 2), " ship hours")
                        print("Monthly predicted change in traffic: ±", round(monthly_std, 2), " ship hours")
                        print("Seasonal predicted traffic:", round(seasonal_predict, 2), " ship hours")
                        print("Seasonal predicted change in traffic: ±", round(seasonal_std, 2), " ship hours")
                        print("Yearly predicted traffic:", round(yearly_predict, 2), " ship hours")
                        print("Yearly predicted change in traffic: ±", round(yearly_std, 2), " ship hours")
                        print()
                        break
                except:
                    print("Invalid format")
        elif command == 'abnormal_detection':
            while True:
                try:
                    print("Enter a desired month in format YYYY.MM starting from 2012.01 (please don't select month in 2012)")
                    position = input()
                    year = int(position.split(".")[0])
                    month = int(position.split(".")[1])
                    if month > 12:
                        print("Invalid month...")
                    elif year < 2012:
                        print("Invalid year...")
                    else:
                        print("Enter a true value to compare real data to the prediction data (must be a positive number):")
                        true_value = int(input())
                        position = (year - 2012) * 12 + (month - 1)
                        abnormal_detection(position, port_data, true_value)
                        break
                except:
                    print("Invalid format")
        elif command == 'quit':
            break
        else:
            print("Invalid command")
            

if __name__ == "__main__":
    main()