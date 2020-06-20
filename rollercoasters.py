import pandas as pd
import matplotlib.pyplot as plt

steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')

#print(wood[wood['Name'] == 'Boulder Dash'])

# Write a function to plot rankings over time for 1 roller coaster here:

def rank_year (name, park):
    dfwood = wood[(wood['Name'] == name) & (wood['Park'] == park)]
    plt.plot(dfwood['Year of Rank'], dfwood['Rank'],)
    plt.ylabel('Rank')
    plt.xlabel('Year')
    plt.legend([name], loc = 1)
    plt.show()

#print(rank_year('El Toro', 'Six Flags Great Adventure'))

# Write a function to plot rankings over time for 2 roller coasters here:

def rank_year2 (name1, name2, park1, park2):
    dfwood1 = wood[(wood['Name'] == name1) & (wood['Park'] == park1)]
    dfwood2 = wood[(wood['Name'] == name2) & (wood['Park'] == park2)]
    ay= plt.subplot()
    plt.plot(dfwood1['Year of Rank'], dfwood1['Rank'])
    plt.plot(dfwood2['Year of Rank'], dfwood2['Rank'])
    plt.ylabel('Rank')
    plt.xlabel('Year')
    plt.legend([name1, name2], loc = 1)
    ay.set_yticks([1, 2, 3, 4])
    plt.show()

#print(rank_year2('El Toro', 'Boulder Dash', 'Six Flags Great Adventure', 'Lake Compounce'))

# Write a function to plot top n rankings over time here:

def top_ranking(df,n):

  top = df[df['Rank'] <= n]
  fig, ax = plt.subplots(figsize=(10,10))
  for coaster in set(top['Name']):
    coaster_rankings = top[top['Name'] == coaster]
    ax.plot(coaster_rankings['Year of Rank'],coaster_rankings['Rank'],label=coaster)
  ax.set_yticks([i for i in range(1,6)])

  plt.title("Top 10 Rankings")
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.legend(loc=4)
  plt.show()

#print(top_ranked(5, wood))

# Load roller coaster data here:

coasters = pd.read_csv('roller_coasters.csv')
#print(coasters.info())

# Write a function to plot histogram of column values here:

def hist_roller(df, column):
    plt.hist(df[column])
    legend = [column]
    plt.legend(legend)
    plt.xlabel(column)
    plt.ylabel('Number of Roller Coasters')
    plt.show()
#print(hist_roller(coasters, 'speed'))

# Write a function to plot inversions by coaster at a park here:

def bar_park(df, park):
    park_df = df[df['park'] == park]
    roller_coaster = park_df['name']
    inversions = park_df['num_inversions']
    plt.figure(figsize = (20, 15))
    ax = plt.subplot()
    ay = plt.subplot()
    plt.bar(range(len(roller_coaster)), inversions)
    ax.set_xticks(range(len(roller_coaster)))
    ax.set_xticklabels(roller_coaster)
    plt.xticks(rotation=45)
    plt.legend([park])
    plt.show()

#print(bar_park(coasters, 'Walibi Belgium'))

# Write a function to plot pie chart of operating status here:

def pie(coasters):
    df_operating = coasters[coasters['status'] == 'status.operating']
    df_closed = coasters[coasters['status'] == 'status.closed.definitely']
    count = [len(df_operating), len(df_closed)]
    labelsdata = ['Operating', 'Closed']
    plt.pie(count, autopct='%0.1f%%', labels = labelsdata)
    plt.axis('equal')
    plt.show()

#print(pie(coasters))

# Write a function to create scatter plot of any two numeric columns here:

def scatter(df, column1, column2):
    c1 = df[column1]
    c2 = df[column2]
    x = range(len(df))
    plt.figure(figsize=(20, 20))
    ax = plt.subplot()
    plt.scatter(x, c1, color= 'blue', alpha= 0.5)
    plt.scatter(x, c2, color='green', alpha=0.5)
    ax.set_xlabel('Variables')
    ax.set_ylabel('Roller Coasters')
    plt.ylim(0, 200)
    plt.legend([column1, column2])
    plt.show()

#print(scatter(coasters, 'speed', 'height'))

