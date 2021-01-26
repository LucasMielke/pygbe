# pygbe

**pygbe** is a library with functions to get data from IBGE (Brazilian Institute of Geography and Statistics) via API

## Required libraries

1. pandas
2. pandas.io.json >> json_normalize
3. requests


## Functions

**`igbe_pam(ano="2019",var="216",loc="1",geo="1",rel="5457")`:**
Returns a pandas dataframe with "Pesquisa Agrícola Municipal" for the required year (ano) and location. The dataframe contains all cultures.

Ano (string): Year consulted. Default = 2019.
Var (string): Variables. Default = 216
loc (string): Location classification. Default = 1 (Country level)
geo (string): Location. Default = 1 (Brazil).
rel (string): report. Default = 5457

**`ibge_help(a="pt")`:** Return some instructions. a="pt (default) is for portuguese. Other values returns instructions in english.
