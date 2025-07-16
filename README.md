Improving LEO Satellite Orbital Predictions with Machine Learning

--------------------------------------------------------
Project Overview
--------------------------------------------------------
This project investigates the use of machine learning to improve the accuracy of orbital predictions for Low Earth Orbit (LEO) satellites. The core objective is to correct for errors in a satellite's predicted Mean Motion, a fundamental parameter governing its orbital speed and position. By accurately predicting the error of the standard SGP4 physics-based model, we can produce a more precise orbital state, which in turn enables more accurate calculations of satellite pass times (AOS/LOS) for ground stations.

The project uses historical orbital data for the Landsat 8 satellite and corresponding space weather data. A key finding of this analysis is the significant challenge posed by concept drift, where the model, trained on data from a calmer solar cycle, fails to generalise to the more active solar cycle present in the test data. This repository serves as a comprehensive demonstration of an end-to-end machine learning project, from data acquisition to the analysis of a critical real-world modelling challenge.

#########################################################
--------------------------------------------------------
Data Extraction
--------------------------------------------------------
The project requires two datasets. Two Python scripts are provided to download them automatically.

Important: These scripts will create a data/ directory in the project root if it does not already exist and will save the files inside it.

Download TLE Data:

Open the download_tle.py script.

Enter your Space-Track.org username and password in the placeholder variables. My details are already there if wanted to be used

Run the script from your terminal:

python download_tle.py

This will create data/landsat8_tle_history.txt.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Download Space Weather Data:

Run the download_sw.py script from your terminal:

python download_sw.py

This will create data/SW-All.txt.

##########################################################
--------------------------------------------------------
Project Documentation
--------------------------------------------------------
The final, detailed project report can be found in the file: LEO Satellite Pass Prediction Error Correction.docx. This document provides a comprehensive walkthrough of the project plan, methodology, results, and conclusions.