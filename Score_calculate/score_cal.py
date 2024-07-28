result = []

with open("學生成績.csv") as infile:
    data = infile.read().split()
    for e in data[1:]:                          #不含title
        stu = e.split(',')                      #每個人資料用','分開
        scores = [int(sc) for sc in stu[1:]]    #stu[0] = name
        exams = scores[3]*0.2 + scores[4]*0.3   
        hw = sum(sorted(scores[0:3])[1:])/2     #取作業分數高的兩個
        final = round(hw*0.5 + exams, 2)
        print(f"{stu[0]}{scores}作業平均{hw}總分{final}")
        stu.append(final)
        result.append(stu)

with open("新學生成績.csv", 'w') as outfile:
    outfile.write(data[0]+",總成績\n")          #在title多加一column'總成績'
    for stu in result:
        outfile.write(','.join([str[e] for e in stu])+'\n')