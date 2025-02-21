import pandas as pd
def calculate_demographic_data(print_data=True):
    # Read data from file
    # df = None
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # race_count = None
    race_count = df['race'].value_counts()

    # What is the average age of men?
    # average_age_men = None
    average_age_men = df.loc[df['sex'] == 'Male','age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    # percentage_bachelors = None
    percentage_bachelors = df.loc[df['education'] == 'Bachelors'].shape[0]/df.shape[0] * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # higher_education = None
    # lower_education = None
    
    higher_education = df[df['education'].isin(advanced_education)]
    lower_education = df[~df['education'].isin(advanced_education)]

    # percentage with salary >50K
    # higher_education_rich = None
    higher_education_rich = higher_education.loc[(higher_education['salary'] == '>50K')].shape[0]/higher_education.shape[0] * 100
    # lower_education_rich = None
    lower_education_rich = lower_education.loc[lower_education['salary'] == '>50K'].shape[0]/lower_education.shape[0] * 100
    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    # min_work_hours = None
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # num_min_workers = None
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]

    # rich_percentage = None
    rich_percentage = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0]/num_min_workers.shape[0]*100

    # What country has the highest percentage of people that earn >50K?
    earning_by_country  = df.loc[df['salary'] == '>50K','native-country'].value_counts()
    
    total_by_country = df['native-country'].value_counts()
    percentage_by_country = (earning_by_country / total_by_country) * 100
    
    # highest_earning_country = None
    highest_earning_country = percentage_by_country.idxmax()
    # highest_earning_country_percentage = None
    highest_earning_country_percentage = percentage_by_country.max()

    # Identify the most popular occupation for those who earn >50K in India.
    indian_rich = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K') ]
    
    # top_IN_occupation = None
    top_IN_occupation = indian_rich['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men,1),
        'percentage_bachelors': round(percentage_bachelors,1),
        'higher_education_rich': round(higher_education_rich,1),
        'lower_education_rich': round(lower_education_rich,1),
        'min_work_hours':    min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':round(highest_earning_country_percentage,1),
        'top_IN_occupation': top_IN_occupation
    }
