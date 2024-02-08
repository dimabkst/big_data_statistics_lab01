from traceback import print_exc
from scipy.stats import chi2, rv_continuous
import matplotlib.pyplot as plt

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

# Variant - 1
# implemented function only for continuous probability distributions
def labTask(*distributionShapeParams, n: int=800, probabilityDistribution: rv_continuous=chi2):
    sample = probabilityDistribution.rvs(*distributionShapeParams, size=n)

    drawHistogram(sample, *distributionShapeParams)


if __name__ == '__main__':
    try:
        labTask(7, probabilityDistribution=chi2, n=800)
    except Exception as e:
        print('Error occurred:')
        print_exc()
