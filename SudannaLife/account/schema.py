import graphene
from graphql_jwt.decorators import login_required, token_auth

from graphene import relay , ObjectType
from graphene.relay.node import Node
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from graphene_file_upload.scalars import Upload
from rest_framework.reverse import reverse as api_reverse
# Import the models
from .models import  User



########################
#TODO: UserType  #
########################
#User type
class UserModelType(DjangoObjectType):
    # image_url = graphene.String()

    class Meta:
        model  = User
        filter_fields = {
            'username': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)
    
    # def resolve_image_url(self, info):
    #     image_url = self.get_image_url()
    #     return  api_reverse("graphql-view", request=info.context).replace("/graphql","") + image_url[1:]

#########################################
#TODO:        The root Query            #
#########################################
class Query(graphene.AbstractType): 
    #TODO:UserProfile Queries
    all_workers           = DjangoFilterConnectionField(UserModelType)
    worker                = relay.Node.Field(UserModelType)    
    # get_user = graphene.Field(UserType, id=graphene.Int())

    @login_required
    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    # @login_required
    # def resolve_user(self, info, **kwargs):
    #     return info.context.user

    # @login_required
    def resolve_get_user(self, info, id, **kwargs):
        return User.objects.get(pk=id)

    