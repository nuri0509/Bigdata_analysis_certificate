# (체험) 제 3유형 (풀이용)

# 제공된 데이터(bcc.csv)는 암환자와 정상인의 리지스틴 수치에 대한 자료이며,
# 두집단의 로그 리지스틴 값에 차이가 있는지를 검정하려고 한다.
# 소문항별로 답을 구한 후, 구한 답을 제시된 [제출형식]에 맞춰 답안 제출 페이지에 입력하시오.
# (단, 모델은 절편항을 포함한다.)
# 
# 1) 두 집단의 로그 리지스틴 값의 분산에 차이가 있는지를 알아보기 위해
# F-검정을 수행할 때, 검정 통계량의 값을 구하여라.(단, 분자의 자유도가 분모의 자유도 보다 크도록 하여라.)
# (반올림하여 소수 셋째 자리까지 작성)
# 
# 2) 두 집단의 로그 리지스틴 값에 대한 합동 분산 추정량을 구하여라.
# (반올림하여 소수 셋째 자리까지 작성)
# 
# 3) 2)번 문제에서 구한 합동 분산 추정량을 이용하여 두 집단의 로그 리지스틴 값에 유의미한 차이가 있는지
# 독립표본 t-검정을 수행하고 p-값을 구하여라.
# 반올림하여 소수 셋째 자리까지 작성

#-------------------------------------------------------------

# 출력을 원할 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

import pandas as pd
import numpy as np

df = pd.read_csv("data/bcc.csv")

# 사용자 코딩

# 해당 화면에서는 제출하지 않으며, 문제 풀이 후 답안제출에서 결괏값 제출

import scipy.stats as stats

# print(df.head())

group1 = df[df['Classification'] == 1]
group2 = df[df['Classification'] == 2]

print(group1)
print(group2)

print(group1.shape)     # 각 그룹의 크기 확인 (group1 : 52행, group2 : 64행)
print(group2.shape)     

statistics, pvalue = stats.bartlett(group2['Resistin'], group1['Resistin'])
                                 # 분자의 자유도가 분모의 자유도보다 크게 설정 (표본크기 중심)
print(statistics)
print(pvalue)

# group1_values = group1['Resistin']
# group2_values = group2['Resistin']

# n1 = len(group1_values)
# n2 = len(group2_values)

# s1_squared = np.var(group1_values, ddof=1)   # 표본분산(ddof=1 설정)
# s2_squared = np.var(group2_values, ddof=1) 

# F_statistic = s2_squared / s1_squared
# df1, df2 = n2 - 1, n1 - 1

# p_value = stats.f.sf(F_statistic, df1, df2) * 2

# print("F-statistic:", F_statistic)
# print("p-value:", p_value)


# 합동 분산 추정량 계산
sp_squared = ((n1 - 1) * s1_squared + (n2 - 1) * s2_squared) / (n1 + n2 - 2)

print(sp_squared)

# 표본 평균 구하기
mean1 = np.mean(group1_values)
mean2 = np.mean(group2_values)

# 합동 분산 추정량을 이용하여 독립 표본 t검정 수행
t_statistics = (mean1 - mean2) / np.sqrt(sp_squared * (1/n1 + 1/n2))

p_value = stats.t.sf(abs(t_statistics), df=n1+n2-2) * 2

print(t_statistics)
print(p_value)
