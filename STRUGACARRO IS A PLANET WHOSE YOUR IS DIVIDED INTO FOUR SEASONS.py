'''
STRUGACARRO IS A PLANET WHOSE YOUR IS DIVIDED INTO FOUR SEASONS "WINTER" "SPRING" "SUMMER" AND "AUTUMN" IN THAT ORDER 
A YEAR HAS N DAYS AND EVERY SEASON LAST FOR EXACTLY N/4 DAYS. THE YEAR STARTS ON THE FIRST DAY OF "WINTER" AND ENDS ON THE LAST DAY OF "AUTUMN".
GIVEN THE HISTORY OF TEMPERATURES FROM THE PREVIOUS YEAR, FIND THE SEASON WITH THE HIGHEST AMPLITUDE OF TEMPERATURE. THE AMPLITUDE IS THE DIFFERENCE BETWEEN THE HIGHEST AND LOWEST TEMPERATURES OVER THE GIVEN PERIOD ASSUME THAT ALL SEASONS WITHIN ONE YEAR HAVE DIFFERENT TEMPERATURE AMPLITUDES.

 WRITE A FUNCTION 
THAT GIVEN AN ARRAY OF N INTEGERS DENOTING THE TEMPERATURE ON ALL DAYS OF THE YEAR RETURNS A STRING WITH THE NAME OF THE SEASON WITH THE HIGHEST TEMPERATURE AMPLITUDE ONE OF THE FOLLOWING WINTER SPRING SUMMER AND AUTUMN
For example given T=[-3, -14, -5, 7, 8, 42, 8, 3]
-3, -14: Winter
-5, 7: Spring
8, 42: Summer
8,3: Autumn
THE FUNCTION SHOULD RETURN "SUMMER" SINCE THE HIGHEST AMPLITUDE IS 34 ACROSS IN "SUMMER".
 THE CORRECT ANSWER IS "AUTUMN" AMPLITUDE = 21.

ASSUME THAT 
THE ELEMENT OF THE NUMBER OF ELEMENTS IN THE ARRAY IS DIVISIBLE BY 4 
EACH ELEMENT OF ARRAY T IS AN INTEGER WITHIN THE RANGE [-1000, 1000]
N IS AN INTEGER WITHIN THE RANGE [8, 200]
AMPLITUDES OF ALL SEASONS ARE DISTINCT
'''

def find_season(T):
    N_4 = len(T) // 4
    seasons = ["WINTER", "SPRING", "SUMMER", "AUTUMN"]
    season_amplitudes = []
    amplitudes = []
    start_season = 0
    end_season = N_4

    # splice T into 4 seasons
    for season in seasons:
        season_amplitudes.append(T[start_season:end_season])
        start_season = end_season
        end_season += N_4
    start_season = 0
    end_season = N_4
    # print(season_amplitudes)
    for season_amplitude in season_amplitudes:
        # print(season_amplitude)
        amplitude = max(season_amplitude) - min(season_amplitude)
        amplitudes.append(amplitude)
        start_season += end_season
        end_season += N_4
    return seasons[amplitudes.index(max(amplitudes))]


            



