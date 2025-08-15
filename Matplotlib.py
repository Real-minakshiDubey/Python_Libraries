import numpy as np
from matplotlib import pyplot as plt
#print(plt.style.available)
plt.style.use('seaborn-v0_8')

#plt.xkcd() #sketch style design mode

# plt.plot() → Use for continuous numeric data over a sequence (like trends over time)

# year_exp=[0,1,2,3,4,5,6,7,8,9,10]

# pydev_salaries = [3.5, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0, 14.0, 17.0, 20.0, 24.0]
# plt.plot(year_exp,pydev_salaries,'o-g',linewidth=3,label='py dev') 
#'--g' can be written as color='g',linestyle='--',marker='o'and we can use hex values for colour #RRGGBB

# javadev_salaries = [3.0, 3.7, 5.0, 6.5, 8.0, 9.5, 11.0, 12.5, 14.5, 17.0, 20.0]
# plt.plot(year_exp,javadev_salaries,'-k',linewidth=3,label="java dev")

# webdev_salaries = [2.5, 3.0, 3.8, 4.5, 5.5, 6.5, 7.5, 9.0, 11.0, 13.0, 15.0]
# plt.plot(year_exp,webdev_salaries,'--',linewidth=2,label="web dev")

#plt.legend()   #It adds a descriptive box (legend) to your plot showing what each plotted data series represents.

# plt.title('Salaries (in lakhs) of developers in India')
# plt.xlabel('years of experience')
# plt.ylabel('salary(in lakhs)')

plt.grid(True)
#plt.tight_layout() # for sufficient padding
#plt.show()
#plt.savefig('plot.png')


#format string: '[marker][line][colour]'
"""
🎨 Matplotlib Format Strings (fmt) Cheat Sheet

Format string syntax for plot(): '[color][marker][line]'

1. Colors:
    'b' : blue
    'g' : green
    'r' : red
    'c' : cyan
    'm' : magenta
    'y' : yellow
    'k' : black
    'w' : white

2. Markers:
    '.' : point marker
    ',' : pixel marker
    'o' : circle marker
    'v' : triangle_down
    '^' : triangle_up
    '<' : triangle_left
    '>' : triangle_right
    '1' : tri_down
    '2' : tri_up
    '3' : tri_left
    '4' : tri_right
    's' : square
    'p' : pentagon
    '*' : star
    'h' : hexagon1
    'H' : hexagon2
    '+' : plus
    'x' : x
    'D' : diamond
    'd' : thin_diamond
    '|' : vline
    '_' : hline

3. Line styles:
    '-'  : solid line
    '--' : dashed line
    '-.' : dash-dot line
    ':'  : dotted line
    ''   : no line (marker only)

Example usage:
    plt.plot(x, y, 'ro-')  # red color, circle marker, solid line
    plt.plot(x, y, 'g^--') # green color, triangle_up marker, dashed line
"""

#print(plt.style.available)
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

#bar plot
# plt.bar() → Use for categorical data (vertical bars) when categories are few

# year_exp=[0,1,2,3,4,5,6,7,8,9,10]
# x_indexes=np.arange(len(year_exp))
# width=0.25
# pydev_salaries = [3.5, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0, 14.0, 17.0, 20.0, 24.0]
# plt.bar(x_indexes-width,pydev_salaries,width=width,linewidth=3,label='py dev') 

# javadev_salaries = [3.0, 3.7, 5.0, 6.5, 8.0, 9.5, 11.0, 12.5, 14.5, 17.0, 20.0]
# plt.bar(x_indexes,javadev_salaries,width=width,linewidth=3,label="java dev")

# webdev_salaries = [2.5, 3.0, 3.8, 4.5, 5.5, 6.5, 7.5, 9.0, 11.0, 13.0, 15.0]
# plt.bar(x_indexes+width,webdev_salaries,width=width,linewidth=2,label="web dev")
# plt.xticks(ticks=x_indexes,labels=year_exp) #get or set the ticks for x axis
# plt.legend()
#plt.show()

#bar plot using csv file

# import csv
# from collections import Counter

# language_counter = Counter()

# with open('data.csv') as data_file:
#     csv_reader = csv.DictReader(data_file)
#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))

# languages = []
# popularity = []

# for item in language_counter.most_common(15):
#     languages.append(item[0])
#     popularity.append(item[1])

# languages.reverse()
# popularity.reverse()  # Makes most popular language appear at top in barh plot

