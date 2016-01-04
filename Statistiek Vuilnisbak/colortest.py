import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

a=np.random.random(400)
#print a
cs=cm.Set1(np.arange(40000)/40000)
print cs
fig, ax = plt.subplots()
p=plt.pie(a, colors=cs)
plt.show()
