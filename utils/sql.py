with db.begin() as cn:
    sql = """INSERT INTO api_continent (continent)
            SELECT continent
            FROM api_tempcontinent t
            WHERE NOT EXISTS 
                (SELECT 1 FROM api_continent f
                 WHERE t.continent = f.continent) ON CONFLICT (continent) DO NOTHING;
                 """

    cn.execute(sql)
with db.begin() as cn:
    sql = """INSERT INTO api_country (country, iso_code, continent_id)
            SELECT location, iso_code, ac.id FROM api_tempcountry t 
            JOIN api_continent ac on t.continent = ac.continent
            WHERE NOT EXISTS (SELECT 1 FROM api_country f WHERE t.location = f.country  AND t.iso_code = f.iso_code 
            AND ac.id = f.continent_id)
            ON CONFLICT DO NOTHING;
                 """

    cn.execute(sql)