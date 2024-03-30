import numpy as np
import matplotlib.pyplot as plt

data = {i : np.random.randn() for i in range (7)}

print(data)

plt.plot(np.random.randn(50).cumsum())
plt.show()