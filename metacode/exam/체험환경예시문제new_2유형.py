# 출력을 원하실 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

import pandas as pd

train = pd.read_csv("data/customer_train.csv")
test = pd.read_csv("data/customer_test.csv")

# 사용자 코딩

# 답안 제출 참고
# 아래 코드는 예시이며 변수명 등 개인별로 변경하여 활용
# pd.DataFrame변수.to_csv("result.csv", index=False)

print(train.head(10))
print(test.head(10))

print(train.shape)
print(test.shape)

print(train.info())
print(test.info())

train = train.drop(columns=['환불금액','주구매상품','주구매지점'])
test = test.drop(columns=['환불금액','주구매상품','주구매지점'])

train = train.set_index('회원ID')
test = test.set_index('회원ID')

print(train.head())
print(test.head())




x = train.drop(columns='총구매액')
y = train['총구매액']

from sklearn.model_selection import train_test_split

x_train, x_val, y_train, y_val = train_test_split(x, y,
																								 test_size=0.3,
																								 random_state=2025)

print(x_train.shape, y_train.shape)
print(x_val.shape, y_val.shape)

from sklearn.ensemble import RandomForestRegressor

rfc = RandomForestRegressor(random_state=2025)
rfc.fit(x_train, y_train)
pred = rfc.predict(x_val)

from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_val, pred)
rmse = mse ** 0.5

print(mse)
print(rmse)

'''
7951927624079798.0
89173581.42454411
'''

x_test = test.drop(columns='총구매액')
y_test = test['총구매액']

pred2 = rfc.predict(x_test)

mse_2 = mean_squared_error(y_test, pred2)
rmse_2 = mse_2 ** 0.5
r2_score = r2_score(y_test, pred2)

print(mse_2)     
print(rmse_2)
print(r2_score)


'''
1.0124121646755026e+16
100618694.32046425
0.6624249944124982
'''

print(pred2)

df = pd.DataFrame({'pred': pred2})
result = df.to_csv('result.csv', index=False)
print(result)