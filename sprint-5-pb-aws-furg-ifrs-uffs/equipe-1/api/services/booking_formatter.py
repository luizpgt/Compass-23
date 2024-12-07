from schemas.Booking import Booking
import pandas as pd

def dummy_transform(data: Booking) -> list:
    
    booking = list(data.__dict__.values())

    # list of values of each column to be dummy transformed
    series = [
        ['Aviation', 'Complementary', 'Corporate', 'Offline', 'Online'],
        ['Meal Plan 1', 'Meal Plan 2', 'Meal Plan 3', 'Not Selected'],
        ['Room_Type 1', 'Room_Type 2', 'Room_Type 3', 'Room_Type 4', 'Room_Type 5', 'Room_Type 6', 'Room_Type 7'],
    ]

    # persists dataframes with a dummy transform of each serie of values
    dfs = []
    for serie in series:
        dfs.append(pd.get_dummies(pd.Series(serie), dtype=int))

    # concat all dataframes. 
    # permits consulting a single dataframe to get dummy values
    fdf = pd.concat(dfs, axis=1)

    # get a list with 'dummied' booking values
    dummied_booking_values = []
    for item in booking:
        if (type(item) == str):
            dummies = list(fdf[item])
            while pd.isna(dummies[-1]): dummies.pop()
            dummied_booking_values += dummies
        else:
            dummied_booking_values.append(item)

    return list(map(int, dummied_booking_values))