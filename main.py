import numpy as np
import matplotlib.pyplot as plt
from traceback import print_exc
from scipy.stats import chi2, rv_continuous

def drawHistogram(data, *distributionShapeParams):
    fig, ax = plt.subplots(1, 1)

    ax.hist(data, density=True, bins='auto', histtype='stepfilled', color='g')

    ax.set_title('Гістограма вибірки')
    ax.set_xlabel('хі')
    ax.set_ylabel('Відносні частоти')
    ax.set_xlim(0)

    ax.text(15, 0.10, r'$\mathbf{{\chi}^2{(%s)}}$' % str([*distributionShapeParams])[1:-1] )

    ax.grid()

    plt.show()

def drawFigure(sample, probabilityDistribution: rv_continuous, *distributionShapeParams):
    fig = plt.figure(1, figsize=(9, 3))

    sortedSample = np.sort(sample)

    ax1 = fig.add_subplot(131)
    ax1.set_title('щільність')
    ax1.plot(sortedSample, probabilityDistribution.pdf(sortedSample, *distributionShapeParams),'r', linewidth=5.0)

    empiricalCdf = np.linspace(0, 1, len(sample))
    ax2= fig.add_subplot(132)
    ax2.set_title('функція розподілу')
    ax2.plot(sortedSample, probabilityDistribution.cdf(sortedSample, *distributionShapeParams),'r', sortedSample, empiricalCdf, 'b')
    
    ax3= fig.add_subplot(133)
    ax3.set_title('вибірка')
    ax3.scatter(np.linspace(0, len(sample), len(sample)), sample, c='black')

    plt.show()

# Variant - 1
# implemented function only for continuous probability distributions
def labTask(*distributionShapeParams, n: int=800, probabilityDistribution: rv_continuous=chi2):
    sample = probabilityDistribution.rvs(*distributionShapeParams, size=n)

    drawHistogram(sample, *distributionShapeParams)

    drawFigure(sample, probabilityDistribution, *distributionShapeParams)

    mean = np.mean(sample)

    variance = np.var(sample)

    standardDeviation = variance ** 0.5

    print(f'Основні характеристики вибірки:\nМатематичне сподівання: {mean};\nДисперсія: {variance};\nСередньоквадратичне відхилення: {standardDeviation}.')

if __name__ == '__main__':
    try:
        labTask(7, probabilityDistribution=chi2, n=800)
    except Exception as e:
        print('Error occurred:')
        print_exc()
