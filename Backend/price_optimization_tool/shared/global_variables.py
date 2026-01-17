import configparser

cp=configparser.ConfigParser()
cp.read("price_optimization_tool/config.ini")

# MYSQL DETAILS
USERNAME=cp.get('mysql', 'username')
PASSWORD=cp.get('mysql', 'password')
HOST=cp.get('mysql','host')
DB_NAME=cp.get('mysql', 'db_name')

DEAFULT_ROLE=cp.get('role', 'default_role')
ADMIN_ROLE="admin"
VIEWER_ROLE="viewer"
BUYER_ROLE="buyer"
SUPPLIER_ROLE="supplier"