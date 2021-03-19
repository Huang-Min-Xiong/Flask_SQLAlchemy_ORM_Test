#### 安裝所需套件
`pip install -r requirements.txt`

#### SQLAlchemy參考設定
- app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
- app.config['SQLALCHEMY_DATABASE_URI'] = [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
