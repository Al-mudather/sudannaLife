import graphene
import json

from graphene import relay, ObjectType
from graphene.relay.node import Node

from SudannaLife.competitions.models import Contest,Contestor
from SudannaLife.account.models import User, Country
from SudannaLife.categories.models import Category


from .schema import ContestType, ContestorType



from SudannaLife.utils import HelperCLass

#########################################
#TODO:        Contest Mutations         #
#########################################


# TODO: Create Contest input

class ContestInput(graphene.InputObjectType):
    ar_title = graphene.String(required=True)
    en_title = graphene.String(blank=True, null=True)
    ar_description = graphene.String(blank=True, null=True)
    en_description = graphene.String(blank=True, null=True)

    logo = graphene.String(blank=True, null=True)
    slogan = graphene.String(blank=True, null=True)

    categories = graphene.List(graphene.ID, blank=True, null=True)
    
    start_at = graphene.DateTime(blank=True, null=True)
    end_at = graphene.DateTime(blank=True, null=True)

# TODO: Create Contest mutation
class CreateContestMutation(graphene.Mutation):
    contest = graphene.Field(ContestType)

    class Arguments:
        data = ContestInput()

    def mutate(self, info, data, **kwargs):
        # TODO: Use CreateModelData to create the static data of the
        contest_obj = HelperCLass.CreateModelData(self, data=data, model=Contest)
        
        #TODO: Set all the model relational
        # contest_obj = self.set_all_relational_models(Contest_obj)
        # TODO: IF the carModel reletion relation exists
        ''' 
        Remember you need to send from the front-end a null value for all the relationship data
        that you don't need, not an empty string for the proceding code to work.
        EX:  carModel = null =>> not carModel = ['']

        '''

        # TODO: IF the category reletion relation exists
        try:
            category_obj = None
            if data.categories is not None:
                category_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.categories, model=Category)
        except:
            category_obj = None
        # If exists
        if category_obj:
            # Set the entended Contest category
            contest_obj.categories = category_obj

        # # TODO: Save the changes before adding the Many2Many relational
        contest_obj.save()
        return CreateContestMutation(contest=contest_obj)

# TODO: Create Contest mutation
class UpdateContestMutation(graphene.Mutation):
    contest = graphene.Field(ContestType)

    class Arguments:
        id = graphene.ID()
        data = ContestInput()

    def mutate(self, info, id, data, **kwargs):
        # Decode the id to get an integer id
        _, id = Node.from_global_id(id)
        # TODO: Call the update method to update any model automaticlly
        contest_obj = HelperCLass.UpdateModelData(
            self, id=id, data=data, model=Contest)
        contest_obj.save()
        return UpdateContestMutation(contest=contest_obj)

# TODO: Delete Contest mutation
class DeleteContestMutation(graphene.Mutation):
    message = graphene.String()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id, **kwargs):
        # Delete the Contest
        result = HelperCLass.deleteOneItem(self, id=id, model=Contest)
        # Return the result
        return DeleteContestMutation(ok=result["ok"], message=result["message"])


#########################################
#TODO:        Contestor Mutations       #
#########################################
# TODO: Create Contestor input

class ContestorInput(graphene.InputObjectType):
    fname = graphene.String(required=True)
    rest_name = graphene.String(blank=True, null=True)
    email = graphene.String(blank=True, null=True)
    avatar = graphene.String(blank=True, null=True)

    phone = graphene.String(blank=True, null=True)
    password = graphene.String(blank=True, null=True)

    account = graphene.List(graphene.ID, blank=True, null=True)
    country = graphene.List(graphene.ID, blank=True, null=True)
    
    start_at = graphene.DateTime(blank=True, null=True)
    end_at = graphene.DateTime(blank=True, null=True)

# TODO: Create Contestor mutation
class CreateContestorMutation(graphene.Mutation):
    contestor = graphene.Field(ContestorType)

    class Arguments:
        data = ContestorInput()

    def mutate(self, info, data, **kwargs):
        # TODO: Use CreateModelData to create the static data of the
        contestor_obj = HelperCLass.CreateModelData(self, data=data, model=Contestor)
        
        #TODO: Set all the model relational
        # contestor_obj = self.set_all_relational_models(Contestor_obj)
        # TODO: IF the carModel reletion relation exists
        ''' 
        Remember you need to send from the front-end a null value for all the relationship data
        that you don't need, not an empty string for the proceding code to work.
        EX:  carModel = null =>> not carModel = ['']

        '''

        # TODO: IF the account reletion relation exists
        try:
            account_obj = None
            if data.account is not None:
                account_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.account, model=User)
        except:
            account_obj = None
        # If exists
        if account_obj:
            # Set the entended Contestor account
            contestor_obj.account = account_obj
        
        # TODO: IF the country reletion relation exists
        try:
            country_obj = None
            if data.country is not None:
                country_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.country, model=Country)
        except:
            country_obj = None
        # If exists
        if country_obj:
            # Set the entended Contestor country
            contestor_obj.country = country_obj

        # # TODO: Save the changes before adding the Many2Many relational
        contestor_obj.save()
        return CreateContestorMutation(contestor=contestor_obj)

# TODO: Create Contestor mutation
class UpdateContestorMutation(graphene.Mutation):
    contestor = graphene.Field(ContestorType)

    class Arguments:
        id = graphene.ID()
        data = ContestorInput()

    def mutate(self, info, id, data, **kwargs):
        # Decode the id to get an integer id
        _, id = Node.from_global_id(id)
        # TODO: Call the update method to update any model automaticlly
        contestor_obj = HelperCLass.UpdateModelData(
            self, id=id, data=data, model=Contestor)
        contestor_obj.save()
        return UpdateContestorMutation(contestor=contestor_obj)

# TODO: Delete Contestor mutation
class DeleteContestorMutation(graphene.Mutation):
    message = graphene.String()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id, **kwargs):
        # Delete the Contestor
        result = HelperCLass.deleteOneItem(self, id=id, model=Contestor)
        # Return the result
        return DeleteContestorMutation(ok=result["ok"], message=result["message"])

#########################################
#TODO:        The root Mutation         #
#########################################


class Mutation(ObjectType):
    #TODO: Contest Mutations
    create_contest= CreateContestMutation.Field()
    update_contest= UpdateContestMutation.Field()
    delete_contest= DeleteContestMutation.Field()
    #TODO: Contestor Mutations
    create_contestor= CreateContestorMutation.Field()
    update_contestor= UpdateContestorMutation.Field()
    delete_contestor= DeleteContestorMutation.Field()

