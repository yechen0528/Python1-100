import pyreadstat

# 使用pyreadstat的read_sav函数读取.sav文件
data, meta = pyreadstat.read_sav('BDE1D25A000000000000000000000000.sav')

# 打印数据的前几行
print(data.head())