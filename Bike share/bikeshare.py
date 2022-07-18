import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new York City': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("there is three cities ! New York City, Chicago or Washington? which one you want to filter by \n").lower()
        if city not in ('new York City', 'chicago', 'washington'):
            print("you didnt enterd the right choice!!")
            continue
        else:
            break

    
    while True:
        month = input("\n any month you want to filter by ? January, February, March, April, May, June or type 'all' \n").lower()
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
            print("You Didnt Enterd the right Value \n" ) 
            continue
        else:
            break

    
    while True:
        day = input("\n Choice one Day To Filter By Or type all : Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n").lower()
        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
            print("Sorry,you entered the wrong value")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    if month != 'all':
    	
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	
        df = df[df['month'] == month]

        
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]

    return df

 


def time_stats(df):
    

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

   
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)

   
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)

    
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

 
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

   
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")
  

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\n No data available for this month.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_input(city):
    display_raw = input("Enter 'yes' for look about raw data or 'no' \n").lower()
    while display_raw=='yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city],chunksize=5):
                print(chunk)
                display_raw = input("Enter 'yes' for look about raw data or 'no' \n").lower()
                if display_raw != 'yes':
                    print("Thankyou")
                    break
            break
        except:
            print("thankYou")
                


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_input(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
