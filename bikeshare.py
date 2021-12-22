{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "debd1489",
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "import pandas as pd\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2c42ac6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_of_city={'chicago':'F:/udacity_project/chicago.csv',\n",
    "             'new york city':'F:/udacity_project/new_york_city.csv',\n",
    "             'washington':'F:/udacity_project/washington.csv'}\n",
    "months= ['all', 'january', 'february', 'march', 'april', 'may', 'june']\n",
    "days= ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c5bca0ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "def filteration():\n",
    "    print('Hello! let\\'s explore some data')\n",
    "    city=''\n",
    "    while city not in data_of_city.keys():\n",
    "        print('let\\'s start with the city')\n",
    "        city=input('Please selcet one of the following city: chicago, new york city or washington: ').lower()\n",
    "        if city.lower() not in  data_of_city.keys():\n",
    "            print(\"please try again\")\n",
    "    \n",
    "    print(f\"\\n your city is {city.title()}.\")\n",
    "\n",
    "    selected_month=''\n",
    "    while selected_month.lower() not in months:\n",
    "        print('please select the month')\n",
    "        selected_month=input('please select one of the following months: all , january, february, march, april, may or june;  ').lower()\n",
    "        if selected_month.lower() not in months:\n",
    "            print('Please try again')\n",
    "    print('your month is {}.'.format(selected_month.title()))\n",
    "    selected_day=''\n",
    "    while selected_day not in days:\n",
    "        print('let\\'s select a day')\n",
    "        selected_day=input('please select one of the following days:all, saturday, sunday, monday, tuesday or  wednesday: ').lower()\n",
    "        if selected_day.lower() not in days:\n",
    "            print('please try again')\n",
    "    print('your day is {}'.format(selected_day))\n",
    "    return city , selected_month, selected_day\n",
    "\n",
    "           "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3ad880b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def loading(city,selected_month,selected_day):\n",
    "    df=pd.read_csv(data_of_city[city])\n",
    "    df['Start Time'] = pd.to_datetime(df['Start Time'])\n",
    "    df['month'] = df['Start Time'].dt.month\n",
    "    df['day'] = df['Start Time'].dt.day_name()\n",
    "    df['hour'] = df['Start Time'].dt.hour\n",
    "    if selected_month != 'all':\n",
    "        months=[i for i in months[1:]]\n",
    "        month = months.index(month) + 1\n",
    "        df = df[df['month'] == month]\n",
    "    if selected_day != 'all':\n",
    "        df=df[df['day']== day.title()]\n",
    "    return df\n",
    "      \n",
    "        \n",
    "           \n",
    "    \n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e94d4c27",
   "metadata": {},
   "outputs": [],
   "source": [
    "def popular_time(df):\n",
    "    '''starting statistics analysis on most popular time'''\n",
    "    print('calculating popular time')\n",
    "    starting_time=time.time()\n",
    "    popular_month = df['month'].mode()[0]\n",
    "    print('popular month is {}'.format(popular_month))\n",
    "    popular_day=df['day'].mode()[0]\n",
    "    print(\"popular month is {}\".format(popular_day))\n",
    "    popular_start_hour=df['hour'].mode()[0]\n",
    "    print('popular start hour is {}'.format(popular_start_hour))\n",
    "    print(f\"\\the time they took {(time.time() - starting_time)} seconds.\")\n",
    "    print('-'*100)\n",
    "\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3875f869",
   "metadata": {},
   "outputs": [],
   "source": [
    "def popular_station(df):\n",
    "    print('calculating popular station')\n",
    "    '''start statistics analysis on most popular station'''\n",
    "    starting_time = time.time()\n",
    "    popular_start_station = df['Start Station'].mode()[0]\n",
    "    print('the popular start station is {}'.format(popular_start_station))\n",
    "    popular_end_station = df['End Station'].mode()[0]\n",
    "    print('the popular end station is {}'.format(popular_end_station))\n",
    "    df['most common trip'] = df['Start Station'] + ' to ' + df['End Station']\n",
    "    most_common_trip = df['most common trip'].mode()[0]\n",
    "    print('Most common trip is {}'.format(most_common_trip))\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - starting_time))\n",
    "   \n",
    "  \n",
    "    print('-'*100)      \n",
    "   \n",
    "   \n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4a2dc803",
   "metadata": {},
   "outputs": [],
   "source": [
    "def trip_duration(df):\n",
    "    ''' statistics on trip duration'''\n",
    "    print('trip duartion calculation')\n",
    "    \n",
    "    starting_time = time.time()\n",
    "    total_travel_time = df['Trip Duration'].sum()\n",
    "    print('total travel time is {}'.format(total_travel_time))\n",
    "    average_travel_time = df['Trip Duration'].mean()\n",
    "    print(\"average travel time is {} mins\".format(average_travel_time))\n",
    "    \n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - starting_time))\n",
    "    print('-'*100)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "451fb66e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def user_info(df,city):\n",
    "    starting_time = time.time()\n",
    "    print('now we will display some information about the users')\n",
    "    print('user type is :')\n",
    "    print(df['User Type'].value_counts())\n",
    "    \n",
    "    if city != 'washington':\n",
    "        print('Gender Stats:')\n",
    "        print(df['Gender'].value_counts())\n",
    "        most_common_year = df['Birth Year'].mode()[0]\n",
    "        print('most common year of birth is {}'.format(most_common_year))\n",
    "        recent_year = df['Birth Year'].max()\n",
    "        print(\"most recent year of birth is {}\".format(recent_year))\n",
    "        early_year = df['Birth Year'].min()\n",
    "        print('the earliest year is {}'.format(early_year))\n",
    "        print(\"\\nThis took %s seconds.\" % (time.time() - starting_time))\n",
    "        print('-'*100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9e40abb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def the_function():\n",
    "    while True:\n",
    "        \n",
    "        city,selected_month,selected_day=filteration()\n",
    "        df=loading(city,selected_month,selected_day)\n",
    "        popular_time(df)\n",
    "        popular_station(df)\n",
    "        trip_duration(df)\n",
    "        user_info(df,city)\n",
    "        another_analysis = input('would you like another analysis yes or no ')\n",
    "        if another_analysis.lower() != 'yes':\n",
    "            break\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5cf5800",
   "metadata": {},
   "outputs": [],
   "source": [
    "the_function()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
