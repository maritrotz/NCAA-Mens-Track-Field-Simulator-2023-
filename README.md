# NCAA-Mens-Track-Field-Simulator-2023-
This project involved a full data analysis of the NCAA Mens track &amp; field performance lists to develop a prediction model of which team would win the NCAA track and field championships.

#STEP 1 - Data Scraping of TFFRS.org
I developed a Python script utilizing the Selenium library to automate the extraction of relevant data on the TFFRS website. I put the top 100 results from 21 different events into dataframes, and converted these dataframes into CSV files.

#STEP 2 - Data Cleaning
After converting all of the dataframes into csv files, I then removed duplicate values, specifically in the 4x100 and 4x400 files because there were multiple times for the same teams. 

#STEP 3- Data Analysis and Manipulation
I then loaded the csv files into Jupyter Notebook using Python's Pandas library. After loading the files in, I pulled the top 8 results from each dataset, and added the associated scores for each placing (1st to 8th, 10 to 1 points). After doing this, I converted the new top 8 results into csv files to be used for visualization.

I used SQL to automate the calculation on which team would win based on their placings in each of the events

#STEP 4 - Data Visualization
I visualized each first-team all american in each event (1st to 8th place), as well as the overall team standings using Tableau Public.  
