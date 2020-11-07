import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required, token_auth
from graphene import ObjectType
from graphene.relay.node import Node
from graphene_django.types import ErrorType


from SudannaLife.utils import HelperCLass

# Import the models
from .models import User
from .schema import UserModelType

#################################
# TODO: User Mutations    #
#################################
# TODO: Create User input
class UserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)


# TODO: Create User mutation
class CreateUserMutation(graphene.Mutation):
    user = graphene.Field(UserModelType)
 
    class Arguments:
        data = UserInput()

    def mutate(self, info, data, **kwargs):

        # user_obj = User(
        #     username=data["username"],
        #     email=data["email"],
        #     is_instructor=data["is_instructor"],
        #     phone_number=data["phone_number"],
        # )
        user_obj = HelperCLass.CreateModelData(self, data=data, model=User)
        user_obj.set_password(data["password"])

        if user_obj:
            user_obj.save()
            return CreateUserMutation(user=user_obj)
        return CreateUserMutation(user=None)


# TODO: Update User mutation
class UpdateUserMutation(graphene.Mutation):
    user = graphene.Field(UserModelType)

    class Arguments:
        id = graphene.ID()
        data = UserInput()

    def mutate(self, info, id, data, **kwargs):
        # Get the intended to update state by the provided id
        if type(id) == str:
            _, id = Node.from_global_id(id)  # parsing global id to (type, id)
        # TODO:Using the generic Updata function
        model_obj = HelperCLass.UpdateModelData(
            self, id=id, data=data, model=User
        )
        return UpdateUserMutation(user=model_obj)


# TODO: Delete User mutation
class DeleteUserMutation(graphene.Mutation):
    user = graphene.Field(UserModelType)
    message = graphene.String()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id, **kwargs):
        # Delete the User
        result = HelperCLass.deleteOneItem(self, id=id, model=User)
        # Return the result
        return DeleteUserMutation(user=result["item"], message=result["message"])


#########################################
# TODO:        Othentication         #
#########################################
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserModelType)

    @classmethod
    @token_auth
    def mutate(cls, root, info, **kwargs):
        return cls.resolve(root, info, **kwargs)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        # print(info.context.user)
        return cls(user=info.context.user)



#########################################
# TODO:        The root Mutation         #
#########################################
class Mutation(ObjectType):
    # TODO: User
    create_User = CreateUserMutation.Field()
    update_User = UpdateUserMutation.Field()
    delete_User = DeleteUserMutation.Field()

    # TODO: Authentication
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
