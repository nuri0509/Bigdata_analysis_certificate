'''
(체험) 제 1유형(풀이용)

제공된 데이터는 회사의 직원 연봉과 근속연수등에 관한 자료이다.
아래 수행 순서에 따라 데이터를 처리한 후, 구한 답을 소문항별로 제출형식에 맞춰 
답안 제출 페이지에 답안을 입력하시오.

(1) 고객만족도가 없는 직원의 경우, 평균 고객만족도로 결측치를 채운다.
(2) 근속연수가 없는 직원의 경우, 해당 직원을 삭제한다.
(3) 직원의 고객만족도의 4분위 중 3사분위수 값을 계산한다.
(4) 부서별로 평균연봉을 구하고, 두번째로 평균연봉이 높은 부서의 평균연봉을 계산한다.

'''

# 출력을 원할 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

import pandas as pd

df = pd.read_csv("data/employee_performance.csv")

# 사용자 코딩

# 해당 화면에서는 제출하지 않으며, 문제 풀이 후 답안제출에서 결괏값 제출

print(df.head(10))
print(df['고객만족도'].dtype)
missing_value = df['고객만족도'].mean()
print(missing_value)

df['고객만족도'] = df['고객만족도'].fillna(missing_value)
print(df.head(10))
print(df.shape)
df['근속연수'] = df['근속연수'].dropna(axis=0)
print(df.head(10))

result = df['고객만족도'].quantile(0.75) # 8
print(result)

pivot1 = pd.pivot_table(data=df,
						index='부서',
						values='연봉',
						aggfunc='mean')

print(pivot1)

result2 = pivot1.sort_values(by='연봉', ascending=False)
print(result2)
print(result2['연봉'].iloc[1])
# Marketing   108005




