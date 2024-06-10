import pandas as pd

#데이터 생성
real_data =[90,72,43,52,88]
exp = int(sum(real_data)/len(real_data))
print(exp)

expected = [69,69,69,69,69]

#카이제곱 적합도 검정
from scipy.stats import chisquare
chi, p_val = chisquare(real_data, expected)  #real_data : 관측빈도, expected : 기대빈도
print('chi:', chi)
print('p_value:', p_val)
