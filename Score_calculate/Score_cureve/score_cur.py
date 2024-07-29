import matplotlib.pyplot as plt

data = []
with open("新學生成績.csv") as infile:
    text = infile.read().split()
    captions = text[0].split(',')       #title
    for e in text[1:]:                 #not include title
        stu = e.split(',')
        scores = [int(sc) for sc in stu[1:0]]
        data.append([stu[0]]+scores)

#class average
avg = []
for i in range(1,len(data[0])):               #0為student name
    all_scores = [data[stu][i] for stu in range(len(data))]
    avg.append(sum(all_scores)/len(all_scores))


for stu in data:
    name = stu[0]
    scores = stu[1:]
    plt.clf()
    plt.plot(scores, marker='o', label = "Your Score")
    plt.plot(avg, marker='x', label = "Class Average")
    plt.legend()
    plt.title(name)
    plt.xticks(range(len(scores)), captions[1:])
    plt.xlabel('Items')
    plt.ylabel('Scores')
    plt.ylim(0, 110)
    plt.tigh_layout()
    plt.savefig(name+'.png')
    #plt.show()