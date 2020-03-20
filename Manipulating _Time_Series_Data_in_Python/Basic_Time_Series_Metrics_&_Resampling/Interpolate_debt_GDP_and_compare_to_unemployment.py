# Import & inspect data here
data = pd.read_csv('debt_unemployment.csv', parse_dates=['date'], index_col='date')
print(data.info())

# Interpolate and inspect here
interpolated = data.interpolate()
print(interpolated)

# Plot interpolated data here
interpolated.plot(secondary_y = 'Unemployment')
plt.show()
