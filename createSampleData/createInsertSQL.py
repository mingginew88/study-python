import pandas as pd


######################################################
# 조건
# 칼럼명 리스트
column_name_list = ['TEST_NM', 'TEST_ADDR', 'TEST_TEL', 'TEST_DT', 'TEST_WORD']
# 데이터 타입 리스트
type_list = ['VARCHAR2(100)', 'VARCHAR2(200)', 'VARCHAR2(30)', 'DATE', 'VARCHAR2(3000)']
schema_name = 'co'
table_name = 'TEST'
number_type_list = ['NUMBER', 'INT', 'TINYINT', 'BIGINT']
######################################################

df = pd.DataFrame()
process_df = pd.DataFrame()

## CSV 불러오기
def load_csv():
    global df
    df = pd.read_csv(f'./files/sampleData.csv')

## INSERT 문 생성
def create_insert_sql():
    global df, process_df
    temp_list = []
    text = 'INSERT INTO ' + str(schema_name) + '.' + str(table_name) + '(' + ', '.join(column_name_list) + ') VALUES '

    process_df = text + '('
    for idx, val in enumerate(df.columns):

        if str(type_list[idx]).upper() in number_type_list:
            if idx == int(len(df.columns) - 1):
                process_df += df[val]
            else:
                process_df += df[val] + ', '
        else:
            if idx == int(len(df.columns) - 1):
                process_df += '\'' + df[val] + '\''
            else:
                process_df += '\'' + df[val] + '\', '
    process_df += ');'



## CSV 생성
def create_csv():
    process_df.to_csv('./files/insertSQL.csv', index=False, encoding='utf-8', header=None)


load_csv()
create_insert_sql()
create_csv()
