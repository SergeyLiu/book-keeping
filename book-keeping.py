import datetime
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

#   日期
date = str(datetime.date.today())
dateArray = date.strip().split('-')
year = int(dateArray[0])
month = int(dateArray[1])
day = int(dateArray[2])
print("当前日期为%d年%d月%d日" % (year, month, day))

#   实现功能1：记录当天花销
def function1():
    print("记录当日花销")
    breakfast = float(input("早餐花销："))
    lunch = float(input("午餐花销："))
    dinner = float(input("晚餐花销："))
    snacks = float(input("零食花销："))
    need = float(input("必需品花销："))
    others = float(input("其他花销："))
    total = breakfast + lunch + dinner + snacks + need + others
    print("当天餐饮花费%.2f元，其他花费%.2f元" % (breakfast + lunch + dinner + snacks, need + others))

    #确定文件路径
    filename = str(year) + "expenses.csv"

    #判定对应路径文件是否存在，若存在则直接读取重写，不存在则创建新文件并初始化
    if os.path.exists(filename):
        #文件已存在，直接读取
        expensesFrame = pd.read_csv(filename, index_col = 0)
    else:
        #文件不存在
        #初始化DataFrame
        zerosArr = np.zeros((12, 31))
        months = []
        for i in range(12):
            months.append(i + 1)
        days = []
        for i in range(31):
            days.append(i + 1)
        expensesFrame = pd.DataFrame(zerosArr, index=months, columns=days)

    #读取结束
    #将当天花销写入文件
    expensesFrame.at[month, str(day)] = total
    expensesFrame.to_csv(filename, sep=',', header=True, index=True)

#   实现功能2：查询具体某天花销
def function2():
    print("查询具体某天花销")
    dateQuery = input("请输入想要查询的日期（格式：year-month-day，例如：2020-9-8）：")
    dateArr = dateQuery.strip().split('-')
    #文件名
    filename = str(year) + "expenses.csv"
    if not os.path.exists(filename):
        #无对应文件记录
        print("该年尚未记账")
    else:
        expensesFrame = pd.read_csv(filename, index_col = 0)
        print(dateQuery + "：" + str(expensesFrame.at[int(dateArr[1]), dateArr[2]]))

#   实现功能3：查询自当月记账日起总花销与平均每日花销
def function3():
    print("查询当月自记账日起总花销与平均每日花销")
    expensesFrame = pd.read_csv(str(year) + "expenses.csv", index_col=0)
    monthExp = np.array(expensesFrame)[month-1].tolist()
    countExp = []
    count = 0
    Index = []
    for i in range(31):
        if monthExp[i] != 0.:
            countExp.append(monthExp[i])
            Index.append(i)
            count += 1
    totalExp = np.sum(countExp)
    if count == 0:
        print("当月无记账记录")
    else:
        print("自" + str(Index[0]+1) + "号起，共记账" + str(count) + "天，总花销" + str(totalExp) + "元，平均每天" + str(totalExp/count) + "元")


#   实现功能4：可视化本月每日花销
def function4():
    print("可视化本月每日花销")
    expensesFrame = pd.read_csv(str(year) + "expenses.csv", index_col=0)
    monthExp = np.array(expensesFrame)[month - 1].tolist()
    Index = list(range(1, 32))
    plt.plot(Index, monthExp)
    plt.xlabel("日期/号")
    plt.ylabel("开销/元")
    for i in range(len(Index)):
        plt.text(Index[i], monthExp[i], monthExp[i], color='b')
    plt.show()

#   实现功能5：可视化本年每月花销
def function5():
    print("可视化本年每月花销")
    expensesFrame = pd.read_csv(str(year) + "expenses.csv", index_col=0)
    expArr = np.array(expensesFrame)
    yearExp = np.sum(expArr, axis=1)
    Index = list(range(1, 13))
    plt.plot(Index, yearExp)
    plt.xlabel("日期/号")
    plt.ylabel("开销/元")
    for i in range(len(Index)):
        plt.text(Index[i], yearExp[i], yearExp[i], color='b')
    plt.show()
choices = {
    1:function1,
    2:function2,
    3:function3,
    4:function4,
    5:function5
}

while(True):
    print("功能菜单")
    print("1、记录当日花销")
    print("2、查询具体某天花销")
    print("3、查询自当月记账日起总花销与平均每日花销")
    print("4、可视化本月每日花销")
    print("5、可视化本年每月花销")
    print("0、退出")
    choose = int(input("请输入对应功能编号："))

    if choose == 0:
        break
    else:
        choices.get(choose)()
        contiue = input("键入0退出，否则继续")
        if contiue == '0':
            break














