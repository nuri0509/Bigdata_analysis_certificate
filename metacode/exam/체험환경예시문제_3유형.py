# 출력을 원할 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

import pandas as pd

df = pd.read_csv("data/Titanic.csv")

# 사용자 코딩

# 해당 화면에서는 제출하지 않으며, 문제 풀이 후 답안제출에서 결괏값 제출


table = pd.crosstab(df['Gender'],df['Survived'])

from scipy.stats import chi2_contingency

statistics, pvalue, ddof, expected = chi2_contingency(table)

print(statistics, pvalue, ddof, expected)
df['Gender'] = df['Gender'].map({'female':0,'male':1})
df.head(10)
x = df[['Gender','SibSp','Parch','Fare']]
y = df['Survived']
print(x)
import statsmodels.api as sm

x = sm.add_constant(x)
model = sm.Logit(y,x).fit()
summary = model.summary()
print(summary)

import numpy as np

coef = -0.3539
odds_ratio = np.exp(coef)
print(odds_ratio)