# print(languages)
# print(popularity)

# # plt.bar(languages,popularity)
# # plt.title("languages popular among developers")
# # plt.xlabel('languages')
# # plt.ylabel('popularity')
# #plt.show()

# #representing bar plot vertically will be messier to understand

# #so lets use horizontal bar plot
#plt.barh()→ Use for categorical data (horizontal bars), good for long labels

# # plt.barh(languages,popularity)
# # plt.title("languages popular among developers")
# # plt.xlabel('popularity')
# # plt.ylabel('languages')
# # plt.tight_layout()
# # plt.show()

#now lets see how to read a csv file using pandas

# import pandas as pd
# from collections import Counter
# import matplotlib.pyplot as plt

# # Read CSV file
# data = pd.read_csv('data.csv')
# lang_Response = data['LanguagesWorkedWith']

# # Count language occurrences
# language_counter = Counter()
# for response in lang_Response:
#     language_counter.update(response.split(';'))

# # Get top 15 languages
# languages = []
# popularity = []
# for item in language_counter.most_common(15):
#     languages.append(item[0])
#     popularity.append(item[1])

# # Reverse for horizontal bar chart (most popular at top)
# languages.reverse()
# popularity.reverse()

# # Plot
# #plt.figure(figsize=(10, 6))
# plt.barh(languages, popularity)
# plt.title("Languages Popular Among Developers")
# plt.xlabel('Popularity')
# plt.ylabel('Languages')
# plt.tight_layout()
# plt.show()


#pie charts
# plt.pie()         → Use for showing parts of a whole (not great for many categories)


# labels=[ 'Java', 'Python', 'SQL', 'HTML/CSS', 'JavaScript']
# slices=[35917, 36443, 47544, 55466, 59219]
# explode=[0,0.1,0,0.1,0]
# colors=['blue','green','red','yellow','pink']
# plt.pie(slices,labels=labels,colors=colors,explode=explode,wedgeprops={'edgecolor':'black'},shadow=True,startangle=90,autopct='%1.1f%%')
# plt.title("My Awesome Pie chart")
# plt.tight_layout()
# plt.show()

#now lets see how to create stack plots

#minutes= [1, 2, 3, 4, 5, 6, 7, 8, 9]
# player1= [1, 2, 3, 3, 4, 4, 4, 4, 5]
# player2= [1, 1, 1, 1, 2, 2, 2, 3, 4]
# player3=[1, 1, 1, 2, 2, 2, 3, 3, 3]

#plt.pie([1, 1, 1], labels=["Player 1", "Player2", "Player3"])

# minutes= [1, 2, 3, 4, 5, 6, 7, 8, 9]
# player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
# player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
# player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

# labels=['player1','player2','player3']
# colors=['red','yellow','blue']
# plt.stackplot(minutes,player1,player2,player3,labels=labels,colors=colors)
# #plt.legend(loc='lower left')  
# plt.legend(loc=(0.06,0.07))#(loc=dist from left,dist from right bottom)

# plt.title('My Awesome stack plots')
# plt.tight_layout()
# plt.show()

#filling area on graph plots
# plt.fill_between()→ Use for area charts (good for showing magnitude over a range)

# import pandas as pd
# #import matplotlib.pyplot as plt

# data=pd.read_csv('salary.csv')
# age=data['Age']
# pydev=data['pydev']
# webdev=data['Webdev']

# # Plot
# plt.plot(age, pydev, color='#444444', label='python developers')
# plt.plot(age,webdev,linestyle='--',label='web developers',color='black')

# #fill in 

# #plt.fill_between(age,pydev,overall_median,alpha=0.25)
# plt.fill_between(age,pydev,webdev,where=(pydev > webdev),interpolate=True,alpha=0.25,label='above avg')
# plt.fill_between(age,pydev, webdev,where=(pydev <=  webdev),interpolate=True,color='pink',alpha=1,label='below avg')
# plt.legend()
# plt.title('salary of developers')
# plt.xlabel('ages')
# plt.ylabel('salary(in lakhs)')
# plt.tight_layout()
# plt.show()


#histograms
# plt.hist() → Use for distribution of a single numeric variable

#import pandas as pd
# ages=[18,19,21,25,26,26,30,32,38,45,55]
# bins=[10,20,30,40,50,60]
# plt.hist(ages,bins=bins,edgecolor='black')

