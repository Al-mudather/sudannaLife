import graphene

# from SudannaLife.categories.schema import Query as categoriesQuery
# from SudannaLife.categories.mutation import Mutation as categoriesMutation

from SudannaLife.competitions.schema import Query as competitionsQuery
from SudannaLife.competitions.mutation import Mutation as competitionsMutation

 

class Query(
        # categoriesQuery,
        competitionsQuery,
        graphene.ObjectType):
    pass


class Mutation(
        # categoriesMutation,
        competitionsMutation,
        graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
