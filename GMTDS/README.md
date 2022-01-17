# Port congestion 

**Note: Data parsing is using the GMTDS .tiff data to generate numpy arrays for all the instances and storing them into a .JSON file. Since we didn't learn what metrics were being used by GMTDS, we decided on synthesizing data instead**


**Note: Currently dataprocessing uses synthetic data to generate summary statistics and forecasting. This would need to be updated to use the AIS data used by the NGA that we didn't have access to**

HOW TO USE: When the file dataprocessing.py is run, an interface comes up where we may enter the port of interest.

From there, we can choose either to receive summary statistics about the port, or predict traffic for an input date, or detect if a data instance is out of the ordinary or not. 
