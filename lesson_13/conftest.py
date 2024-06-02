import pytest
from CompanyApi import CompanyApi

@pytest.fixture(scope="session")
def client():
    return CompanyApi("https://x-clients-be.onrender.com")

#@pytest.fixture(autouse=True)
#def my_first():
#   pass
