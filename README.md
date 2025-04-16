# Skill Seeds & Career Roots: Early Careers and Skills Development
## Project overview
We have chosen a Kaggle's survey on Machine Learning and Data Science in 2020. There was no specifically required results, as the survey was made with the purpose of discoverig different data stories about a subset of the data science community represented in it.

For our story, we have decided to exploit the data to get insights on __'which skills and programming languages machine learning beginners should learn to earn a better chance when entering the job market'__.
 
### Introduction to the dataset

[Data Source](https://www.kaggle.com/c/kaggle-survey-2020/overview)

The dataset is of raw format, consisting of 355 columns and over 20,000 observations (each column recored the answers to the question on the first line after the header). 

The survey only had 39 multiple choice questions, but for certain questions that allow more than one choice, another column would appear in accordance with each choice. (This explains why in certain columns, there are only 1 value and the rest is null).

_For more information on the variables, please visit the following [LINK](https://docs.google.com/document/d/1cvFLwSeV20bbl6zc1V08Ev19oHazCVwT65OChMs40j4/edit?usp=sharing)_

### Introduction to the story plot

In short, the story begins with our main character, Quan, a newly graduate with a dream to become a machine learning engineer. However, since he still has little practical experience, he felt lost and did not know what step he should take to achieve his dream. (Unfortunately, Quan is the embodiment of many young people with the same struggle after graduation in reality.) 

_And so, through exploring this dataset, we hope to give him a clearer idea on the path to his dream job._

## Project Details
### Data Cleaning & Processing
* Import data
```
import pandas as pd
data = 'kaggle_survey_2020_responses.csv'
data = pd.read_csv(data)
data.head()
# Remove row 0
data = data.iloc[1:]
```
* Check for missing values
```
pd.set_option('display.max_rows', None)
na_counts = data.isna().sum()
print(na_counts)
```

* Import functions
```
from processing_function import *
from file_seperater import *
df = pd.DataFrame(data)
```
**Explanation**: 

In 'processing_function.py' are all the **self-coded** functions we need to process the raw data (and for EDA later on). To summarize, here are the functions we are going to use: "fhelp", "col_format", "add_sum_col", "cavo", "gcbp", "vvc", "heatmapping", "favc", "rename_col".

In 'file_seperater.py' is the function used to filter a separated dataframe for later use.

_More explanation will be added along the way, but for thorough details on how to use these functions, please open these files on Github._

* Ways to handle missing data

Generally, there were quesions with only one answer and questions with multiple answers selected.

__For data columns of multiple-selections questions, we transferred all the unique values to 1 and NAs (the rest) to 0.__
```
questions = [
    "Q7", "Q9", "Q10", "Q12", "Q14", "Q16", "Q17", "Q18", "Q19", "Q23", 
    "Q26_A", "Q27_A", "Q28_A", "Q29_A", "Q31_A", "Q33_A", "Q34_A", "Q35_A", 
    "Q36", "Q37", "Q39", "Q26_B", "Q27_B", "Q28_B", "Q29_B", "Q31_B", 
    "Q33_B", "Q34_B", "Q35_B"
]

for question in questions:
    column_names = gcbp(data, question)
    data = col_format(data, column_names)
```
Next, we renamed these columns for better visual efficency.
```
# Example (apply similarly to the other columns)
Q7_columns = gcbp(data, "Q7_")
data = rename_col(data, Q7_columns, "Q7_")
```

__For columns with only 1 answer, we handled missing values in 2 ways.__

_For columns on personal detail of the surveyee (Q1 to Q6), we dropped the rows with NA, as it cannot be replaced._

``` 
# Check for NAs in columns 'Q1' to 'Q6'
na_check = data[['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']].isna().sum()
print(na_check)
# Remove rows with NAs in Q4, Q5, and Q6
data = data.dropna(subset=['Q4'])
data = data.dropna(subset=['Q5'])
data = data.dropna(subset=['Q6'])
```
_For the rest, we replaced null with 'none', 'unknown' or others similarly._
```
#Examples
replace_na(data, 'Q8', 'None')
replace_na(data, 'Q11', 'Other')
replace_na(data, 'Q15', 'I do not use machine learning methods')
replace_na(data, 'Q24', 'Unknown')
```
Among these, there are cases in which questions are related to another one, so we replaced some values in those cases depending on the surveyee's answers to the related one.

(For instance, 'Question 30: Which of the big data products in Q29 you use the most?' And so, if the individual choose 1 choice or less in Q29, the value of that row in Q30 will be changed to 'Not questioned')
```
data.loc[data['Q29_ATotal'] <= 1, 'Q30'] = 'Not Questioned'
data.loc[data['Q31_ATotal'] <= 1, 'Q32'] = 'Not Questioned'
```
* Convert into a csv file
```
data.to_csv('cleaned-data.csv', index=False)
```

* Filter for valuable data related to machine learning

Our story specifically target the machine learning engineer sector in the job market, so we tend to value the opinions given by people with that position. And so, we extracted all the rows with answers from machine learning engineers into a new dataframe. This would be the dataframe we mainly use in EDA.
```
# This is a function imported from 'file_seperater.py'
separate_roles('cleaned-data.csv')
```


### EDA
* Import libraries and separated dataframe
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
data = 'machine_learning_engineers.csv'
data = pd.read_csv(data)
data.head()
df = pd.DataFrame(data)
```
* _**How does the job market for ML engineer look like around the globe?**_
```
df['Q3'] = df['Q3'].replace({
    'United States of America': 'USA',
    'United Kingdom of Great Britain and Northern Ireland': 'UK',
    'Iran, Islamic Republic of...': 'Iran',
    'Republic of Korea': 'South Korea',
    'United Arab Emirates': 'UAE'
})
unique_values_q3 = df['Q3'].unique().tolist()
print("Shortened unique values in Q3:", unique_values_q3)
vvc(df, 'Q3', 'Country', 'Counts', 'ML engineers country-wise distributrion', bar_width= 4, bar_spacing= 8,angling=90,label_size=8)
```
![graph3](https://i.imgur.com/glxFwRB.png)

*Insight:* 

*ML engineer is an occupation that seems to be most popular in India and the U.S.*

* _**How high of education do ML engineers usually have?**_
```
title = "Education level in relation to the working field"
df['Q4'] = df['Q4'].replace({
    'Doctoral degree': 'PhD',
    'Master’s degree': 'Master',
    'Bachelor’s degree': 'Bachelor',
    'I prefer not to answer': 'No answer',
    'Some college/university study without earning a bachelor’s degree': 'Some college',
    'No formal education past high school': 'High school',
    'Professional degree': 'Professional'
})
vvc(df, "Q4", "Education level", "Number of engineers", title)
```
![graph4](https://i.imgur.com/j3LAaS8.png)

*Insight:* 

*It can be seen that a majority of ML engineers posess a graduate degree, be it master, PhD or bachelor (the 3 study level with the most numbers of engineers). Among them, particularly, the master degree is the most common, then followed by the bachelor degree.*

*=> Through that, it can be conclude that for Quan, a bachelor degree alone is quite fine. But if he want a higher chance of landing a job as ML engineer, maybe he should consider pursueing a master degree.*

* _**What are the most common ML frameworks and algorithms?**_
```
cavo(df, gcbp(df, "Q7"),xlabel= 'Programming language',ylabel= "Number of users", title = "Programming Languages User count", horizontal=True)
```
![g7](https://i.imgur.com/Ak3EP70.png)
```
cavo(df, gcbp(df, "Q16",),xlabel= 'Number of users',ylabel= "ML framework", title= "ML frameworks User count",horizontal=True)
```
![g16](https://i.imgur.com/q9ADrzy.png)
```
cavo(df, gcbp(df, "Q17",),xlabel= 'Number of users',ylabel= "ML algorithm", title= "ML algorithms User count", horizontal=True)
```
![g17](https://i.imgur.com/3RhDU0L.png)

*Insights:*

*The Python programming language seems to be distinctly more common among the engineers compared to the rest.* 

*For Machine Learning, Scikit-learn, TensorFlow, and Keras are the used frameworks ML engineers usuallty work with, while the most used algorithms are linear/logistics regression, CNN, random forest, gradient boosting machines.*

*=> With that, Quan should definitely focus on sharpening his Python programming skill and familiarize himself with the mentioned frameworks and widely-used algorithms.Though not all of them will be applied in every company, but knowing them might increase his chance of getting a job.* 

* _**What are the most common ML products?**_
```
cavo(df, gcbp(df, "Q28_A",), xlabel= "ML product",ylabel= "Number of users", title = "ML products usage", horizontal=True)
```
![g28a](https://i.imgur.com/YuyzQ9N.png)

*Insights:*

*There is a large number of people who do not use a ML product, but among those who does, the most popular ones are Amazon Sagemaker and Google Cloud ML Engine.*

*=> It's fine even if Quan does not use any ML product, but knowing how to use one of the two above might earn him plus points from future employers.*

* _**What are the notable traits of the ML engineer sector in the job market?**_
```
vvc(df, "Q6", "Coding Experience Years", "Number of engineers", title = "ML Engineers by Coding Experience Years")
```
![g6](https://i.imgur.com/jxCTco9.png)
```
df['Q15'] = df['Q15'].replace({
    'Under 1 year': '<1 year',
    '1-2 years': '1-2 yrs',
    '2-3 years': '2-3 yrs',
    '3-4 years': '3-4 yrs',
    '4-5 years': '4-5 yrs',
    '5-10 years': '5-10 yrs',
    '10-20 years': '10-20 yrs',
    '20 or more years': '20+ yrs',
    'I do not use machine learning methods': 'No ML'
})
vvc(df, "Q15", "number of experience years", "counts", title = "ML engineers by ML methods usage experience years")
```
![g15](https://i.imgur.com/D2ySppt.png)
```
vvc(df, "Q20", "Company size", "Number of engineers employed", title = "ML engineers distribution by their company size")
```
![g20](https://i.imgur.com/vFzp9cc.png)
```
cavo(df, gcbp(df, "Q23"),xlabel= 'Counts',ylabel= "Role description",title ="Engineers distribution by roles",horizontal=True)
```
![g23](https://i.imgur.com/BSTDow7.png)
```
vvc(df, "Q24", "salary amount", "Number of engineers", title = "ML engineers distribution by salary amount")
```
![g24](https://i.imgur.com/NqIXMHU.png)

*Insight:*

*The majority of ML engineers have 3 years or more of programming experience in general. However, the number of people with only 1-2 experience years is not small either.*

*Over half of the engineers in the survey has less than 3 years experience of using ML methods. In fact, people with only 1-2 years, or less than 1 year of experience stood first in numbers.*

*The majority of Ml engineers work in small companies and they are scattered among various roles. Their salary of on average is about $1000.*

*=> It is not impossible to become a ML engineer even with little experience using ML methods. But at least 1-2 years of programming experience is much needed to have a good career start. Even so, it might be hard to apply into a big company.*

* _**What are some tools that Ml engineers need in the near future?**_
```
cavo(df, gcbp(df, "Q28_B",), xlabel= "Number of engineers wish to use it",ylabel= "ML product", title = "ML products by upcoming adoption need",horizontal=True)
```
![g28b](https://i.imgur.com/qozo41x.png)
```
cavo(df, gcbp(df, "Q35_B",),xlabel= "Number of engineers wish to use it",ylabel= "ML experiments management tools", title = "ML experiments management tools by upcoming adoption need",horizontal=True)
```
![g35b](https://i.imgur.com/p9dtLHK.png)

*Insight:*

*Among the ML products, it seems Google Cloud Vision AI or Google Cloud ML Engine are the new trend in the sector. Additionally, there appear to be an extreme need of TensorBoard.*

*=> As it has been mentioned before, it is encouraged for Quan to learn the usage of Google Cloud ML Engine (or GG Cloud Vision AI). Especially in this fiercely competitive job market, it would help him make a difference compared to other candidates when applying. Furthermore, if he intends to work in the R&D department, then it will certainly work in his favour if he is fammiliar with TensorBoard as well.*