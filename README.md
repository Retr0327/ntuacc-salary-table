# **NTUACC Salary Table**
Downloading the project details as a table from the website [National Taiwan University Accounting (NTUACC)](https://ntuacc.cc.ntu.edu.tw/acc/) system. 

>Note: In order to use this project, you need to be the project assistant of your organization


## **Documentation**

### 1. Import the package.

``` python
from ntuacc import NTUACC
``` 
 
### 2. Fill in and instantiate `NTUACC` class: 
* `bossid`: the id/account of your professor, doctoral advisor or boss
* `assid`: the id/account of project assistant 
* `asspwd`: the password of project assistant 
* `project_year`: the project year you want to download

``` python
salary_table = NTUACC("xxx", 'xxx', 'xxx', project_year=2021)
```

### 3. Download the table: 
Download the table by using the `.download_table()` method:
```python
salary_table.download_table()
```
This prints:
| 黏存單號碼 |  計畫代碼 |計畫名稱 | 計畫費用別 | 金額 | 申請日期 | 報帳類別  | 受款人 | 發票號碼	 |入帳日期|
|----|----|----|----|----|----|----|----|----|----|
| 110xxxx | xxx | xxx | 其他費用 | 100 | 1100801 | 計畫經費 | xxx | AB12345078 | 20210826 |
| ... | ...| ...| ...| ...| ...| ...| ...| ... | ... |

### 4. Download the table as CSV: 
Download the table as a CSV file by calling the `.to_csv()` method:
```python
salary_table.to_csv()
```

### 5. Download the table as Pickle: 
Download the table as a CSV file by calling the `.to_pickle()` method:
```python
salary_table.to_pickle()
```

## Contact Me
If you have any suggestion or question, please do not hesitate to email me at r07142010@g.ntu.edu.tw
