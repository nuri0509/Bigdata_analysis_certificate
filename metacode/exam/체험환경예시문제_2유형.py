
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
# 1.데이터 탐색(EDA)
print(train.head(10))
print(test.head(10))

print(train.shape)
print(test.shape)

print(train.info())
print(test.info())

#2-1. 결측치 처리

print(train.isnull().sum())
print(test.isnull().sum())

train = train.drop(columns=['회원ID'])
test = test.drop(columns=['회원ID'])


train['환불금액'] = train['환불금액'].fillna(0)
test['환불금액'] = test['환불금액'].fillna(0)

# #2-1. 이상치 처리


# 2-3.변수처리
print(train.corr())

print(train.shape)
print(test.shape)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
train['주구매지점'] = le.fit_transform(train['주구매지점'])
test['주구매지점'] = le.transform(test['주구매지점'])

train['주구매상품'] = le.fit_transform(train['주구매상품'])
test['주구매상품'] = le.transform(test['주구매상품'])



x = train.drop(columns='성별')
y = train['성별']


from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(x,y,test_size = 0.2, stratify = y, random_state=2024)

print(x_train.shape)
print(y_train.shape)
print(x_val.shape)
print(y_val.shape)


from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=100, max_depth=10,random_state=2024)

model = rfc.fit(x_train, y_train)
pred = model.predict(x_val)
pred_proba = model.predict_proba(x_val)


from sklearn.metrics import accuracy_score
acc= accuracy_score(y_val, pred)
print(acc)

pred2 = model.predict(test)
print(pred2)
result = pd.DataFrame({'pred':pred2}).to_csv('result.csv', index = False)
result = pd.read_csv('result.csv')
print(result)