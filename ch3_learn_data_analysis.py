import pandas as pd

# 3.1 시리즈 ====================================================================
dict_data = {'a' : 1, 'b' : 2, 'c' : 3}
series = pd.Series(dict_data)
print(series)
print(type(series))
print(series.values)
print(series.index)


list_data = [1,2,3]
series2 = pd.Series(list_data, index = ['index1', 'index2' , 'index3'])
print( series2['index1']) # 키값으로 값에 접근 가능 
print( series2[0:3]) # 범위로도 값에 접근할 수 있다


print("")
# 3.2 데이터 프레임 ================================================================
# Excel 과 같은 행렬이 있는 데이터

dict_data2 = {'col1' : [1,2,3] , 'col2' : [4,5,6], 'col3' : [7,8,9]}
df = pd.DataFrame(dict_data2)
print(df)

df2 = pd.DataFrame(
    [[1,2,3], [4,5,6], [7,8,9]],
    index = ['index1', 'index2', 'index3'],
    columns= ['col1','col2','col3']
)
print(df2)

# df2.index , df2.columns 로 직접 지정 및 변경할 수 있다.
df2.index = ['행1', '행2', '행3']
df2.columns = ['열1', '열2', '열3' ]
print(df2)

# 데이터를 제거해보자
# axis = 0 : 행 지울 때, axios = 1 : 열 지울 때
# inplace = True : 원본데이터 변경 여부
df2.drop('행3', axis=0, inplace=True)
print(df2)

df2.drop('열3', axis=1, inplace=True)
print(df2)

print(df2['열2'])
type(df2.loc['열'])
print(df2['열2']['행2'])

print("")

# 3.3 데이터 불러오기 및 저장하기 ================================================================
