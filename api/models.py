from django.db import models


# Create your models here.
class Continent(models.Model):
    continent = models.CharField(max_length=50, verbose_name='Continent', unique=True)

    class Meta:
        ordering = ('continent',)

    def __str__(self):
        return self.continent


class Country(models.Model):
    country = models.CharField(max_length=100, unique=True)
    iso_code = models.CharField(max_length=5, verbose_name='Country Iso Code', unique=True)
    continent = models.ForeignKey('Continent', on_delete=models.CASCADE, related_name='countries')

    class Meta:
        ordering = ('country',)

    def __str__(self):
        return self.country


class Data(models.Model):
    country = models.ForeignKey(
        'Country',
        related_name='country_data',
        on_delete=models.CASCADE
        )
    date = models.DateField()
    total_cases = models.IntegerField(verbose_name="Total covid19 case")
    new_cases = models.IntegerField(verbose_name="new covid19 cases", blank=True, null=True)
    new_cases_smoothed = models.FloatField(blank=True, null=True)
    total_deaths = models.IntegerField(blank=True, null=True)
    new_deaths = models.IntegerField(blank=True, null=True)
    new_deaths_smoothed = models.FloatField(blank=True, null=True)
    total_cases_per_million = models.FloatField(blank=True, null=True)
    new_cases_per_million = models.FloatField(blank=True, null=True)
    new_cases_smoothed_per_million = models.FloatField(blank=True, null=True)
    total_deaths_per_million = models.FloatField(blank=True, null=True)
    new_deaths_per_million = models.FloatField(blank=True, null=True)
    new_deaths_smoothed_per_million = models.FloatField(blank=True, null=True)
    reproduction_rate = models.FloatField(null=True, blank=True)
    icu_patients = models.FloatField(null=True, blank=True)
    icu_patients_per_million = models.FloatField(null=True, blank=True)
    hosp_patients = models.FloatField(null=True, blank=True)
    hosp_patients_per_million = models.FloatField(null=True, blank=True)
    weekly_icu_admissions = models.FloatField(null=True, blank=True)
    weekly_icu_admissions_per_million = models.FloatField(null=True, blank=True)
    weekly_hosp_admissions = models.FloatField(null=True, blank=True)
    weekly_hosp_admissions_per_million = models.FloatField(null=True, blank=True)
    new_tests = models.FloatField(null=True, blank=True)
    total_tests = models.FloatField(null=True, blank=True)
    total_tests_per_thousand = models.FloatField(null=True, blank=True)
    new_tests_per_thousand = models.FloatField(null=True, blank=True)
    new_tests_smoothed = models.FloatField(null=True, blank=True)
    new_tests_smoothed_per_thousand = models.FloatField(null=True, blank=True)
    positive_rate = models.FloatField(null=True, blank=True)
    tests_per_case = models.FloatField(null=True, blank=True)
    tests_units = models.FloatField(null=True, blank=True)
    total_vaccinations = models.FloatField(null=True, blank=True)
    people_vaccinated = models.FloatField(null=True, blank=True)
    people_fully_vaccinated = models.FloatField(null=True, blank=True)
    total_boosters = models.FloatField(null=True, blank=True)
    new_vaccinations = models.FloatField(null=True, blank=True)
    new_vaccinations_smoothed = models.FloatField(null=True, blank=True)
    total_vaccinations_per_hundred = models.FloatField(null=True, blank=True)
    people_vaccinated_per_hundred = models.FloatField(null=True, blank=True)
    people_fully_vaccinated_per_hundred = models.FloatField(null=True, blank=True)
    total_boosters_per_hundred = models.FloatField(null=True, blank=True)
    new_vaccinations_smoothed_per_million = models.FloatField(null=True, blank=True)
    stringency_index = models.FloatField(null=True, blank=True)
    population = models.FloatField(null=True, blank=True)
    population_density = models.FloatField(null=True, blank=True)
    median_age = models.FloatField(null=True, blank=True)
    aged_65_older = models.FloatField(null=True, blank=True)
    aged_70_older = models.FloatField(null=True, blank=True)
    gdp_per_capita = models.FloatField(null=True, blank=True)
    extreme_poverty = models.FloatField(null=True, blank=True)
    cardiovasc_death_rate = models.FloatField(null=True, blank=True)
    diabetes_prevalence = models.FloatField(null=True, blank=True)
    female_smokers = models.FloatField(null=True, blank=True)
    male_smokers = models.FloatField(null=True, blank=True)
    handwashing_facilities = models.FloatField(null=True, blank=True)
    hospital_beds_per_thousand = models.FloatField(null=True, blank=True)
    life_expectancy = models.FloatField(null=True, blank=True)
    human_development_index = models.FloatField(null=True, blank=True)
    excess_mortality = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ('country',)

    def __str__(self):
        return self.country


