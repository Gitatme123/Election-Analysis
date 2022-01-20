# **Analysis of Election Audit**

## **Overview of Project**

#### In this project, we are helping our friends Seth and Tom audit some election data for the election commissioner. In order to do this, we have put together a python file with a script that is able to scan a csv file, aggregate and organize the analysis and then automates our desired output into a text file that then can be shared.
#### Before Seth and Tom can deliver this file to the commissioner, they received additional data requests for the audit. We have just finished editing our script to include outputs for the new requests and are ready to deliver the script. We have also included a list of pros and cons with examples for how the script could be used in any election so that the commissioner might want to purchase this script from us.

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


## **Summary of the Election Audit Script with Opportunities for further use**

Pros of the script for business prop:
* The script gives us a custom output 
* It is able to read a scan through a large amount of votes, something excel may trip up with
* The script can be edited based on changing requirements with the general structure remaining intact

Cons of the script for business prop:
* The script requires python, since it is a .py file
* It's output is relatively simple, giving us outcomes, and isn't able to performan an analysis in its current form
* The script as is, is relatively limited. It's ability to print out our outcomes would be more valuable if there were tons of datasets that needed to be scanned. For example, the entire state of Colorado and it's counties.

With the success of the script, we were able to aggregate over 369,000 votes, an output of desired stats and text answers to specific questions we programmed in. Now this can all be done using VBA and some of it can be done using pivot tables, but what our program script is able to read the csv file and aggreagate the data my means of the content of our script. This is also easily done in excel using pivot tables. But what excel can not offer here without VBA and macros, is the logic that enables us to print out answers to questions or specific statistics from the dataset. Now the script was able to automate output and that may be where we'll find our value proposition for the

## Business proposition: Use in any given election
This script is able to accomplish quite a few feats given the low level of energy needed to run. This script can also be repurposed for any election, and therefore is a valuable asset to have. Below i have provide 2 examples for other use cases in analyzing election data.

**Example 1)** Since the script is not tied to any county name or any spceific candidate name, we can easily repurpose this for any other election. The key requirement is that we would have to ensure the dataset is in a csv file with the same data in the same columns. That just means that column A needs to be the county column for any dataset. Columm B would need the candidate name. It could be 100 different counties and different candidates, only as long as the dataset has the correct data in the same columns.
  * If the data is not in the same columns, we can identify exactly where in the code we would need to change things to read the new csv file properly. 
> ![Screen Shot 2022-01-20 at 3 23 54 PM](https://user-images.githubusercontent.com/95602006/150424345-6e7383a4-3681-481e-9d7e-7d92c6fa7de9.png)
  * We see below in the screenshot that the candidate name is being pulled from row[2]. THis meas that it is the 3rd columm in our csv file. If the candidate name was in the 4th column, also known as column D, we would replace the 2 with a 3 because it is index counting, which starts at 0 instead of 1. It would then look like this: candidate_name = row[3]
  * We could also do the same thing for the county name which is currently reading as county_name = row[1]. This means its reading column B, or column 2. If we knew the county data was in column F, we would then substitute the row[1] with row [5].
  

**Example 2)** This dataset is very simple and can't really provide any insights that would normally come with an audit. I would propose that we open it up and add multiple more columns including but not limited to: Polling Site, Polling Day, Polling Time, Party Affiliation etc. One thing I would want on here is polling station or method. That would be an addition to our script but it would provide a better view at the distribution. A county can be huge, and not much can be extrapolated from that.
  * We can do that by adding new lists and new dictionaries similar to what we do in this step
> ![Screen Shot 2022-01-20 at 4 31 13 PM](https://user-images.githubusercontent.com/95602006/150432591-5c1ecc71-32d9-4fc6-b008-3cde2ac032e0.png)
  * Then we would add a few variables to track the new category similar to the screenshot below
> ![Screen Shot 2022-01-20 at 4 35 26 PM](https://user-images.githubusercontent.com/95602006/150433025-93f530e9-46f4-4e21-bb10-92de5fd7cd8e.png)
  * We would then have to add the new category in our initial for statement similar to the script line below 
> ![Screen Shot 2022-01-20 at 4 32 46 PM](https://user-images.githubusercontent.com/95602006/150432744-ec0c0d97-434d-4e10-a782-08203938d290.png)
  * Then we would have to add another if statement to add the new category option to our list similar to the screenshot below
> ![Screen Shot 2022-01-20 at 4 33 33 PM](https://user-images.githubusercontent.com/95602006/150432822-2a548934-6f93-4675-a74e-6109e860f07e.png)
  * Then we would add another for-if statement that would get the votes assosiated with the new category we introduced similar to the screenshot below.
> ![Screen Shot 2022-01-20 at 4 39 15 PM](https://user-images.githubusercontent.com/95602006/150433428-22b886bb-07f9-42f2-9c23-5c988abe0c31.png)
  * You'll notice in the screenshot below, we have entered a script that prints a text output. We would then add, edit, copy and paste and edit this section to output different results with our new categories from this script.
> ![Screen Shot 2022-01-20 at 4 40 31 PM](https://user-images.githubusercontent.com/95602006/150433579-d521be83-ebcf-46b7-8790-8f1a95050ad4.png)


