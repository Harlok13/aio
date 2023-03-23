from collections import namedtuple
from typing import Union

from sqlalchemy import text, update, select
from sqlalchemy.orm import sessionmaker

from bot_ai.data.schemas.user_model import User

ProfileInfo = namedtuple('ProfileInfo', ('nickname', 'question_count', 'token_count', 'days_left', 'status'))


class UserRequest:
    def __init__(self, session: sessionmaker):
        self.session: sessionmaker = session

    @staticmethod
    def set_days_left(
            current_status: str,
            purchased_status: str,
            days_left: int,
            days_sub: int
    ) -> int:
        """
        If the current status is the same as the one being purchased, then the number
        of subscription days increases. Otherwise, the counter is reset to zero and takes
        the standard value for the subscription
        :param current_status: current status of the user subscription
        :param purchased_status: purchased status of the user subscription
        :param days_left: days left in the subscription
        :param days_sub: number of days in the purchased subscription
        :return: days left in the subscription
        """
        if current_status == purchased_status:
            return days_left + days_sub
        return days_sub

    @staticmethod
    def set_tokens(
            current_status: str,
            purchased_status: str,
            current_tokens: int,
            purchased_tokens
    ) -> Union[str, int]:
        """
        If the current status is unlimited, then the number of tokens is unlimited.
        if the current status matches the one being acquired, then the number of tokens
        does not change. If the status is different, the number of tokens takes the
        value that is in the subscription
        :param current_status: current status of the user subscription
        :param purchased_status: purchased status of the user subscription
        :param current_tokens: current number of tokens of the user
        :param purchased_tokens: purchased number of tokens of the user
        :return: number of tokens or the string 'unlimited' if the status is unlimited
        """
        if purchased_status == 'unlimited':
            return 'unlimited'
        elif current_status == purchased_status and current_status:
            return current_tokens
        return purchased_tokens

    async def set_subscription(
            self,
            purchased_status: str,
            user_id: int,
            days_sub: int,
            purchased_tokens: Union[int, str],
    ) -> None:
        """
        Set paid subscription status for user in database
        :param purchased_tokens: number of tokens purchased
        :param days_sub: number of days of subscription
        :param purchased_status: subscription type to be set
        :param user_id: just a user id in telegram
        :return:
        """
        print('set_default_sub', purchased_status, user_id)
        async with self.session.begin():
            stmt_get: ChunckedIteratorResult = await self.session.execute(  # type: ignore
                select(User.token_count, User.days_left, User.status).where(User.user_id == user_id)
            )
            token_count, days_left, current_status = stmt_get.fetchall()[0]

            stmt_set = update(User).where(User.user_id == user_id).values(
                status=purchased_status,
                days_left=self.set_days_left(
                    current_status,
                    purchased_status,
                    days_left,
                    days_sub
                ),
                token_count=self.set_tokens(
                    current_status,
                    purchased_status,
                    token_count,
                    purchased_tokens
                )
            )

        await self.session.execute(stmt_set)  # type: ignore
        await self.session.commit()  # type: ignore

    async def get_profile_info(self, user_id: int) -> ProfileInfo:
        """Get profile info from database"""
        print('get_profile_info', user_id)
        stmt_get: ChunckedIteratorResult = await self.session.execute(  # type: ignore
            select(
                User.nickname, User.question_count, User.token_count, User.days_left, User.status
            ).where(User.user_id == user_id)
        )
        # print(stmt_get.fetchall())

        profile: ProfileInfo = ProfileInfo(*stmt_get.fetchall()[0])
        return profile

    async def increase_question_count(self, user_id: int) -> None:
        """
        Increase question count for user in database
        :param user_id: just a user id in telegram
        :return:
        """
        async with self.session.begin():
            stmt_get: ChunckedIteratorResult = await self.session.execute(  # type: ignore
                select(User.question_count).where(User.user_id == user_id)
            )
            question_count = stmt_get.fetchall()[0][0] + 1
            stmt_set = update(User).where(User.user_id == user_id).values(
                question_count=question_count
            )
        await self.session.execute(stmt_set)  # type: ignore
        await self.session.commit()  # type: ignore

