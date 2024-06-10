
import pandas as pd

#데이터 생성
purchase = pd.DataFrame({'purchase':[540,370,310,120]},
                        index=['laptop','TV','air conditioner','refrigerator'])

non_purchase = pd.DataFrame({'non_purchase':[160,230,490,380]},
                        index=['laptop','TV','air conditioner','refrigerator'])

df = pd.concat([purchase, non_purchase], axis=1)  #열 기준으로 데이터 합치기

print(df)

#카이제곱 동질성 검정
from scipy.stats import chi2_contingency
chi2, p_val, dof, exp = chi2_contingency(df)
print('chi2_stats:', chi2)
print('p_value:', p_val)
