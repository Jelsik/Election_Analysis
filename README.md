
# Auditing The Election

## Overview of Audit

The purpose of this analysis was to take information from a hypothetical Colorado election
in the format of a .csv file, read the data from it, and then determine who won the election using
python scripting. The analyized data would then be written to a text file for review.

## Election-Audit Results

And with all said and done, the results were in!

![ElectionResults](https://github.com/Jelsik/Election_Analysis/blob/main/Results.PNG)

Taking that data into mind, we can see that:

* A Total of 369,711 votes were cast in this election
* The Counties had a wide variance in population or turnout, with Denver providing 82.8%(306,055) of the vote, Jefferson providing 10.5%(38,855) of the vote, and Arapahoe 6.7%(24,801) of the rest.
* Denver County, we can see, by far, had the largest number of votes, with 306,055 of the total 369,711
Those votes were distributed out to these candidates:
* Raymon Anthony Doane, who won 3.1%(11,606) of the vote
* Charles Capser Stockham, who won 23.1%(85,213)
* Diana DeGette, who won 73.8%(272,892)

Which brings us to our winner:
* Diana DeGette, with the beforementioned 272,892(73.8%) votes, has claimed victory.

## Audit Summary

Based off of the above analysis, this script is effective at determining the victor in this election. However,
with some modifications this script could be adjusted to work for any election. Rather than merely counting votes towards
a total, the script could also be edited to count ballots related to votes opposing or in support of propositions.
With the addition of a scond conditional statement, a second mirrored dictionary to collect the votes 'against' a
proposed option could operate during the data reading. The two sets of data could then be compared to determine the outcome

A second way that this script could be modified to be used for another election is in the scope. For this election
the data collceted in a simple ballot number/county/candidate format. However, it could accept more complicated data
and parse it if the width of columns searched in reading the file were widened. In this way, it could check for data sets that were more complex
or had more than one response in them. In a hypothetical ballot#/county/candidate/decision1/decision2 etc. format.
