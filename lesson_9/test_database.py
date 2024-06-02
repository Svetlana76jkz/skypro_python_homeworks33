from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgres://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet"

def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[0] == company

def test_select():
    # Подключились к БД
    db = create_engine(db_connection_string) 
    rows = db.execute("select * from company").fetchall() 

    assert row1["id"] == 111
    assert row1["name"] == "Барбершоп 'ЦирюльникЪ'"

def test_select_one_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")

    rows = db.execute(sql_statement, company_id = 112).fetchall() 

    assert len(rows) == 1
    assert rows[0]["name"] == "Кондитерская Профи-тролли"

def test_select_one_row_wiht_two_filters():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where \"isActive\" = :isActive and id >= :id")
    # 1 способ
    my_params = {
        "id": 113,
        "isActive": True
    }
    rows = db.execute(sql_statement, my_params).fetchall()
    # 2 способ
    rows = db.execute(sql_statement, isActive = true, id = 113).fetchall() 

    assert len(rows) == 2

def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into company(\"name\") values(:new_name)")

    rows = db.execute(sql, new_name = 'SkyPro')

def test_update():
    db = create_engine(db_connection_string)
    sql = text("update company set description = :descr where id = :id")

    db.execute(sql, descr = 'New Descr', id = 162)   

def test_delete():
     db = create_engine(db_connection_string)         
     sql = text("delete from company where id = :id") 
     db.execute(sql, id = 162) 
   
