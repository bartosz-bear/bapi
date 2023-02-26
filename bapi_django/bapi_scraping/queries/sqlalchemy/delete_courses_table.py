'''
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
#from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy.orm import Session

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"

    #id: Mapped[int] = mapped_column(primary_key=True)
    #name: Mapped[str] = mapped_column(String(30))
    #fullname: Mapped[Optional[str]]

    #def __repr__(self) -> str:
    #    return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

    
class Course(Base):
    __tablename__ = "bapi_scraping_courses4"

    #id: Mapped[int] = mapped_column(primary_key=True)
    #category: Mapped(str) = mapped_column()

def delete_courses_table(engine):

  with Session(engine) as session:
      
      #courses = Course()

      Course.__bapi_scraping_courses4__drop()

      session.commit()
   
  print('success')


from sqlalchemy import delete

stmt = delete(user_table).where(user_table.c.name == 'patrick')
'''