import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = {'january', 'february', 'march', 'april', 'may', 'june', 'all'}

DAYS = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #Print statement informs the user to select a city and outlines the choices before input is requested, .lower ensures a user input will be recongized even if the user writes out capital letters
    city = input("Which city would you like to analyze? You have the choice of Chicago, New York City or Washington\n")


    #While loop to run in the event of a invalid input being entered
    while (city.lower() not in CITY_DATA):
        print ('Invalid Input!: Incorrect City Name')
        city =input("Which city would you like to analyze? You have the choice of Chicago, New York City or Washington\n")



    # get user input for month (all, january, february, ... , june)
    month =input("Which month would you like to analyze? You have the choice of the first six months of the year: January, February, March, April, May and June. If you wish to see data from all months instead of just one, simply type all\n")


    #While loop to account for user enterting a specific month or all to see data for every month
    while (month.lower() != 'all' and month.lower() not in MONTHS):
        print ('Invalid Input!: Incorrect Month Name')
        month =input("Which month would you like to analyze? You have the choice of the first six months of the year: January, February, March, April, May and June. If you wish to see data from all months instead of just one, simply type all\n")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day =input("Which day of the week would you like to analyze? If you wish to see data from every day of the week instead of just one, simply type all\n")


    #day equavient of month while loop
    while (day.lower() != 'all' and day.lower() not in DAYS):
     print ('Invalid Input!: Incorrect Day Name')
     day =input("Which day of the week would you like to analyze? If you wish to see data from every day of the week instead of just one, simply type all\n")


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

    #Loads the selected city's data into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    #Converts the start time column into datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #pulls the month, day and hour from Start Time into three new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    #checks if the month filter is required
    if month != 'all':
        # uses the month list to get the reprenstative value for each month
        # filters by month
        df = df[df['month'] == month.title()]

    #checks if the day filter is required
    if day != 'all':
        #filters by day of week
        df = df[df['day_of_week'] == day.title()]

    #uses dataframe to get an output from get filters to define the data values of city, month, day
    return df
    city,month, day = get_filters()
    load_data(city,month, day)
    print(df)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displays the most common month by calculating the mode of the month column
    #[0] is used in this calculation and all other mode calculations to convert the string data to a integer
    common_month = df['month'].mode()[0]
    print('The Most Common Month for Travel is:', common_month) #Uses mode function to work out the most commonth month, converts the integer into a string and displays


    #displays the most common day of week by calculating the mode of the day of week column
    common_day = df['day_of_week'].mode()[0]
    print('The Most Common Day For Travel is:', common_day)

    # displays the most common start hour by calculating the mode of the hour column
    common_hour = df['hour'].mode()[0]
    print('The Most Common Hour For Travel is:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    common_start_st = df['Start Station'].mode()[0]
    print('The Most Common Station that trips start at is:', common_start_st)


    # display most commonly used end station
    common_end_st = df['End Station'].mode()[0]
    print('The Most Common Station that trips end at is:', common_end_st)

    # display most frequent combination of start station and end station trip
    #combines the start and end station data into one, mode is then calucated
    common_combo = df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    print('The most Common combination of start and end stations among trips is:', common_combo.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displays total travel time by suming the trip duration column
    total_time = df['Trip Duration'].sum()
    print('The total duration of trips is:', total_time, 'seconds')

    # displays mean travel time by calculating the trip duration column's mean
    mean_time = df['Trip Duration'].mean()
    print('The average/mean duration of trips is:', mean_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displays counts of user types by counting the values in the user type column and then using .loc to seperate the total of subscribers and customers
    user_count = df['User Type'].value_counts()
    print('The type of user stats are as follows:')
    print('The amount of subscriber users is:', user_count.loc['Subscriber'])
    print('The amount of customer users is:', user_count.loc['Customer'])

    #checks the df columns for the gender column if it is present it runs the following calculation. This accounts for washington's data lacking a gender column
    if "Gender" in df.columns:
    # Displays counts of gender using the same method as the user type calucation
       gender_count = df['Gender'].value_counts()
       print('The gender stats are as follows:')
       print('The total of male users is:', gender_count.loc['Male'])
       print('The total of female users is:', gender_count.loc['Female'])

    # Does the same check as done with the gender column just for birth year instead of gender. Again accounting for washington's lack of data
    if "Birth Year" in df.columns:
    # Displays the earliest, most recent, and most common year of birth by getting the calucating the min, max and mode of the birth year column
       early_by = df['Birth Year'].min()
       recent_by = df['Birth Year'].max()
       common_by = df['Birth Year'].mode()[0]
       print('The earliest birth year of a user is:', early_by)
       print('The most recent birth year of a user is:', recent_by)
       print('The most common birth year of a user is:', common_by)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

    """Displays raw bikeshare data."""


    #askes user for input on if they wish to view raw data. if the user inputs yes it activates the below while loop otherwise the program moves on to asking the user if they wish to restart or not
    view_data = input ('\nWould you like to view 5 rows of raw trip data? Enter yes or no.\n').lower()
    #tells the program to start locating from the first row of data
    start_loc = 0

    #The while loop continues to loop as long as yes is inputted. it will print five rows and each print function adds 5 to the start_loc value thus the code knows to constantly print the next five rows
    #The user is again asked if they wish to see more data, if they say yes they will say the next 5 rows due to the start_loc being updated everytime the while loop repeats
    #if the user types no in response to either the initial input
    while view_data== 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input ('\nWould you like to view 5 rows of raw trip data? Enter yes or no.\n').lower()

#Function which loads the gathered and then askes the user their input if they wish to restart the program
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
