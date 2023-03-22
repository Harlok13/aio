import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, VARCHAR, Boolean, DATE


class User:
    __tablename__ = 'users'

    user_id: Column = Column(BigInteger, primary_key=True)
    username: Column = Column(VARCHAR(64), nullable=True)
    nickname: Column = Column(VARCHAR(64), nullable=False)
    status: Column = Column(Boolean, nullable=False, default='standard')
    token_count: Column = Column(BigInteger, nullable=False, default=50000)
    days_left: Column = Column(Integer, nullable=False, default=0)
    question_count: Column = Column(Integer, nullable=False, default=0)
    register_date: Column = Column(DATE, default=datetime.date.today)
    update_date: Column = Column(DATE, onupdate=datetime.date.today)

    def __str__(self) -> str:
        return f'<User: {self.user_id} - {self.nickname}>'

