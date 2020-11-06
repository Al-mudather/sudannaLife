import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from SudannaLife.competitions.models import Contest, Contestor
from SudannaLife.utils import ExtendedConnection

 
#############################
#TODO:     Contest          #
#############################

# TODO: Create Contest type
class ContestType(DjangoObjectType):
    class Meta:
        model = Contest
        filter_fields = ['ar_title','en_title']
        interfaces = (relay.Node,)
        connection_class = ExtendedConnection

#############################
#TODO:     Contestor          #
#############################

# TODO: Create Contestor type
class ContestorType(DjangoObjectType):
    class Meta:
        model = Contestor
        filter_fields = ['fname']
        interfaces = (relay.Node,)
        connection_class = ExtendedConnection
    

#########################################
#TODO:        The root Query            #
#########################################
class Query(graphene.AbstractType):
    #TODO: Contest
    all_contests = DjangoFilterConnectionField(ContestType)
    contest = relay.Node.Field(ContestType)
    #TODO: Contestor
    all_contestors = DjangoFilterConnectionField(ContestorType)
    contestor = relay.Node.Field(ContestorType)