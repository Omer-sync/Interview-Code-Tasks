import matplotlib
import matplotlib.pyplot as plt
import numpy as np



labels = ["Work","Family","Homeworks","Individual","Socializing","Spare Time","Sleep"]
Charles = [8.5,0.5,3.0,1.0,1.5,3.0,6.5]
Henry = [9.5,1.0,2.0,1.5,0.5,2.5,7.0]
Susan = [7.0,1.5,1.0,2.5,2.0,2.0,8.0]

x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, Charles, width, label='Charles')
rects2 = ax.bar(x , Henry, width, label='Henry')
rects3 = ax.bar(x + width, Susan, width, label='Susan')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Hours')
ax.set_title('Daily Activities')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()

plt.show()