# from api.models import Continent, Country, Data
import pandas as pd
from sqlalchemy import create_engine

NAME = 'nakala'
USER = 'nakalaApi'
PASSWORD = 'nakala'
HOST = '127.0.0.1'
PORT = '5432'

path = '/home/sage/PycharmProjects/NakalaAnalytics/utils/sample.csv'
path2 = '/home/sage/PycharmProjects/NakalaAnalytics/owid-covid-data.csv'

continent_list = ['continent']
country_list = ['location', 'iso_code', 'continent']
conn_string = 'postgresql://nakalaApi:nakala@127.0.0.1/nakala'
herokuconn = 'postgres://fnitjwitqtdejm:2620bc31af1bb6b60631b3d1eed6c6f11b9a2c72c1d9a7bcbadd60c59e9a1366@ec2-34-196-238-94.compute-1.amazonaws.com:5432/db62abn7bicg5s'
df = pd.read_csv(path2, usecols=continent_list)
df2 = pd.read_csv(path2, usecols=country_list)
df3 = pd.read_csv(path2, parse_dates=['date'])

print(df, df2)

db = create_engine(conn_string)
conn = db.connect()
# df.to_sql('api_tempcontinent', con=conn, if_exists='replace', index=False)
# df2.to_sql('api_tempcountry', con=conn, if_exists='replace', index=False)
df3.rename(columns={'location': 'country'}, inplace=True)
df3.drop(columns=['iso_code', 'continent'], axis=1, inplace=True)
df3.to_sql('api_tempdata', con=conn, index=False, if_exists='append', method='multi')

with db.begin() as cn:
    sql1 = """INSERT INTO api_continent (continent)
            SELECT continent
            FROM api_tempcontinent t
            WHERE NOT EXISTS 
                (SELECT 1 FROM api_continent f
                 WHERE t.continent = f.continent) ON CONFLICT (continent) DO NOTHING;
                 """

    cn.execute(sql1)
with db.begin() as cn:
    sql2 = """INSERT INTO api_country (country, iso_code, continent_id)
            SELECT location, iso_code, ac.id FROM api_tempcountry t 
            JOIN api_continent ac on t.continent = ac.continent
            WHERE NOT EXISTS (SELECT 1 FROM api_country f WHERE t.location = f.country  AND t.iso_code = f.iso_code 
            AND ac.id = f.continent_id)
            ON CONFLICT DO NOTHING;
                 """
    cn.execute(sql2)
with db.begin() as cn:
    sql3 = """INSERT INTO api_data (date, total_cases, new_cases, new_cases_smoothed, total_deaths, new_deaths, 
    new_deaths_smoothed, total_cases_per_million, new_cases_per_million, new_cases_smoothed_per_million, 
    total_deaths_per_million, new_deaths_per_million, new_deaths_smoothed_per_million, reproduction_rate, icu_patients, 
    icu_patients_per_million, hosp_patients, hosp_patients_per_million, weekly_icu_admissions, 
    weekly_icu_admissions_per_million, weekly_hosp_admissions, weekly_hosp_admissions_per_million, new_tests, 
    total_tests, total_tests_per_thousand, new_tests_per_thousand, new_tests_smoothed, new_tests_smoothed_per_thousand, 
    positive_rate, tests_per_case, tests_units, total_vaccinations, people_vaccinated, people_fully_vaccinated, 
    total_boosters, new_vaccinations, new_vaccinations_smoothed, total_vaccinations_per_hundred, 
    people_vaccinated_per_hundred, people_fully_vaccinated_per_hundred, total_boosters_per_hundred, 
    new_vaccinations_smoothed_per_million, stringency_index, population, population_density, median_age, aged_65_older, 
    aged_70_older, gdp_per_capita, extreme_poverty, cardiovasc_death_rate, diabetes_prevalence, female_smokers, 
    male_smokers, handwashing_facilities, hospital_beds_per_thousand, life_expectancy, human_development_index, 
    excess_mortality, country_id) 
    SELECT date, total_cases, new_cases, new_cases_smoothed, total_deaths, new_deaths, 
    new_deaths_smoothed, total_cases_per_million, new_cases_per_million, new_cases_smoothed_per_million, 
    total_deaths_per_million, new_deaths_per_million, new_deaths_smoothed_per_million, reproduction_rate, icu_patients, 
    icu_patients_per_million, hosp_patients, hosp_patients_per_million, weekly_icu_admissions, 
    weekly_icu_admissions_per_million, weekly_hosp_admissions, weekly_hosp_admissions_per_million, new_tests, 
    total_tests, total_tests_per_thousand, new_tests_per_thousand, new_tests_smoothed, new_tests_smoothed_per_thousand, 
    positive_rate, tests_per_case, tests_units, total_vaccinations, people_vaccinated, people_fully_vaccinated, 
    total_boosters, new_vaccinations, new_vaccinations_smoothed, total_vaccinations_per_hundred, 
    people_vaccinated_per_hundred, people_fully_vaccinated_per_hundred, total_boosters_per_hundred, 
    new_vaccinations_smoothed_per_million, stringency_index, population, population_density, median_age, aged_65_older, 
    aged_70_older, gdp_per_capita, extreme_poverty, cardiovasc_death_rate, diabetes_prevalence, female_smokers, 
    male_smokers, handwashing_facilities, hospital_beds_per_thousand, life_expectancy, human_development_index, 
    excess_mortality, ac.id FROM api_tempdata t 
            JOIN api_country ac on t.country = ac.country
            """
    cn.execute(sql3)


conn.close()
