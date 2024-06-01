import pandas as pd

s = pd.Series([1,2,3,4,5])
# print(s)

# 요렇게 하면 index 를 바꿀 수 있다.
# 이 행위를 통해서 기존의 default index 였던 0,1,2,3,4,5 와의 mapping 이 깨진다.
s.index = ['a', 'b','c','d','e']
# print(s)

# 데이터 프레임 - 특정 column 을 index 로 만듦
employee_infos = {
    '이름' : ['경우' , '민혁' , '강호' , '주원'],
    '나이' : [32,29,27,35],
    '성별' : ['남','남','남','남',]
}

# print(employee_infos)
# print(employee_infos['이름'])

employee_df = pd.DataFrame(employee_infos)
# print(employee_df)
# print(employee_df['나이'])
# print(employee_df.loc[0])

employee_df['근속연수'] = pd.Series([5,2,3,8])
# print(employee_df)
new_employee_df = employee_df.set_index('이름')
# print(new_employee_df)
# print(new_employee_df.loc['경우'])