# CodeBook for dataframe

### Respondents Sex

**Column Name:** sex

**Type:** str

**Description:** Indicate sex of respondent.

| Value | Value Label |
| :---- | :---------- |
| M     | Male        |
| F     | Female      |



### Age

**Column Name:** age

**Type:** int

**Description:** Imputed Age value collapsed above 80.

| Value   | Value Label          |
| ------- | -------------------- |
| 18 - 80 | Imputed Age 18 to 80 |



### Education Level

**Column Name:** edu

**Type:** int

**Description:** What is the highest grade or year of school you completed? 

| Value | Value Label                              |
| ----- | ---------------------------------------- |
| 1     | Never attended school or only kindergarten |
| 2     | Grades 1 through 8 (Elementary)          |
| 3     | Grades 9 through 11 (Some high school)   |
| 4     | Grade 12 or GED (High school graduate)   |
| 5     | College 1 year to 3 years                |
| 6     | College 4 years or more (College graduate) |
| 9     | Refused                                  |



### Marital Status

**Column Name:** marital 

**Type:** int

**Description:** Are you : [marital status]

| Value | Value Label                     |
| ----- | ------------------------------- |
| 1     | Married                         |
| 2     | Divorced                        |
| 3     | Widowed                         |
| 4     | Separated                       |
| 5     | Never married                   |
| 6     | A member of an unmarried couple |
| 9     | Refused                         |



### Employment Status

**Column Name:** employ

**Type:** int

**Description:**  Are you currently …?

| Value | Value Label                      |
| ----- | -------------------------------- |
| 1     | Employed for wages               |
| 2     | Self-employed                    |
| 3     | Out of work for 1 year or more   |
| 4     | Out of work for less than 1 year |
| 5     | A homemaker                      |
| 6     | A student                        |
| 7     | Retired                          |
| 8     | Unable to work                   |
| 9     | Refused                          |



### Income Level 

**Column Name:** income

**Type:** int (—>float )

**Description:** Is your annual household income from all sources: 

| Value | Value Label                   |
| ----- | ----------------------------- |
| 1     | Less than $10,000             |
| 2     | $10,000 to less than $15,000  |
| 3     | $15,000 to less than $20,000  |
| 4     | $20,000 to less than $25,000) |
| 5     | $25,000 to less than $35,000  |
| 6     | ($35,000 to less than $50,000 |
| 7     | $50,000 to less than $75,000  |
| 8     | $75,000 or more               |
| NaN   | Not Available                 |



### General Health

**Column Name:** health

**Type:** int (—>float)

**Description:** Would you say that in general your health is: 

| Value | Value Label   |
| ----- | ------------- |
| 1     | Excellent     |
| 2     | Very good     |
| 3     | Good          |
| 4     | Fair          |
| 5     | Poor          |
| NaN   | Not Available |



### Body Mass Index

**Column Name:** bmi

**Type:** float

**Description:** Body Mass Index (BMI) 

| Value        | Value Label              |
| ------------ | ------------------------ |
| 0.01 - 99.99 | weight / (height*height) |
| NaN          | Not Available            |



### Height

**Column Name:** height

**Type:** float

**Description:** Reported height in meters 

| Value       | Value Label      |
| ----------- | ---------------- |
| 0.91 - 2.44 | Height in meters |
| NaN         | Not Available    |



### Weight

**Column Name:** weight

**Type:** float

**Description:** Reported weight in kilograms 

| Value    | Value Label         |
| -------- | ------------------- |
| 23 - 295 | Weight in kilograms |
| NaN      | Not Available       |



### Exercise in Past 30 Days

**Column Name:** exercise

**Type:** bool (—>float)

**Description:** During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise? 

| Value | Value Label   |
| ----- | ------------- |
| True  | Yes           |
| False | No            |
| NaN   | Not Available |



###  Work Hour per week

**Column Name:** workhour

**Type:** float

**Description:** Thinking about the last time you worked, about how many hours did you work per week at all of your jobs and businesses combined? 

| Value  | Value Label          |
| ------ | -------------------- |
| 0 - 96 | Hours (0-96 or more) |
| NaN    | Not Available        |



### Minutes of total exercise per week

**Column Name:** exemin

**Type:** float

**Description:** Minutes of total Physical Activity per week 

| Value     | Value Label                  |
| --------- | ---------------------------- |
| 0 - 99999 | Minutes of Activity per week |
| NaN       | Not Available                |



### Fruit Consume

**Column Name:** fruit

**Type:** bool (—>float)

**Description:** Consume Fruit 1 or more times per day 

| Value | Value Label                              |
| ----- | ---------------------------------------- |
| True  | Consumed fruit one or more times per day |
| False | Consumed fruit less than one time per day |
| NaN   | Not Available                            |



### Vegetables Consume

**Column Name:** vegetable

**Type:** bool (—>float)

**Description:** Consume Vegetables 1 or more times per day 

| Value | Value Label                              |
| ----- | ---------------------------------------- |
| True  | Consumed vegetables one or more times per day |
| False | Consumed vegetables less than one time per day |
| NaN   | Not Available                            |

