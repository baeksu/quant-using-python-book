import pandas as pd

dict_data = {'a' : 1, 'b' : 2, 'c' : 3}
series = pd.Series(dict_data)
print(series)
print(type(series))
print(series.values)
print(series.index)


list_data = [1,2,3]
series2 = pd.Series(list_data, index = ['index1', 'index2' , 'index3'])
print("===================series2=================== ")
print( series2['index1']) # 키값으로 값에 접근 가능 
print( series2[0:3]) # 범위로도 값에 접근할 수 있다


print("===================data frame=================== ")


