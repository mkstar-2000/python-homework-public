# Travel Planner Based on Currency Conversion Risk

**Project Goal:**  Create a travel planning tool that will allow the user to select a set of countries they would like to travel to and a travel timeframe (3,6,12 months).  The tool will analyze historical Forex data and predict the country that will have the most favorable currency within the given travel timeframe.

**The tool will:**
Check Forex volatility as barometer for travel decisions
Use historical forex data (up to 2 years)
3 - 6 - 12 months predictive outlook using Monte Carlo and other algorithms
Produce graphs, risk graphs, value graphs,
Variables - currency / country,  traveling times (3-6-12 months)


## Instructions

Complete the following steps.

1. Import the necessary libraries and dependencies.

2. Read in the `.csv` data.

3. Show the first `10` records of the data.

4. View summary statistics for the `.csv` data.

5. Create a Function to repeat this process for every instrument in the forex_pairs list. 


Create a subset DataFrame `filtered_df` by filtering out the important columns:

# Conversion Rate
##AllForexPairs
    * `date`
    * `close`
    * `int_rate`
    
-Use forex data to build a conversion calculator.
-Build a line plot and bar plot
-Build a candle stick chart
-Use Monte Carlo Simulator as function. 
-How each pair correlates with the other 
-News volatility (use an api for news calendar and parse major volatility)
-Build interst rate database on pgadmin using sql 



##Country    
    * `date`
    * `AllForexPairs`
    * `purpose`

Use lat lon data to build functioning maps through plotly. 
Px.scatter, barchart, line chart, heat map    
    
##Weather
    * `temp`
    * `projectjedForcast` 
    
Use weather data to build functioning weather forcaster map through plotly.



---

# Keep it clean, do not repeat code. set reusable code into variables and reuse when possible.

# Discuss variable naming structure. 