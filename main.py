from data._DATA_     import ROWS
from schema.config   import HEADER, COLUMNS_ONEHOT, COLUMNS_METADATA
from tools.csv_tools import create_csv, read_csv
from tools.onehot    import create_csv_onehot


PATH_DATA_       = 'data/DATA_.csv'
PATH_DATA_BINARY = 'data/DATA_BINARY.csv'

create_csv(PATH_DATA_, HEADER, ROWS)

df = read_csv(PATH_DATA_, COLUMNS_METADATA)
create_csv_onehot(df, PATH_DATA_BINARY, COLUMNS_ONEHOT, COLUMNS_METADATA)
