# Voting Information Project
The two CSV files in this repository, addresses and precinct_polling_list, are simply fictitious addresses of voters and precincts respectively.  Although they are not entirely freeform addresses, they are not properly structured and require cleaning.

The primary goal of this project is to merge addresses and precincts into a single table matching addresses to polling places.  Particular to this project is the creation of a composite key (a combination of two columns in one table used to uniquely identify).  The best way to do this is by creating a new ID (End ID) that matches the three digits following the hyphen in the Precinct ID column in the addresses table to the three digits following the hyphen in the Precinct column in the precincts table.  The secondary identifier to be used is the column State.

## Using the Voting Information Project
First, import the pandas library and the functions file.

<img src="images/Screen Shot 2019-12-30 at 10.45.49 PM.png" width="200" height="35">

Next, save the addresses and precinct_polling_list CSV files under the variables addresses and precincts respectively.

<img src="images/Screen Shot 2019-12-30 at 10.46.08 PM.png" width="400" height="40">

Continue to follow along with the code in the ipynb file. 
