import matplotlib.pyplot as plt
from datasets import dataset1, dataset2, x, colors1, colors2
import pylab

aver_colors = []
for i in range(len(colors1)):
    aver_colors.append(max(colors1[i], colors2[i]) - min(colors1[i], colors2[i]))
    
print('Среднее отклонение в количестве цветов:', sum(aver_colors) / len(aver_colors))

pylab.subplot(2, 1, 1)
pylab.plot(x, dataset1, label='First alg', color='blue')
pylab.plot(x, dataset2, label='Second alg', color='orange')
pylab.legend()

pylab.subplot(2, 1, 2)
pylab.plot(x, colors1, label='First alg', color='red')
pylab.plot(x, colors2, label='Second alg', color='blue')
#pylab.plot(x,aver_colors, label='Average', color='green')
pylab.legend()

pylab.show()