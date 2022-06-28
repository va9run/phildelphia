##    a) Shape of the data which is the total number of rows and columns (75757 * 64) (# Picture)
##   b) Looked for the data types and columns with null values
###        i) Three Categorical columns and rest Numerical (`State_Factor, building_class, facility_type`)
###       ii) Columns with Missing values: (`year_built, energy_star_rating, direction_max_wind_speed, direction_peak_wind_speed, max_wind_speed, days_with_fog`)
###        iii) `year_built` is in float data type, it needs to be converted into Integer as year can't be float