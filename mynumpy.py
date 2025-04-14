from matplotlib import pyplot as plt
from numpy import random
import seaborn as sns

ran=random.randint(100, size=(3))
sns.displot(ran)
plt.show()

