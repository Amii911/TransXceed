from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import (User, Investment, Transaction)

if name == 'main':
    engine = create_engine("sqlite:///transxceed.db")
    session = Session(engine, future=True)

    import ipdb; ipdb.set_trace()