# data=pd.read_csv('data.csv')
# id=data['Responder_id']
# ages=data['Ages']
# bins=[10,20,30,40,50,60]
# plt.hist(ages,bins=bins,edgecolor='black',log=True)
# median_age=29
# plt.axvline(median_age,color='#fc4f30',label="Age Median",linewidth=2)
# plt.legend()
# plt.title('My Awesome histogram')
# plt.xlabel('Ages')
# plt.ylabel('Total Respondents')
# plt.tight_layout()
# plt.show()


#Scatter plots
# plt.scatter()→ Use to show relationship between two numeric variables

#import pandas as pd

# x =[5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y =[7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
# colors= [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
# sizes= [209, 486, 381, 255, 191, 315, 185, 228, 174, 538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]
# plt.scatter(x,y,s=sizes,c=colors,edgecolors='black',alpha=0.75,linewidth=1) #s is size of marker(point) , c is color of marker
# cb=plt.colorbar()
# cb.set_label('Satisfaction')


# data=pd.read_csv('TrendingMovies.csv')
# avg=(data['vote_average'])
# vote=data['vote_count']
# plt.scatter(avg,vote,edgecolors='black',linewidths=1,alpha=0.75)
# cbar=plt.colorbar()
# cbar.set_label('ids')
# #for using log scale to plot
# plt.xscale('log')
# plt.yscale('log')
# plt.legend()
# plt.title('My Awesome Scatter Plot')
# plt.xlabel('id')
# plt.ylabel('vote_count')
# plt.tight_layout()
# plt.show()


#Plotting time series data

import pandas as pd
#from datetime import datetime , timedelta
#from matplotlib import dates as mpl_dates

# dates = [
# datetime (2019, 5, 24),
# datetime (2019, 5, 25),
# datetime (2019, 5, 26),
# datetime (2019, 5, 27),
# datetime (2019, 5, 28),
# datetime (2019, 5, 29),
# datetime (2019, 5, 30)
# ]
# y= [0, 1, 3, 4, 6, 5, 7]
# plt.plot_date(dates,y,linestyle='solid')#we can remove marker by marker=none
# plt.gcf().autofmt_xdate() # for slant dates
# date_format= mpl_dates.DateFormatter('%b,%d %Y')
# plt.gca().xaxis.set_major_formatter(date_format)



# Read CSV
# data = pd.read_csv('dates.csv')

# # Convert Date column to datetime
# data['Date'] = pd.to_datetime(data['Date'])

# # Sort by date
# data.sort_values('Date', inplace=True)

# # Extract columns
# date = data['Date']
# close = data['Close']

# # Plot time series
# plt.plot_date(date, close, linestyle='solid', marker=None, label='Closing Price')

# # Auto-format date labels
# plt.gcf().autofmt_xdate()

# # Add legend
# plt.legend()

# # Titles & layout
# plt.title('Time Series Data Plot')
# plt.xlabel('Date')
# plt.ylabel('Close Value')
# plt.tight_layout()

# # Show
# plt.show()


#Plotting live data in real-time
# import random 
# import pandas as pd
# from itertools import count
# from matplotlib.animation import FuncAnimation
# x_vals=[]
# y_vals=[]

# index = count()
# def animate(i):
#     x_vals.append (next (index))
#     y_vals.append(random.randint(0, 5))
#     plt.cla()
#     plt.plot(x_vals, y_vals)
# ani = FuncAnimation (plt.gcf(), animate, interval=1000)
# plt.title("Real time data plotting")

# plt.show()

#subplots

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
data = pd.read_csv('salary.csv')

# Extract columns
age = data['Age']
webdev = data['Webdev']
pydev = data['pydev']
javadev = data['javadev']

# Create figure and axis
#fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1) #sharex and sharey used to share values of x and y
#we can create multiple fig at the same time
fig1,ax1=plt.subplots()
fig2,ax2=plt.subplots()

# Plot each line
ax1.plot(age, pydev, label='pydev salaries')
ax2.plot(age, webdev, label='webdev salaries', linestyle='--', color='black')
ax1.plot(age, javadev, label='javadev salaries', linestyle='-.', color='red')

# Add legend
ax1.legend()
ax2.legend()


ax1.set_title('Developers Salaries')
# ax1.set_xlabel('Age')
ax1.set_ylabel('Salaries')


ax2.set_xlabel('Age')
ax2.set_ylabel('Salaries')

plt.tight_layout()
plt.show()
