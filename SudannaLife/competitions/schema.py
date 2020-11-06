import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

# Import the models
from .models import QuotationOrder
from monjid.utils import ExtendedConnection


#############################
#TODO:      Course        #
############################

# TODO: Create Course type
class QuotationOrderType(DjangoObjectType):
    class Meta:
        model = QuotationOrder
        filter_fields = {
            'customerName': ['icontains', 'istartswith']
        }
        interfaces = (relay.Node,)
        connection_class = ExtendedConnection
    

#########################################
#TODO:        The root Query            #
#########################################
class Query(graphene.AbstractType):
    all_quotation_orders = DjangoFilterConnectionField(QuotationOrderType)
    quotation_order = relay.Node.Field(QuotationOrderType)