class TempContinent(models.Model):
    continent = models.CharField(max_length=50, verbose_name='Continent')

    class Meta:
        ordering = ('continent',)

    def __str__(self):
        return self.continent


class TempCountry(models.Model):
    country = models.CharField(max_length=100)
    iso_code = models.CharField(max_length=5, verbose_name='Country Iso Code')
    continent = models.CharField(max_length=50, verbose_name='Continent')

    class Meta:
        ordering = ('country',)

    def __str__(self):
        return self.country


class TempData(models.Model):
    country = models.CharField(max_length=150)
    date = models.DateField()
    total_cases = models.IntegerField(verbose_name="Total covid19 case")
    new_cases = models.IntegerField(verbose_name="new covid19 cases", blank=True, null=True)
    new_cases_smoothed = models.FloatField(blank=True, null=True)
    total_deaths = models.IntegerField(blank=True, null=True)
    new_deaths = models.IntegerField(blank=True, null=True)
    new_deaths_smoothed = models.FloatField(blank=True, null=True)
    total_cases_per_million = models.FloatField(blank=True, null=True)
    new_cases_per_million = models.FloatField(blank=True, null=True)
    new_cases_smoothed_per_million = models.FloatField(blank=True, null=True)
    total_deaths_per_million = models.FloatField(blank=True, null=True)
    new_deaths_per_million = models.FloatField(blank=True, null=True)
    new_deaths_smoothed_per_million = models.FloatField(blank=True, null=True)
    reproduction_rate = models.FloatField(null=True, blank=True)
    icu_patients = models.FloatField(null=True, blank=True)
    icu_patients_per_million = models.FloatField(null=True, blank=True)
    hosp_patients = models.FloatField(null=True, blank=True)
    hosp_patients_per_million = models.FloatField(null=True, blank=True)
    weekly_icu_admissions = models.FloatField(null=True, blank=True)
    weekly_icu_admissions_per_million = models.FloatField(null=True, blank=True)
    weekly_hosp_admissions = models.FloatField(null=True, blank=True)
    weekly_hosp_admissions_per_million = models.FloatField(null=True, blank=True)
    new_tests = models.FloatField(null=True, blank=True)
    total_tests = models.FloatField(null=True, blank=True)
    total_tests_per_thousand = models.FloatField(null=True, blank=True)
    new_tests_per_thousand = models.FloatField(null=True, blank=True)
    new_tests_smoothed = models.FloatField(null=True, blank=True)
    new_tests_smoothed_per_thousand = models.FloatField(null=True, blank=True)
    positive_rate = models.FloatField(null=True, blank=True)
    tests_per_case = models.FloatField(null=True, blank=True)
    tests_units = models.FloatField(null=True, blank=True)
    total_vaccinations = models.FloatField(null=True, blank=True)
    people_vaccinated = models.FloatField(null=True, blank=True)
    people_fully_vaccinated = models.FloatField(null=True, blank=True)
    total_boosters = models.FloatField(null=True, blank=True)
    new_vaccinations = models.FloatField(null=True, blank=True)
    new_vaccinations_smoothed = models.FloatField(null=True, blank=True)
    total_vaccinations_per_hundred = models.FloatField(null=True, blank=True)
    people_vaccinated_per_hundred = models.FloatField(null=True, blank=True)
    people_fully_vaccinated_per_hundred = models.FloatField(null=True, blank=True)
    total_boosters_per_hundred = models.FloatField(null=True, blank=True)
    new_vaccinations_smoothed_per_million = models.FloatField(null=True, blank=True)
    stringency_index = models.FloatField(null=True, blank=True)
    population = models.FloatField(null=True, blank=True)
    population_density = models.FloatField(null=True, blank=True)
    median_age = models.FloatField(null=True, blank=True)
    aged_65_older = models.FloatField(null=True, blank=True)
    aged_70_older = models.FloatField(null=True, blank=True)
    gdp_per_capita = models.FloatField(null=True, blank=True)
    extreme_poverty = models.FloatField(null=True, blank=True)
    cardiovasc_death_rate = models.FloatField(null=True, blank=True)
    diabetes_prevalence = models.FloatField(null=True, blank=True)
    female_smokers = models.FloatField(null=True, blank=True)
    male_smokers = models.FloatField(null=True, blank=True)
    handwashing_facilities = models.FloatField(null=True, blank=True)
    hospital_beds_per_thousand = models.FloatField(null=True, blank=True)
    life_expectancy = models.FloatField(null=True, blank=True)
    human_development_index = models.FloatField(null=True, blank=True)
    excess_mortality = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ('country',)

    def __str__(self):
        return self.country
