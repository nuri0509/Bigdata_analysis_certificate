import pandas as pd

#데이터 로드
df = pd.read_csv('https://raw.githubusercontent.com/JEunJin/BigData_python/master/bigdata_csvfile/wine_data.csv')
df=df.iloc[:100,:]
df.rename(columns={'class':'type'}, inplace=True) #칼럼명이 class이면 혼동될수있으므로 칼럼명 변경
print(df.info())

#로지스틱 회귀분석
from statsmodels.formula.api import logit

result = logit('type ~ alcohol + ash + magnesium + hue', data=df).fit().summary()
print(result)
