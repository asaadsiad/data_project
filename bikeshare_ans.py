import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    while True:
        city = input("Enter city name (Chicago, New York City, Washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city name. Please try again.")

    # Get user input for month
    while True:
        month = input("Enter month (all, January, February, ... June): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid month. Please try again.")

    # Get user input for day of week
    while True:
        day = input("Enter day of the week (all, Monday, Tuesday, ... Sunday): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid day. Please try again.")

    print('-' * 40)
    return city, month, day


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
    # Load the data file for the specified city
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from 'Start Time' to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        month = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['Month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['Month'].mode()[0]
    print('Most Common Month:', common_month)

    # Display the most common day of week
    common_day = df['Day of Week'].mode()[0]
    print('Most Common Day of Week:', common_day)

    # Display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)

    # Display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print('Most Frequent Trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:')
    print(user_types)

    # Display counts of gender if available
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:')
        print(gender_counts)

    # Display earliest, most recent, and most common year of birth if available
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year of Birth:', earliest_year)

        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year of Birth:', most_recent_year)

        common_year = df['Birth Year'].mode()[0]
        print('Most Common Year of Birth:', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
import pandas as pd

import pandas as pd

def print_pandas_lines(df):
    start_line = 5
    end_line = 10

    while True:
        user_input = input("Do you want to see more lines? (yes/no): ")
        if user_input.lower() == "yes":
            if end_line <= len(df):
                print(df[start_line:end_line])
                start_line += 5
                end_line += 5
            else:
                print("No more lines to show.")
                break
        elif user_input.lower() == "no":
            print("Ending the program.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_pandas_lines(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
