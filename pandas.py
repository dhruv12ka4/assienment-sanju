import pandas as pd
import numpy as np
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
Import the dataset from this(https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user).
Use sep= "|" while reading the data

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
Assign it to a variable called users and use the 'user_id' as index
users = pd.read_table(url, sep='|', index_col='user_id')
users

age	gender	occupation	zip_code
user_id				
1	24	M	technician	85711
2	53	F	other	94043
3	23	M	writer	32067
4	24	M	technician	43537
5	33	F	other	15213
...	...	...	...	...
939	26	F	student	33319
940	32	M	administrator	02215
941	20	M	student	97229
942	48	F	librarian	78209
943	22	M	student	77841
943 rows × 4 columns

See the first 10 and last 10 entries

print("--------First 10 entries -------\n",users.head(10))
print("--------Last 10 entries -------\n",users.tail(10))

--------First 10 entries -------
          age gender     occupation zip_code
user_id                                    
1         24      M     technician    85711
2         53      F          other    94043
3         23      M         writer    32067
4         24      M     technician    43537
5         33      F          other    15213
6         42      M      executive    98101
7         57      M  administrator    91344
8         36      M  administrator    05201
9         29      M        student    01002
10        53      M         lawyer    90703
--------Last 10 entries -------
          age gender     occupation zip_code
user_id                                    
934       61      M       engineer    22902
935       42      M         doctor    66221
936       24      M          other    32789
937       48      M       educator    98072
938       38      F     technician    55038
939       26      F        student    33319
940       32      M  administrator    02215
941       20      M        student    97229
942       48      F      librarian    78209
943       22      M        student    77841


What is the number of observations in the dataset?

print("Number of Observations :  ",users.shape[0])
Number of Observations :   943

What is the number of columns in the dataset?

print("Number of Columns :  ",users.shape[1])
Number of Columns :   4

Print the name of all the columns.

users.columns
Index(['age', 'gender', 'occupation', 'zip_code'], dtype='object')

How is the dataset indexed?

users.index
Int64Index([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,
            ...
            934, 935, 936, 937, 938, 939, 940, 941, 942, 943],
           dtype='int64', name='user_id', length=943)

What is the data type of each column?

users.dtypes
age            int64
gender        object
occupation    object
zip_code      object
dtype: object

Print only the occupation column

users["occupation"]
user_id
1         technician
2              other
3             writer
4         technician
5              other
           ...      
939          student
940    administrator
941          student
942        librarian
943          student
Name: occupation, Length: 943, dtype: object

How many different occupations are in this dataset?

users["occupation"].value_counts().count()
21

What is the most frequent occupation?

users["occupation"].value_counts().sort_values(ascending=False).head()
student          196
other            105
educator          95
administrator     79
engineer          67
Name: occupation, dtype: int64

DataFrame Info.

users.info(verbose=True)
<class 'pandas.core.frame.DataFrame'>
Int64Index: 943 entries, 1 to 943
Data columns (total 4 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   age         943 non-null    int64 
 1   gender      943 non-null    object
 2   occupation  943 non-null    object
 3   zip_code    943 non-null    object
dtypes: int64(1), object(3)
memory usage: 36.8+ KB

Describe all the columns

users.describe(include="all")

age	gender	occupation	zip_code
count	943.000000	943	943	943
unique	NaN	2	21	795
top	NaN	M	student	55414
freq	NaN	670	196	9
mean	34.051962	NaN	NaN	NaN
std	12.192740	NaN	NaN	NaN
min	7.000000	NaN	NaN	NaN
25%	25.000000	NaN	NaN	NaN
50%	31.000000	NaN	NaN	NaN
75%	43.000000	NaN	NaN	NaN
max	73.000000	NaN	NaN	NaN

Summarize only the occupation column

print(users.occupation.describe())
print(users.occupation.value_counts())

count         943
unique         21
top       student
freq          196
Name: occupation, dtype: object
student          196
other            105
educator          95
administrator     79
engineer          67
programmer        66
librarian         51
writer            45
executive         32
scientist         31
artist            28
technician        27
marketing         26
entertainment     18
healthcare        16
retired           14
lawyer            12
salesman          12
none               9
homemaker          7
doctor             7
Name: occupation, dtype: int64

What is the mean age of users?

users.age.mean()
34.05196182396607

What is the age with least occurrence?

users.age.value_counts().tail()
7     1
66    1
11    1
10    1
73    1
Name: age, dtype: int64


