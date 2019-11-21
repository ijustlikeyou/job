import pandas as pd

# 第6节课的课后作业
# 数据集保存及读取
# 添加编号列，并将数据集写入到machine_learning.csv文件，使用pandas读取验证文件是否有效(无错即可)。
# 添加一条记录，青绿 硬挺 浊响 稍糊 平坦 硬滑 0.666 0.111 好
# 再使用普通文件读取将数据集读取出来，列名读取到columns，数据(带编号)读取到datalist
# 在所有数据中过滤出色泽='浅白'的数据
# 在所有数据中过滤出密度大于0.5的数据
dataSet = \
    """色泽 根蒂 敲声 纹理 脐部 触感 密度 含糖率 好瓜
       青绿 蜷缩 浊响 清晰 凹陷 硬滑 0.697 0.460 是
       乌黑 蜷缩 沉闷 清晰 凹陷 硬滑 0.774 0.376 是
       乌黑 蜷缩 浊响 清晰 凹陷 硬滑 0.634 0.264 是
       青绿 蜷缩 沉闷 清晰 凹陷 硬滑 0.608 0.318 是
       浅白 蜷缩 浊响 清晰 凹陷 硬滑 0.556 0.215 是
       青绿 稍蜷 浊响 清晰 稍凹 软粘 0.403 0.237 是
       乌黑 稍蜷 浊响 稍糊 稍凹 软粘 0.481 0.149 是
       乌黑 稍蜷 浊响 清晰 稍凹 硬滑 0.437 0.211 是
       乌黑 稍蜷 沉闷 稍糊 稍凹 硬滑 0.666 0.091 否
       青绿 硬挺 清脆 清晰 平坦 软粘 0.243 0.267 否
       浅白 硬挺 清脆 模糊 平坦 硬滑 0.245 0.057 否
       浅白 蜷缩 浊响 模糊 平坦 软粘 0.343 0.099 否
       青绿 稍蜷 浊响 稍糊 凹陷 硬滑 0.639 0.161 否
       浅白 稍蜷 沉闷 稍糊 凹陷 硬滑 0.657 0.198 否
       乌黑 稍蜷 浊响 清晰 稍凹 软粘 0.360 0.370 否
       浅白 蜷缩 浊响 模糊 平坦 硬滑 0.593 0.042 否
       青绿 蜷缩 沉闷 稍糊 稍凹 硬滑 0.719 0.103 否"""


# 进行数据处理添加编号列并转为二维list 如果type为true则添加编号列
def getListData(listData, index=9, type=False):
    list1, list2, count = list(), ["编号"] if type else list(), 1
    for i in range(len(listData)):
        if (i + 1) % index == 0:
            list2.append(listData[i])
            list1.append(map(str, list2[:]))
            list2 = list()
        elif type and i >= index and (i + 1) % index == 1:
            list2.append(count)
            list2.append(listData[i])
            count += 1
        else:
            list2.append(listData[i])
    return list1


# 将数据转为String
def listToStr(data):
    returnStr = ""
    for i in data:
        for x in i:
            returnStr += str(x) + " "
        returnStr += "\n"
    return returnStr


# 将数据写入文件
def writeFile(path, data):
    myFile = open(path, 'w+', encoding='utf-8')
    myFile.write(data)
    myFile.close()


# 将字符串list转为list集合并过滤编号列表
def strListToList(data, delIndex=0, type=True):
    for i in range(len(data)):
        data[i] = data[i].split()
        if type:
            del data[i][delIndex]
    return data


# write into a file
# your code here
file = r'C:\machine_learning.csv'  # file path, you can change the direction
writeFile(file, listToStr(getListData(dataSet.split(), type=False)))

# add a new data
# your code here
# 添加的数据
addData = ['青绿', '硬挺', '浊响', '稍糊', '平坦', '硬滑', '0.666', '0.111', '好']
fileList = open(file, encoding='utf-8').readlines()
fileList.append(' '.join(addData) + "\n")
writeFile(file, listToStr(getListData(' '.join(fileList).split(), type=True)))

# vertify
df = pd.read_csv(file)
print(df.head())

# read file
# your code here
fileList = open(file, encoding='utf-8').readlines()

columns = fileList[0].split()
datalist = strListToList(fileList[1:])

# vertify
print(columns == ['编号', '色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖率', '好瓜'])
print(datalist[-1] == ['青绿', '硬挺', '浊响', '稍糊', '平坦', '硬滑', '0.666', '0.111', '好'])


# your code here

def isEmpty(obj):
    return float(obj[6]) > 0.5


# 过滤数据
# 在所有数据中过滤出色泽='浅白'的数据
print(list(filter(lambda data: data.count('浅白') > 0, datalist)))

# 在所有数据中过滤出密度大于0.5的数据

print(list(filter(isEmpty, datalist)))
