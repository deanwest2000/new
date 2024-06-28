import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns

data = pd.read_csv('automotive_components_data.csv')

data.dropna(inplace=True)
data['Date'] = pd.to_datetime(data['Date'])
data['ProductionVolume'] = data['ProductionVolume'].astype(int)

summary_stats = data.describe()
print("Summary Statistics:\n", summary_stats)

plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['ProductionVolume'], label='Production Volume')
plt.xlabel('Date')
plt.ylabel('Production Volume')
plt.title('Production Volume Over Time')
plt.legend()
plt.savefig('production_volume_over_time.png')
plt.show()

plt.figure(figsize=(10, 8))
correlation = data.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.show()

X = data[['MachineUtilization']]
y = data['ProductionVolume']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

plt.figure(figsize=(10, 5))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, predictions, color='red', linewidth=2, label='Predicted')
plt.xlabel('Machine Utilization')
plt.ylabel('Production Volume')
plt.title('Machine Utilization vs Production Volume')
plt.legend()
plt.savefig('machine_utilization_vs_production_volume.png')
plt.show()

data.to_csv('cleaned_automotive_components_data.csv', index=False)
