# 数据库配置信息
HOSTNAME = "127.0.0.1"
P0RT = "3306"
USERNAME = "debian-sys-maint"
PASSWORD = "ET8f5F3qMOvqPnbM"
DATABASE = "recommend"
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{P0RT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI

SECRET_KEY = "sgddsvubva;jnkdvbhaes"