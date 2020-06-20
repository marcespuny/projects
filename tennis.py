import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:

df = pd.read_csv('tennis_stats.csv')
#print(df.head(5))

# Perform exploratory analysis here:

x = df['BreakPointsOpportunities']
y = df['Wins']
plt.scatter(x,y, label='Break Points VS Wins', color='blue', s=10, marker="o")
plt.xlabel('Break Points')
plt.ylabel('Wins')
#plt.show()
plt.clf()

# After comparing different variables, wins and break points have the strongest correlation amongst all the rest.

# Perform single feature linear regressions here:

#Break Points to Predict Wins

X = df[['BreakPointsOpportunities']]
y = df[['Wins']]

X_train, \
X_test, \
y_train, \
y_test = train_test_split(X, y, train_size = 0.8)

model = LinearRegression()
model.fit(X_train,y_train)
#print(model.score(X_test, y_test))
prediction = model.predict(X_test)
#print(prediction)
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, prediction, color='blue', linewidth=3)
plt.xlabel("Break Points")
plt.ylabel("Wins")
#plt.show()
plt.clf()

#Aces to Predict Wins

X = df[['Aces']]
y = df[['Wins']]

X_train, \
X_test, \
y_train, \
y_test = train_test_split(X, y, train_size = 0.8)

model = LinearRegression()
model.fit(X_train,y_train)
#print(model.score(X_test, y_test))
prediction = model.predict(X_test)
#print(prediction)
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, prediction, color='blue', linewidth=3)
plt.xlabel("Aces")
plt.ylabel("Wins")
#plt.show()
plt.clf()

#Break Points To Predict Winnings (This regression ends up being the best model)

X = df[['BreakPointsOpportunities']]
y = df[['Winnings']]

X_train, \
X_test, \
y_train, \
y_test = train_test_split(X, y, train_size = 0.8)

model = LinearRegression()
model.fit(X_train,y_train)
#print(model.score(X_test, y_test))
prediction = model.predict(X_test)
#print(prediction)
ax = plt.subplot()
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, prediction, color='blue', linewidth=3)
plt.xlabel("Break Points")
plt.ylabel("Winning per Year")
#plt.show()
plt.clf()


# Perform two feature linear regressions here to find the features that have most impact:

features = df[['TotalPointsWon', 'Wins', 'Losses', 'Ranking', 'Aces',
               'DoubleFaults', 'FirstServe', 'FirstServePointsWon',
               'SecondServePointsWon', 'BreakPointsFaced', 'BreakPointsSaved',
               'ServiceGamesPlayed', 'ServiceGamesWon', 'TotalServicePointsWon',
               'FirstServeReturnPointsWon', 'SecondServeReturnPointsWon',
               'BreakPointsOpportunities', 'BreakPointsConverted', 'ReturnGamesPlayed',
               'ReturnGamesWon', 'ReturnPointsWon']]

outcome = df[['Winnings']]

X_train, \
X_test, \
y_train, \
y_test = train_test_split(features, outcome, train_size = 0.8)

lr = LinearRegression()

model = lr.fit(X_train, y_train)

#print(lr.coef_)

# The features that have a bigger impact on the winnings outcome
# are the total of points won and the points won when the opponent was serving








