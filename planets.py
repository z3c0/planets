
import ephem
import numpy as np
import pandas as pd
import datetime as dt

from ephem import Mercury, Venus, Mars, Saturn, Jupiter, Uranus, Neptune, Pluto, Moon

today = dt.date.today()


def create_reports():
    print('generate date index')
    date = [(today + dt.timedelta(n)).isoformat() for n in range(-36525, 18263)]

    print('instantiate planet vectors')
    mercury =   [Mercury(d) for d in date]
    venus =     [Venus(d) for d in date]
    moon =      [Moon(d) for d in date]
    mars =      [Mars(d) for d in date]
    saturn =    [Saturn(d) for d in date]
    jupiter =   [Jupiter(d) for d in date]
    uranus =    [Uranus(d) for d in date]
    neptune =   [Neptune(d) for d in date]
    pluto =     [Pluto(d) for d in date]

    planet_matrix = [date, mercury, venus, moon, mars, saturn,
                    jupiter, uranus, neptune, pluto]

    print('create dataframe')
    planets_df = pd.DataFrame(np.rot90(planet_matrix))
    planets_df.columns = ['Date', 'Mercury', 'Venus', 'Moon', 'Mars', 'Saturn',
                        'Jupiter', 'Uranus', 'Neptune', 'Pluto']

    planets_df = planets_df.set_index('Date')

    print('calculate distances')
    distance_df = planets_df.applymap(lambda n: n.earth_distance)

    print('determine constellations')
    constellation_df = planets_df.applymap(lambda n: ephem.constellation(n)[1])

    print('create reports')
    constellation_df.to_markdown('constellations.md')
    constellation_df.to_csv('constellations.csv')
    distance_df.to_markdown('distances.md')
    distance_df.to_csv('distances.csv')


if __name__ == '__main__':
    create_reports()
