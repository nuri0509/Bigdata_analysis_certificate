import pandas as pd

#데이터 로드
df = pd.read_csv('https://raw.githubusercontent.com/JEunJin/BigData_python/master/bigdata_csvfile/cardiovascular_heart_disease_data.csv', delimiter=';')
print(type(df))
print(df.head())

#다중 선형 회귀 분석
import statsmodels.api as sm

X =sm.add_constant(df[['weight','cholesterol','smoke']])
model = sm.OLS(df['cardio'], X)
result = model.fit()

#다중 선형 회쉬 분석 결과 출력
print(result.summary())
print(round(result.params['cholesterol'],3)) #콜레스테롤 회귀계수