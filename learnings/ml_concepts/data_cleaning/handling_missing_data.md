# Missing data

## types of missingness

### MCAR

### MAR

### MNAR

## How to handle missing data

### Remove Rows
- Best if MCAR (safe removal) or small proportion missing even if MAR.
- Remove only if a small percentage of rows have missing values.
- Remove if many columns are missing for that row and imputation is unreliable.
### Remove Column
- Remove if too many values are missing (commonly >40–60%).
- Best if MCAR or MAR and feature isn't critical.
- Remove if feature is not important (Low variance/weak correlation).
- Remove if imputation is impractical or produces noise.

### Not do anything
- the algo can handle missing values (XGBoost)
- the missing data is meaningful
- if MNAR

### Create a new column to say whether another column had missing value or not
- missing data is meaningful
- data is MAR or MNAR
- 

### Imputation 
- data set is not huge (dropping leads to waste data)
- MCAR or MAR
- feature is important


#### Imputation technique depends on the type of data (numerical or categorical)

#### mean/median/mode imputation

#### Zero imputation (set to 0)

#### random imputation (take random value)

#### KNN/ linear regression imputation

#### ICE imputation

#### Model based imputation
- Random Forest Imputation
- XGBoost / LightGBM imputation
- Neural network-based imputation

#### Forward fill (FFILL) → use previous value
#### Backward fill (BFILL) → use next value
