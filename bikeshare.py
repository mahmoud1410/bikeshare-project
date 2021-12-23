import time
import pandas as pd
import numpy as np
data_of_city={'chicago':'chicago.csv',
             'new york city':'new_york_city.csv',
             'washington':'washington.csv'}
months= ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days= ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']
def filteration():
    print('Hello! let\'s explore some data')
    city=''
    while city not in data_of_city.keys():
        print('let\'s start with the city')
        city=input('Please selcet one of the following city: chicago, new york city or washington: ').lower()
        if city.lower() not in  data_of_city.keys():
            print("please try again")
    
    print(f"\n your city is {city.title()}.")

    selected_month=''
    while selected_month.lower() not in months:
        print('please select the month')
        selected_month=input('please select one of the following months: all , january, february, march, april, may or june;  ').lower()
        if selected_month.lower() not in months:
            print('Please try again')
    print('your month is {}.'.format(selected_month.title()))
    selected_day=''
    while selected_day not in days:
        print('let\'s select a day')
        selected_day=input('please select one of the following days:all, saturday, sunday, monday, tuesday or  wednesday: ').lower()
        if selected_day.lower() not in days:
            print('please try again')
    print('your day is {}'.format(selected_day))
    return city , selected_month, selected_day
def loading(city,selected_month,selected_day):
    df=pd.read_csv(data_of_city[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if selected_month != 'all':
        months=[i for i in months[1:]]
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if selected_day != 'all':
        df=df[df['day']== day.title()]
    return df 
def popular_time(df):
    '''starting statistics analysis on most popular time'''
    print('calculating popular time')
    starting_time=time.time()
    popular_month = df['month'].mode()[0]
    print('popular month is {}'.format(popular_month))
    popular_day=df['day'].mode()[0]
    print("popular month is {}".format(popular_day))
    popular_start_hour=df['hour'].mode()[0]
    print('popular start hour is {}'.format(popular_start_hour))
    print(f"\the time they took {(time.time() - starting_time)} seconds.")
    print('-'*100)

def popular_station(df):
    print('calculating popular station')
    '''start statistics analysis on most popular station'''
    starting_time = time.time()
    popular_start_station = df['Start Station'].mode()[0]
    print('the popular start station is {}'.format(popular_start_station))
    popular_end_station = df['End Station'].mode()[0]
    print('the popular end station is {}'.format(popular_end_station))
    df['most common trip'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_trip = df['most common trip'].mode()[0]
    print('Most common trip is {}'.format(most_common_trip))
    print("\nThis took %s seconds." % (time.time() - starting_time))
   
  
    print('-'*100)      
def trip_duration(df):
    ''' statistics on trip duration'''
    print('trip duartion calculation')
    
    starting_time = time.time()
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time is {}'.format(total_travel_time))
    average_travel_time = df['Trip Duration'].mean()
    print("average travel time is {} mins".format(average_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - starting_time))
    print('-'*100)
def user_info(df,city):
    starting_time = time.time()
    print('now we will display some information about the users')
    print('user type is :')
    print(df['User Type'].value_counts())
    
    if city != 'washington':
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        most_common_year = df['Birth Year'].mode()[0]
        print('most common year of birth is {}'.format(most_common_year))
        recent_year = df['Birth Year'].max()
        print("most recent year of birth is {}".format(recent_year))
        early_year = df['Birth Year'].min()
        print('the earliest year is {}'.format(early_year))
        print("\nThis took %s seconds." % (time.time() - starting_time))
        print('-'*100)
def displaying(df):
    """Displaying 5 raws at a time ."""

    data_displaying = input('\nWould you like to see 5 rows of raw data? yes or no:\n').lower()
    if data_displaying != 'no':
        z = 0
        while (z < df['Start Time'].count() and data_displaying != 'no'):
            print(df.iloc[z:z+5])
            z += 5
            more = input('\nWould you like to see 5 more rows of data? yes or no:\n').lower()
            if more != 'yes':
                break
def main():
    while True:
        
        city,selected_month,selected_day=filteration()
        df=loading(city,selected_month,selected_day)
        popular_time(df)
        popular_station(df)
        trip_duration(df)
        user_info(df,city)
	displaying(df)
        another_analysis = input('would you like another analysis yes or no ')
        if another_analysis.lower() != 'yes':
            break
if __name__ == "__main__":
	main()  
           
