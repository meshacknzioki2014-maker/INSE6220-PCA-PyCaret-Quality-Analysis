from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# Assuming X_scaled is your standardized data
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

explained_var = pca.explained_variance_ratio_
cum_explained = np.cumsum(explained_var)

plt.figure(figsize=(8,5))
plt.plot(np.arange(1, len(explained_var)+1), explained_var, 'o-', label='Individual')
plt.plot(np.arange(1, len(cum_explained)+1), cum_explained, 's--', label='Cumulative')
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Scree / Cumulative Variance Plot')
plt.grid(True)
plt.legend()
plt.show()