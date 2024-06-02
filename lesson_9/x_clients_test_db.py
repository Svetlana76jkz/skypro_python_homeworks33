from CompanydbApi import CompanydbApi
from CompanyTable import CompanyTable

api = CompanydbApi("https://x-clients-be.onrender.com")
db = CompanyTable("postgres://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")

def test_get_companies():
    api_result = api.get_company_list() # получить список из api
    db_result = db.get_companies()# получить список из БД
    assert len(api_result) == len(db_result)# сравнить списки, что они равны

def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={"active": "c true"})
    db_list = db.get_active_companies()
    assert len(filtered_list) > len(db_list)

def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    name = "Autotest"
    descr = "Descr"
    result = api.create_company(name=name, description=descr)
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    db.delete(new_id)

    assert len_after - len_before == 1

    for company in body:
        if company["id"] == new_id:
            assert company["name"] == name
            assert company["description"] == descr
            assert company["id"] == new_id

def test_get_one_company():
    name = 'Skypro'
    db.create('Skypro')
    max_id = db.get_max_id()
   
    new_company = api.get_company(max_id)

    db.delete(max_id)
    
    assert new_company["id"] == max_id
    assert new_company["name"] == name
    # доработать db.create так, чтобы описание пробрасовалось в базу
    #assert new_company["description"] == descr
    assert new_company["isActive"] == True

def test_edit():
    name = 'Skypro'
    db.create('Skypro')
    max_id = db.get_max_id()

    new_name = "Updated"
    new_descr = "_upd_"

    edited = api.edit(max_id, new_name, new_descr)
    db.delete(max_id)

    assert edited["id"] == max_id
    assert edited["name"] == new_name
    assert edited["description"] == new_descr
    assert edited["isActive"] == True

def test_delete():
    name = 'Skypro'
    db.create('Skypro')
    max_id = db.get_max_id()

    deleted = api.delete(max_id)
    
    assert deleted["id"] == max_id
    assert deleted["name"] == name
    # доработать db.create так, чтобы описание пробрасовалось в базу
    # assert deleted["description"] == descr
    assert deleted["isActive"] == True

    rows = db.get_company_by_id(max_id)
    assert len(rows) == 0

def test_deactivate():
    name = 'Skypro'
    db.create('Skypro')
    max_id = db.get_max_id()

    body = api.set_active_state(max_id, False)

    db.delete(max_id)

    assert body["isActive"] == False

def test_deactivate_and_activate_back():
    name = 'Skypro'
    db.create('Skypro')
    max_id = db.get_max_id()

    api.set_active_state(max_id, False)

    body = api.set_active_state(max_id, True)
    db.delete(max_id)
    assert body["isActive"] == True    
