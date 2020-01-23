import time
import pandas as pd
import numpy as np
from IPython.display import clear_output
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        city = input('enter any one city in chicago, new york city and washington')
        if city.lower() not in CITY_DATA.keys():
            clear_output()
            continue
        else:
            print('entered city is',city)
            break
            
    while True:
        month = input('enter he month of your choice--- january,february,march,april,may,june.july,august,september,october,november,december or all for no filter')
        if month=='all':
            print('Applied No filter')
            break
        
        elif month.capitalize() not in calendar.month_name:
            clear_output()
            continue
        
        else:
            print('entered month is',month)
            break
    
    while True:
        day = input ('enter your choice of day in the format of mon,tue,wed,thu,fri,sat,sun or all for no fiter')
        if day=='all':
            print('Applied No filter')
            break
        elif day.capitalize() not in calendar.day_name:
            clear_output()
            continue
        else:
            print('entered day is',day)
            break
    print('-'*40)
    return city, month.capitalize(), day.capitalize()


def load_data(city, month, day):

    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month=='All':
        pass
    else:
        d={n:a for a,n in enumerate(calendar.month_name)}
        df=df[df['month']==d.get(month)]    
        
    if day=='All':
        pass
    else:
        df=df[df['day_of_week']==day]
    
    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    a = df['month'].value_counts().head(1).index
    for i in a:
        print('The most common month is \n',calendar.month_name[i],'\n')
    b=df['day_of_week'].value_counts().head(1).index
    for i in b:
        print('The most common day of week is \n',i,'\n')    
    print('The most common start hour is \n',df['Start Time'].dt.hour.head(1),'\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('The most commonly used start station\n',df['Start Station'].value_counts().head(1),'\n')
    print('The most commonly used end station\n',df['End Station'].value_counts().head(1),'\n')
    A=pd.Series(zip(df['Start Station'],df['End Station']))
    print('The most popular trip is \n',A.value_counts().head(1),'\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('The total travel time is\n',df['Trip Duration'].sum(),'\n')    
    print('The mean travel time is\n',df['Trip Duration'].mean(),'\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('The count of the user types are \n',df['User Type'].value_counts(),'\n')
    
    try:
        print('The counts of genders are\n',df['Gender'].value_counts(),'\n')
    except KeyError:
        print('There  isnt a column called Gender in this city data so exception occured')


    try:
        print('The earliest year of birth\n',df['Birth Year'].min(),'\n')
        print('The most recent year of birth\n',df['Birth Year'].max(),'\n')
        print('The common year of birth is\n',df['Birth Year'].value_counts().head(1),'\n')
    except KeyError:
        print('There  isnt a column called Birth Year in this city data so exception occured')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    i = 0
    j = 5
    while True:
        a = input('would you like to see raw data yes/no')
        if a == 'yes':
            print(df.iloc[i:j])
            i= i+5
            j =j+5
        else:
            break
        


def main():
    while True:
        city, month, day = get_filters()
        df =load_data(city, month, day)   

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
