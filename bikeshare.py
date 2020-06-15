import time
import pandas as pd
import numpy as np
from IPython.display import display

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
    print('\n Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('\nPlease enter the name of one of these cities: '
                         'Chicago, New York City, or Washington: ').lower()
        except:
            print("sorry, I didn't understand that, please try again.")
            continue
        if city not in ('chicago', 'new york city', 'washington'):
            print("\nSorry, I didn't understand.")
        else:
            print('\nThank You!')
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Please enter a month between January and June, or enter 'all': ").lower()
        except:
            print("sorry I didn't understand the month, please try again.")
            continue
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("\nSorry, I didn't understand.")
        else:
            print('\nThank You!')
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Please enter a day of the week, or enter 'all': ").lower()
        except:
            print("sorry I didn't understand which day, please try again.")
            continue
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("\nSorry, I didn't understand.")
        else:
            print('\nThank You!')
            break


    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city], index_col=0)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #convert the Birth Year column to integers, so it looks clean
    df['Birth Year'] = df['Birth Year'].astype(pd.Int64Dtype())

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['month_name'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month_name'].mode()[0]
    display("the most common month is: {}".format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    display("the most common day of the week is: {}".format(popular_day))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start = df['hour'].mode()[0]
    display("the most common start hour is: {}".format(popular_start))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    pop_start_station = df['Start Station'].mode()[0]
    display("the most commonly used start station is:  {}".format(pop_start_station))

    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].mode()[0]
    display("the most commonly used end station is: {}".format(pop_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    pop_combined_stations = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    display("the most frequently used combined station is: {}".format(pop_combined_stations))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    display("total travel time is: {}".format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    display("mean travel time is: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = pd.DataFrame(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    count_gender = pd.DataFrame(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    most_recent_birth = df['Birth Year'].max()
    popular_year_birth = df['Birth Year'].mode()[0]
    print("\nthe count per user types is: {}"
          "\n\nthe count per gender is: {}"
          "\n\nthe earliest year of birth is: {}"
          "\n\nthe most recent year of birth is: {}"
          "\n\nthe most common year of birth is: {}".
          format(count_user_types, count_gender, earliest_birth, most_recent_birth, popular_year_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_display(df):
    """Displays bikeshare raw data five rows at a time"""

    one_set = 0
    next_set = 5
    while True:
        user_input = input('\nQUESTION: Would you like to display 5 records'
                  ' of raw data? Enter "y" or "n": \n').lower()
        if user_input != 'y':
            print("\nGot it.")
            break

        else:
            print('\nProcessing raw data...\n', df[df.columns[0:]].iloc[one_set:next_set])
            one_set += 5
            next_set += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_display(df)

        restart = input('\nWould you like to restart? Enter "y" or "n": \n').lower()
        if restart != 'y':
            print("\nOK. Good Bye.")
            break


if __name__ == "__main__":
	main()
