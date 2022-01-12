```python
import pandas as pd
```


```python
df=pd.read_excel(r'C:\Users\ankit.kumar.kothari\Desktop\step2successs-20210731T082503Z-001\step2successs\Training5\team_members.xlsx')
```


```python
df.shape
```




    (83, 6)




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 83 entries, 0 to 82
    Data columns (total 6 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   S.No.       83 non-null     int64  
     1   name        83 non-null     object 
     2   team        83 non-null     object 
     3   email       83 non-null     object 
     4   Unnamed: 4  0 non-null      float64
     5   Unnamed: 5  0 non-null      float64
    dtypes: float64(2), int64(1), object(3)
    memory usage: 4.0+ KB
    


```python
df.columns
```




    Index(['S.No.', 'name', 'team', 'email', 'Unnamed: 4', 'Unnamed: 5'], dtype='object')




```python
df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>S.No.</th>
      <th>name</th>
      <th>team</th>
      <th>email</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Ankit kothari</td>
      <td>Reactive</td>
      <td>abhishek.jha@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Atul bajaj</td>
      <td>Reactive</td>
      <td>ankur1.gupta@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Chirag</td>
      <td>Proactive</td>
      <td>anuj.kumar@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>S.No.</th>
      <th>name</th>
      <th>team</th>
      <th>email</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>80</th>
      <td>80</td>
      <td>Malviya Saurabh</td>
      <td>Voice</td>
      <td>saurabh.malviya.ext@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>81</th>
      <td>81</td>
      <td>Sachin Kumar</td>
      <td>Voice</td>
      <td>sachin2.kumar.ext@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>82</th>
      <td>82</td>
      <td>Kumar Sachin</td>
      <td>Voice</td>
      <td>sachin2.kumar.ext@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['name','team']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ankit kothari</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Atul bajaj</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Chirag</td>
      <td>Proactive</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Dagar Arun</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rawat Arvind</td>
      <td>IPE</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>78</th>
      <td>Sharma Kapil</td>
      <td>Voice</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Saurabh Malviya</td>
      <td>Voice</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Malviya Saurabh</td>
      <td>Voice</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Sachin Kumar</td>
      <td>Voice</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Kumar Sachin</td>
      <td>Voice</td>
    </tr>
  </tbody>
</table>
<p>83 rows × 2 columns</p>
</div>




```python
df.iloc[[0]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>S.No.</th>
      <th>name</th>
      <th>team</th>
      <th>email</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Ankit kothari</td>
      <td>Reactive</td>
      <td>abhishek.jha@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>S.No.</th>
      <th>name</th>
      <th>team</th>
      <th>email</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Ankit kothari</td>
      <td>Reactive</td>
      <td>abhishek.jha@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Atul bajaj</td>
      <td>Reactive</td>
      <td>ankur1.gupta@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Chirag</td>
      <td>Proactive</td>
      <td>anuj.kumar@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Dagar Arun</td>
      <td>Reactive</td>
      <td>arunk.dagar@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Rawat Arvind</td>
      <td>IPE</td>
      <td>arvind.rawat@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>78</th>
      <td>78</td>
      <td>Sharma Kapil</td>
      <td>Voice</td>
      <td>kapil.sharma@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>79</th>
      <td>79</td>
      <td>Saurabh Malviya</td>
      <td>Voice</td>
      <td>saurabh.malviya.ext@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>80</th>
      <td>80</td>
      <td>Malviya Saurabh</td>
      <td>Voice</td>
      <td>saurabh.malviya.ext@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>81</th>
      <td>81</td>
      <td>Sachin Kumar</td>
      <td>Voice</td>
      <td>sachin2.kumar.ext@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>82</th>
      <td>82</td>
      <td>Kumar Sachin</td>
      <td>Voice</td>
      <td>sachin2.kumar.ext@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>83 rows × 6 columns</p>
</div>




```python
a=df[df['team']=='Reactive']
a
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>S.No.</th>
      <th>name</th>
      <th>team</th>
      <th>email</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Reactive</th>
      <th>Reactive</th>
      <th>Proactive</th>
      <th>Reactive</th>
      <th>...</th>
      <th>Voice</th>
      <th>Voice</th>
      <th>Voice</th>
      <th>Voice</th>
      <th>Voice</th>
      <th>Voice</th>
      <th>Voice</th>
      <th>Voice</th>
      <th>Voice</th>
      <th>Voice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Ankit kothari</td>
      <td>Reactive</td>
      <td>abhishek.jha@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Atul bajaj</td>
      <td>Reactive</td>
      <td>ankur1.gupta@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Dagar Arun</td>
      <td>Reactive</td>
      <td>arunk.dagar@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Bagalay Bhupender</td>
      <td>Reactive</td>
      <td>bhupender.bagalay@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Pandey Gaurav</td>
      <td>Reactive</td>
      <td>gaurav1.pandey.ext@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Sharma Himanshu</td>
      <td>Reactive</td>
      <td>himanshu.sharma@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>Shiraz Mohamad</td>
      <td>Reactive</td>
      <td>shiraz.nasir@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>Singh Naveen</td>
      <td>Reactive</td>
      <td>naveen.singh@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>Gupta Prashantg</td>
      <td>Reactive</td>
      <td>prashantg.gupta@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>Khurana Prashant</td>
      <td>Reactive</td>
      <td>prashant.khurana@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>Sinha Rachna</td>
      <td>Reactive</td>
      <td>rachna.sinha.ext@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>Yadav Rajesh</td>
      <td>Reactive</td>
      <td>rajeshy.yadav@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>Verma Ravi</td>
      <td>Reactive</td>
      <td>ravi.verma@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>Chaurasia Swati</td>
      <td>Reactive</td>
      <td>swati.chaurasia@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
      <td>Kumar Vikash</td>
      <td>Reactive</td>
      <td>vikash1.kumar@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>Bhatia Vivek</td>
      <td>Reactive</td>
      <td>vivek.bhatia@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
      <td>Ravi Verma</td>
      <td>Reactive</td>
      <td>ravi.verma@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>Abhishek Jha</td>
      <td>Reactive</td>
      <td>abhishek.jha@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>Ankur Gupta</td>
      <td>Reactive</td>
      <td>ankur1.gupta@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39</td>
      <td>Arun Dagar</td>
      <td>Reactive</td>
      <td>arunk.dagar@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43</td>
      <td>Bhupender Bagalay</td>
      <td>Reactive</td>
      <td>bhupender.bagalay@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>Gaurav Pandey</td>
      <td>Reactive</td>
      <td>gaurav1.pandey.ext@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46</td>
      <td>Himanshu Sharma</td>
      <td>Reactive</td>
      <td>konark.sharma.ext@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50</td>
      <td>Mohamad Shiraz</td>
      <td>Reactive</td>
      <td>naveen.singh@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>50</th>
      <td>51</td>
      <td>Naveen Singh</td>
      <td>Reactive</td>
      <td>pankaj.phartiyal@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>52</th>
      <td>53</td>
      <td>Prashant Gupta</td>
      <td>Reactive</td>
      <td>prashant.khurana@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>53</th>
      <td>54</td>
      <td>Prashant Khurana</td>
      <td>Reactive</td>
      <td>shiraz.nasir@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>54</th>
      <td>55</td>
      <td>Rachna Sinha</td>
      <td>Reactive</td>
      <td>rachna.sinha.ext@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>56</th>
      <td>57</td>
      <td>Rajesh Yadav</td>
      <td>Reactive</td>
      <td>rajeshy.yadav@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>63</th>
      <td>64</td>
      <td>Swati Chaurasia</td>
      <td>Reactive</td>
      <td>swati.chaurasia@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>65</th>
      <td>66</td>
      <td>Vikash Kumar</td>
      <td>Reactive</td>
      <td>vikash1.kumar@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>67</th>
      <td>68</td>
      <td>Vivek Bhatia</td>
      <td>Reactive</td>
      <td>vivek.bhatia@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
    <tr>
      <th>68</th>
      <td>23</td>
      <td>Ravi verma</td>
      <td>Reactive</td>
      <td>ravi.verma@orange.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>...</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
      <td>Reactive</td>
    </tr>
  </tbody>
</table>
<p>33 rows × 89 columns</p>
</div>




```python

```
