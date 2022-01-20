# **Analysis of Election Audit**

## **Overview of Project**

### Purpose
#### In this project, we are helping our friends Seth and Tom audit some election data for the election commissioner. In order to do this, we have put together a python file with a script that is able to scan a csv file, aggregate and organize the analysis and then automates our desired output into a text file that then can be shared.
#### Before Seth and Tom can deliver this file to the commissioner, they received additional data requests for the audit. We have just finished editing our script to include outputs for the new requests and are ready to deliver the script. 

## **Results**

##### 1. How many votes were cast in this congressional election?
> ![Screen Shot 2022-01-20 at 2 54 52 PM](https://user-images.githubusercontent.com/95602006/150420707-309a2305-ba19-458a-94a6-e40d48daeb02.png)
##### 2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
> ![Screen Shot 2022-01-19 at 10 24 23 PM](https://user-images.githubusercontent.com/95602006/150273161-f6f563e6-e0f7-4ef7-b7b7-99ade7154ad8.png)
##### 3. Which county had the largest number of votes?
> <img width="277" alt="Screen Shot 2022-01-20 at 10 59 01 AM" src="https://user-images.githubusercontent.com/95602006/150385809-05bae2ad-5dcc-4bcd-953a-c655bcba453e.png">
##### 4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
> <img width="340" alt="Screen Shot 2022-01-20 at 10 58 12 AM" src="https://user-images.githubusercontent.com/95602006/150385680-38d3cda4-2049-4961-80ed-eef086cc2ad0.png">
##### 5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
> <img width="257" alt="Screen Shot 2022-01-20 at 10 58 29 AM" src="https://user-images.githubusercontent.com/95602006/150385724-ce842b9d-1e4e-41be-ab1c-e90fde935526.png">


## **Summary**

#### In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
Pros for business prop:
* The script gives us a custom output
* It is able to read a scan through a large amount of votes, something excel may trip up with
* Its quick

Cons for business prop:
* The script requires python, since it is a .py file
* It's output is relatively simple
* The script as is, is relatively limited. It's quickness would be valuable if there were tons of datasets that needed to be scanned. For example, the entire state of Colorado and it's counties.

With the success of the script, we were able to aggregate over 369,000 votes, an output of desired stats and text answers to specific questions we programmed in. Now this can all be done using VBA and some of it can be done using pivot tables, but what our program script is able to read the csv file and aggreagate the data my means of the content of our script. This is also easily done in excel using pivot tables. But what excel can not offer here without VBA and macros, is the logic that enables us to print out answers to questions or specific statistics from the dataset. Now the script was able to automate output and that may be where we'll find our value proposition for the

### Examples for use in any election
Example 1) Since the script is not tied to any county name or any spceific candidate name, we can easily repurpose this for any other election. The key requirement is that we would have to ensure the dataset is in a csv file with the same data in the same columns. That just means that column A needs to be the county column for any dataset. Columm B would need the candidate name. It could be 100 different counties and different candidates, only as long as the dataset has the correct data in the same columns.
Example 2) This dataset is very simple and can't really provide any insights that would normally come with an audit. I would propose that we open it up and add multiple more columns including but not limited to: Polling Site, Polling Day, Polling Time, Party Affiliation etc. 
One thing I would want on here is polling station or method. That would be an addition to our script but it would provide a better view at the distribution. A county can be huge, and not much can be extrapolated from that.



