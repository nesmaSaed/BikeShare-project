import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city= get_city()
    month, day = get_month_day()
    print('-'*40)
    return city, month, day

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
def get_city():
    while True:
        city=(input("\nWould you like to see data for Chicago, New york city or Washington?\n").lower().strip())
        if city in CITY_DATA:
            return city
        else:
            pass

def get_month_day():
    while True:
        user_choice= (input("\nWould you like to filter the data by month, day, both or not at all?\n ").lower().strip())
        if user_choice=="month":
            month= get_month()
            day= "all"
            break
        
        elif user_choice=="day":
            month="all"
            day= get_day()
            break
        elif user_choice=="both":
            month= get_month()
            day= get_day()
            break
        elif user_choice=="not at all" or user_choice=="no" or user_choice=="not" or user_choice=="all":
            month= "all"
            day= "all"
            break
        else:
            pass
    return month, day 
    # get user input for month (all, january, february, ... , june)
def get_month():
    while True:
        months=["january", "february", "march", "april", "may", "june"]
        month=(input("\nWhich month - January, February, March, April, May, or June?\n").lower().strip())
        if month in months:
            return month
        else:
            pass

    # get user input for day of week (all, monday, tuesday, ... sunday)
def get_day():
    while True:
        days=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day= (input("\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower().strip())
        if day in days:
            return day
        else:
            pass

    

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df= pd.read_csv(CITY_DATA[city])
    
    df["Start Time"]= pd.to_datetime(df['Start Time'])
    
    df['month']=df['Start Time'].dt.month
    
    df['day_of_week']= df['Start Time'].dt.day_name()
    
    df['hour']= df['Start Time'].dt.hour
    
    df_unfiltered= df 
    
    if month!= 'all':
        months= ["january", "february", "march", "april", "may", "june"]
        month= months.index(month)+1
        df= df[df["month"]==month]
    else:
        df= df_unfiltered

    if day!="all":
        df= df[df["day_of_week"]==day.title()]
    else:
        df= df_unfiltered


    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month!= "all":
        pass
    else:
        common_month= df["month"].mode()[0]
        print("\nThe most common month is: \n", common_month)

    # display the most common day of week
    if day!="all":
        pass
    else:
        common_day= df["day_of_week"].mode()[0]
        print("\nThe most common day of the week is: \n", common_day)

    # display the most common start hour
    df['hour']= df['Start Time'].dt.hour
   
    common_hour= df['hour'].mode()[0]
    print("\nThe most common hour\n", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station= df["Start Station"]. mode()[0]
    print("\nthe most common start station is:\n", common_start_station) 

    # display most commonly used end station
    common_end_station= df["End Station"].mode()[0]
    print("\nThe most common end station is:\n", common_end_station)


    # display most frequent combination of start station and end station trip
    common_combination_start_end= (df["Start Station"]+ df["End Station"]).mode()[0]
    print("\nThe most frequent combination of start station and end station is:\n", common_combination_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time= df["Trip Duration"].sum()
    print("\nThe total travel time is:\n", total_travel_time)

    # display mean travel time
    mean_travel_time= df["Trip Duration"].mean()
    print("\nthe mean of the travel time is:\n", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # Display counts of user types
        count_user_type= df["User Type"].value_counts().to_frame()
        print("Counts of user types are:\n", count_user_type)

        # Display counts of gender
        count_of_gender= df["Gender"].value_counts().to_frame()
        print("Counts of gender are:\n", count_of_gender)

        # Display earliest, most recent, and most common year of birth
        earliest_year_of_birth= df["Birth Year"].min()
        recent_year_of_birth= df["Birth Year"].max()
        common_year_of_birth= df["Birth Year"].mode()[0]
        print("The earliest year of birth is:\n", earliest_year_of_birth)
        print("The most recent year of birth is:\n", recent_year_of_birth)
        print("THe most common year of birth is:\n", common_year_of_birth)
    except:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(city):
    ask= (input(f"\nDo you want to see the raw data of the state of {city}? Enter yes or no.\n").lower().strip())
    if ask!="yes":
        return
    df= pd.read_csv(CITY_DATA[city])
    i=0
    while i<len(df.index):
        data= df.iloc[i:(i+5)]
        print(data)
        answer=(input("\nDo you want to see more? Enter yes or no.\n").lower().strip())
        if answer!="yes":
            return
        i+=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
