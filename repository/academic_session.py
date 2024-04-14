from database.schema import AcademicSession
from beanie import PydanticObjectId
from validation import CreateAcademicSession
from typing import List


class AcademicSessionRepository:


    @staticmethod
    async def add_academic_session(session: CreateAcademicSession):

        query = AcademicSession(session=session.session, semester=session.semester)

        query.save()

        return query
    

    @staticmethod
    async def get_all_academic_session():

        pipeline = [
            {
                "$project": {
                    "id": { "$toString": "$_id" },
                    "session": 1,
                    "semester": 1
                }
            }
        ]

        query = AcademicSession.objects.aggregate(*pipeline)

        return query

