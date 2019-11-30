import pandas as pd
see_more =""
CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv' }

### ask user input data filter
def get_input():
    print('Hi there! Let\'s explore some US bikeshare data!')
    while True:
        city_list = ['chicago','new york','washington']
        city = input('For which city would you like to see bikeshare data?\n Chicago\n New York\n Washington\n').lower()
        if (city not in city_list):
            print ("You typed an incorrect city name. Please try again")
        else:
            break
    global ask
    while True:
        choices = ['month','day','none']
        ask = input('Filter the data by month, day, or no filter at all?\n Please type month, day, or none\n').lower()
        if (ask not in choices):
            print ('Please print only one of the following: month, day, or none:')
        else:
            break
    if ask == 'month':
        while True:
            month = input('Insert month to filter: \n January \n February \n March \n April \n May \n June \n').lower()
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if (month not in months):
                print ('Please type only a proper full month name from the list below (e.g.: March)')
            else:
                break
        month = months.index(month)+1
        day = 0
        print ('\n Month based Filtering:')
    elif ask == 'day':
        while True:
            days = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            day = input('Insert any day of the week to filter:\n').title()
            if (day not in days):
                print ('Please type only a proper full week day (e.g.: Sunday)')
            else:
                break
        month = 0
    elif ask == 'none':
        print('\n No Filtering:')
        day = 0
        month = 0
    return ask, city, month, day

### load data function
def load_data(ask,city,month,day):
    df = pd.read_csv(CITY_DATA[city])
# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
# extract month day and hour from Start Time to create new and separate columns for each
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if ask == 'month':
        df = df[df['month'] == month]
    if ask == 'day':
        df = df[df['day_of_week'] == day]
    print (df.head(10))
    return df

### Function to present all necessary data
def present_data(df):
    # printing popluar times of travel
    popular_day = df['day_of_week'].mode()[0]
    popular_hour = df['hour'].mode()[0]
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    if ask == 'month' or ask == 'none':
        print ('Most popular day of week: ', popular_day)
    if ask == 'none':
        print ('Most popular month: ', popular_month)

# printing trip data
    print('\nTotal travel time:')
    total_hours_travel = df['Trip Duration'].sum()
    time1 = total_hours_travel
    hour1 = time1 // 3600
    time1 %= 3600
    minutes1 = time1 // 60
    time1 %= 60
    seconds1 = time1
    print("{}h:{}m:{}s".format(hour1, minutes1, seconds1),'\n')

# display mean travel time
    avg_travel = df['Trip Duration'].mean()
    time2 = avg_travel
    minutes2 = time2 // 60
    time2 %= 60
    seconds2 = time2
    print ('Average travel time (mins) {}m:{}s'.format(minutes2,seconds2),'\n')

#printing popular stations and trip data
    common_start_station = df['Start Station'].mode()[0]
    print ('Most common start station: ', common_start_station)

    common_end_station = df['End Station'].mode()[0]
    print ('Most common end station: ', common_end_station)

    df['most_common_trip'] = df['Start Station'].str.cat(df['End Station'], sep = ' to ')
    common_trip = df['most_common_trip'].mode()[0]
    print ('Most common trip from start to end: ', common_trip,'\n')
### end of Present Data function

### user info and data
def user_info(df):

    try:
        print('\nUser Info:\n')
        # count of user types
        user_type = df.groupby(['User Type']).size().reset_index().rename(columns={0:'count'})
        print (user_type)
        #  Display counts of gender
        gender_count=df.groupby(['Gender']).size().rename(columns={0:'Gender_Count'})
        print(gender_count)
        # Display earliest, most recent, and most common year of birth
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print ('Year of birth - Earliest: {}, most recent: {}, most common: {}'.format(earliest, most_recent, common),'\n')
    except KeyError:
        print('User info for Washington city is not available.\n')

### ask user if to present raw data
def raw_data(city):
    df = pd.read_csv(CITY_DATA[city])
    option = 'yes'
    i=5
    while option == 'yes':
       option = input('\nWould you like to see the raw data? please type yes or no: ').lower()
       if option != 'yes':
           break
       else:
           print (df[:5])
           while option == 'yes':
               option = input ('\n Would you like to see additional 5 rows of raw data? please type yes or no: ').lower()
               if option == 'yes':
                   print (df[i:(i+5)])
                   i += 5


def main():
    while True:
        ask, city, month, day = get_input()
        df = load_data(ask, city, month, day)
        present_data (df)
        user_info(df)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
     main()

def new_city():
    nc = input("please add a new city: ")
        
