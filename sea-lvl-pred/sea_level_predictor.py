import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    regress = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    print('Slope =', regress[0], 'y-intercept =', regress[1])
    ax.plot(range(1880, 2051), regress[0]*range(1880, 2051)+regress[1], color='r')

    # Create second line of best fit
    df['Year'] = df['Year'].astype(int)
    recentdf = df.loc[df['Year'] >= 2000]
    regress = linregress(x=recentdf['Year'], y=recentdf['CSIRO Adjusted Sea Level'])
    ax.plot(range(2000, 2051), regress[0]*range(2000, 2051)+regress[1], color='g')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()