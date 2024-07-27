import csv
from collections import Counter

with open("中華職棒球員打擊數據.csv") as infile:
    data = list(csv.DictReader(infile))           #字典方式儲存
    results = []                                  #存放達成紀錄的球員
    for e in data:
        if e["全壘打"] > 10 and e["盜壘"] > 10:     #條件: 全壘打+盜壘都大於10
            results.append(e)

counts = Counter(e["姓名"] for e in results)       #統計達成紀錄的球員，如("張泰山", 5)
print(f"共有{len(counts)}人有此成就")
for r,p in enumerate(counts.most_common(3)):      #取前三
    name, times = p[0], p[1]
    print(f"第{r+1}名{name}紀錄達成{times}次")
    for e in results:
        if e["姓名"] == name:
            print(name, e['年度'], e["全壘打"], e["盜壘"])
