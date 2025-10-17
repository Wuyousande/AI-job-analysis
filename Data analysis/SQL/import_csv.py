import pandas as pd
from sqlalchemy import create_engine

# === 配置你的数据库连接 ===
db_user = 'root'        # 替换为你的用户名
db_pass = 'YHYztt9664.@'   # 替换为你的密码
db_host = 'localhost'
db_name = 'learn_sql'   # 替换为你要导入到的数据库

# === 替换为你的 CSV 文件路径 ===
csv_file = '8月成交数据.csv'  # 文件和当前脚本在同一目录下
table_name = 'august_data'   # 你想导入成什么表名（避免中文）

# === 读取 CSV 文件 ===
df = pd.read_csv(csv_file, encoding='utf-8')  # 如果失败换成 'utf-8-sig'

# === 连接数据库 ===
engine = create_engine(f'mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}?charset=utf8mb4')

# === 导入数据 ===
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

print(f"✅ 数据成功导入表 {table_name}")