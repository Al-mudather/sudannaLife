import graphene
import json

from graphene import relay, ObjectType
from graphene.relay.node import Node

# Import the models
from .models import  QuotationOrder


from .schema import QuotationOrderType
from monjid.config.models import ( 
    CarModel,
    CarType ,
    IndustryDate,
    BatteryType,
    BatteryServiceType,
    BatteryCapacity,
    State,
    OilType,
    FilterType,
    TireCompany,
    TireSize,
    TireType,
    TireService,
    WashType,
    LiterCapacity
    )


from monjid.utils import HelperCLass

# TODO: Create quotationOrder input


class quotationOrderInput(graphene.InputObjectType):
    #TODO: Customer information
    customerName = graphene.String(required=True)
    phoneNumber = graphene.String(blank=True, null=True)
    orderNumber = graphene.String(blank=True, null=True)
    location = graphene.String(blank=True, null=True)
    lat = graphene.String(blank=True, null=True)
    lon = graphene.String(blank=True, null=True)

    #TODO: car information
    carModel = graphene.List(graphene.ID, blank=True, null=True)
    carType = graphene.List(graphene.ID, blank=True, null=True)
    industryDate  = graphene.List(graphene.ID, blank=True, null=True)

    #TODO: Tire Service
    tireType = graphene.List(graphene.ID, blank=True, null=True)
    tireService = graphene.List(graphene.ID, blank=True, null=True)
    tireServicePrice = graphene.Float(blank=True, null=True)

    #TODO: Jump Startup
    jumpStartupPrice = graphene.Float(blank=True, null=True)

    #TODO: Battery Purchase
    batteryPurchasePrice = graphene.Float(blank=True, null=True)

    #TODO: Battery info
    batteryType = graphene.List(graphene.ID, blank=True, null=True)
    batteryServiceType = graphene.List(graphene.ID, blank=True, null=True)
    batteryCapacity = graphene.List(graphene.ID, blank=True, null=True)

    #TODO: Towing Services
    fromLocation = graphene.String(blank=True, null=True)
    toLocation = graphene.String(blank=True, null=True)
    km = graphene.String(blank=True, null=True)
    carState = graphene.List(graphene.ID, blank=True, null=True)
    towingServicePrice = graphene.Float(blank=True, null=True)

    #TODO: Oil Change
    oilType = graphene.List(graphene.ID, blank=True, null=True)
    filterType = graphene.List(graphene.ID, blank=True, null=True)
    currentCounter = graphene.Float(blank=True, null=True)
    oilPrice = graphene.Float(blank=True, null=True)
    filterPrice = graphene.Float(blank=True, null=True)
    carLiterCapacity = graphene.List(graphene.ID, blank=True, null=True)
    # Depends on oilPrice and filterPrice
    oilChangePrice = graphene.Float(blank=True, null=True)

    #TODO: Car Wash
    washType = graphene.List(graphene.ID, blank=True, null=True)
    carWashPrice = graphene.Float(blank=True, null=True)

    #TODO: Tite Purchase
    tireCompany = graphene.List(graphene.ID, blank=True, null=True)
    tireSize = graphene.String(blank=True, null=True)
    tireUnit = graphene.String(blank=True, null=True)
    tirePurchasePrice = graphene.Float(blank=True, null=True)

    #TODO: Product
    productType = graphene.String(blank=True, null=True)
    productUnit = graphene.String(blank=True, null=True)
    productPrice = graphene.Float(blank=True, null=True)

    #TODO: Date Time
    quotationOrderDate = graphene.DateTime(blank=True, null=True)

# TODO: Create quotationOrder mutation
class CreateQuotationOrderMutation(graphene.Mutation):
    quotationOrder = graphene.Field(QuotationOrderType)

    class Arguments:
        data = quotationOrderInput()

    def mutate(self, info, data, **kwargs):
        # TODO: Use CreateModelData to create the static data of the
        # quotationOrder automaticlly without the relational
        # This function will retrun the intialized object so you must call .save()
        # after you finished
        quotationOrder_obj = HelperCLass.CreateModelData(self, data=data, model=QuotationOrder)
        
        #TODO: Set all the model relational
        # quotationOrder_obj = self.set_all_relational_models(quotationOrder_obj)
        # TODO: IF the carModel reletion relation exists
        ''' 
        Remember you need to send from the front-end a null value for all the relationship data
        that you don't need, not an empty string for the proceding code to work.
        EX:  carModel = null =>> not carModel = ['']

        '''
        try:
            carModel_obj = None
            if data.carModel is not None:
                carModel_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.carModel, model=CarModel)
        except:
            carModel_obj = None
        # If exists
        if carModel_obj:
            # Set the entended quotationOrder carModel
            quotationOrder_obj.carModel = carModel_obj
        
        # TODO: IF the carType reletion relation exists
        try:
            carType_obj = None
            if data.carType is not None:
                carType_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.carType, model=CarType)
        except:
            carType_obj = None
        # If exists
        if carType_obj:
            # Set the entended quotationOrder carType
            quotationOrder_obj.carType = carType_obj

        # TODO: IF the carType reletion relation exists
        try:
            carType_obj = None
            if data.carType is not None:
                carType_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.carType, model=CarType)
        except:
            carType_obj = None
        # If exists
        if carType_obj:
            # Set the entended quotationOrder carType
            quotationOrder_obj.carType = carType_obj
        
        # TODO: IF the industryDate reletion relation exists
        try:
            industryDate_obj = None
            if data.industryDate is not None:
                industryDate_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.industryDate, model=IndustryDate)
        except:
            industryDate_obj = None
        # If exists
        if industryDate_obj:
            # Set the entended quotationOrder industryDate
            quotationOrder_obj.industryDate = industryDate_obj
        
        # TODO: IF the tireType reletion relation exists
        try:
            tireType_obj = None
            if data.tireType is not None:
                tireType_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.tireType, model=TireType)
        except:
            tireType_obj = None
        # If exists
        if tireType_obj:
            # Set the entended quotationOrder tireType
            quotationOrder_obj.tireType = tireType_obj
        
        # TODO: IF the tireService reletion relation exists
        try:
            tireService_obj = None
            if data.tireService is not None:
                tireService_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.tireService, model=TireService)
        except:
            tireService_obj = None
        # If exists
        if tireService_obj:
            # Set the entended quotationOrder tireService
            quotationOrder_obj.tireService = tireService_obj
        
        # TODO: IF the batteryType reletion relation exists
        try:
            batteryType_obj = None
            if data.batteryType is not None:
                batteryType_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.batteryType, model=BatteryType)
        except:
            batteryType_obj = None
        # If exists
        if batteryType_obj:
            # Set the entended quotationOrder batteryType
            quotationOrder_obj.batteryType = batteryType_obj
        
        # TODO: IF the batteryServiceType reletion relation exists
        try:
            batteryServiceType_obj = None
            if data.batteryServiceType is not None:
                batteryServiceType_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.batteryServiceType, model=BatteryServiceType)
        except:
            batteryServiceType_obj = None
        # If exists
        if batteryServiceType_obj:
            # Set the entended quotationOrder batteryServiceType
            quotationOrder_obj.batteryServiceType = batteryServiceType_obj
        
        # TODO: IF the batteryCapacity reletion relation exists
        try:
            batteryCapacity_obj = None
            if data.batteryCapacity is not None:
                batteryCapacity_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.batteryCapacity, model=BatteryCapacity)
        except:
            batteryCapacity_obj = None
        # If exists
        if batteryCapacity_obj:
            # Set the entended quotationOrder batteryCapacity
            quotationOrder_obj.batteryCapacity = batteryCapacity_obj
        
        # TODO: IF the carState reletion relation exists
        try:
            carState_obj = None
            if data.carState is not None:
                carState_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.carState, model=State)
        except:
            carState_obj = None
        # If exists
        if carState_obj:
            # Set the entended quotationOrder carState
            quotationOrder_obj.carState = carState_obj
        
        # TODO: IF the oilType reletion relation exists
        try:
            oilType_obj = None
            if data.oilType is not None:
                oilType_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.oilType, model=OilType)
        except:
            oilType_obj = None
        # If exists
        if oilType_obj:
            # Set the entended quotationOrder oilType
            quotationOrder_obj.oilType = oilType_obj
        
        # TODO: IF the filterType reletion relation exists
        try:
            filterType_obj = None
            if data.filterType is not None:
                filterType_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.filterType, model=FilterType)
        except:
            filterType_obj = None
        # If exists
        if filterType_obj:
            # Set the entended quotationOrder filterType
            quotationOrder_obj.filterType = filterType_obj
        
        # TODO: IF the carLiterCapacity reletion relation exists
        try:
            carLiterCapacity_obj = None
            if data.carLiterCapacity is not None:
                carLiterCapacity_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.carLiterCapacity, model=LiterCapacity)
        except:
            carLiterCapacity_obj = None
        # If exists
        if carLiterCapacity_obj:
            # Set the entended quotationOrder carLiterCapacity
            quotationOrder_obj.carLiterCapacity = carLiterCapacity_obj
        
        # TODO: IF the washType reletion relation exists
        try:
            washType_obj = None
            if data.washType is not None:
                washType_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.washType, model=WashType)
        except:
            washType_obj = None
        # If exists
        if washType_obj:
            # Set the entended quotationOrder washType
            quotationOrder_obj.washType = washType_obj
        
        # TODO: IF the tireCompany reletion relation exists
        try:
            tireCompany_obj = None
            if data.tireCompany is not None:
                tireCompany_obj = HelperCLass.setRelationalModelData(
                    self, relational=data.tireCompany, model=TireCompany)
        except:
            tireCompany_obj = None
        # If exists
        if tireCompany_obj:
            # Set the entended quotationOrder tireCompany
            quotationOrder_obj.tireCompany = tireCompany_obj

        # # TODO: Save the changes before adding the Many2Many relational
        quotationOrder_obj.save()
        return CreateQuotationOrderMutation(quotationOrder=quotationOrder_obj)

    # def set_all_relational_models(self, model):
    #     ''' 
    #         This function for set all the relation ship
    #         between this model and all it's related models
    #     '''
    #     # TODO: IF the carModel reletion relation exists
    #     try:
    #         carModel_obj = None
    #         if data.carModel is not None:
    #             carModel_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.carModel, model=CarModel)
    #     except:
    #         carModel_obj = None
    #     # If exists
    #     if carModel_obj:
    #         # Set the entended quotationOrder carModel
    #         model.carModel = carModel_obj
        
    #     # TODO: IF the carType reletion relation exists
    #     try:
    #         carType_obj = None
    #         if data.carType is not None:
    #             carType_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.carType, model=CarType)
    #     except:
    #         carType_obj = None
    #     # If exists
    #     if carType_obj:
    #         # Set the entended quotationOrder carType
    #         model.carType = carType_obj

    #     # TODO: IF the carType reletion relation exists
    #     try:
    #         carType_obj = None
    #         if data.carType is not None:
    #             carType_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.carType, model=CarType)
    #     except:
    #         carType_obj = None
    #     # If exists
    #     if carType_obj:
    #         # Set the entended quotationOrder carType
    #         model.carType = carType_obj
        
    #     # TODO: IF the industryDate reletion relation exists
    #     try:
    #         industryDate_obj = None
    #         if data.industryDate is not None:
    #             industryDate_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.industryDate, model=IndustryDate)
    #     except:
    #         industryDate_obj = None
    #     # If exists
    #     if industryDate_obj:
    #         # Set the entended quotationOrder industryDate
    #         model.industryDate = industryDate_obj
        
    #     # TODO: IF the tireType reletion relation exists
    #     try:
    #         tireType_obj = None
    #         if data.tireType is not None:
    #             tireType_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.tireType, model=TireType)
    #     except:
    #         tireType_obj = None
    #     # If exists
    #     if tireType_obj:
    #         # Set the entended quotationOrder tireType
    #         model.tireType = tireType_obj
        
    #     # TODO: IF the tireService reletion relation exists
    #     try:
    #         tireService_obj = None
    #         if data.tireService is not None:
    #             tireService_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.tireService, model=TireService)
    #     except:
    #         tireService_obj = None
    #     # If exists
    #     if tireService_obj:
    #         # Set the entended quotationOrder tireService
    #         model.tireService = tireService_obj
        
    #     # TODO: IF the batteryType reletion relation exists
    #     try:
    #         batteryType_obj = None
    #         if data.batteryType is not None:
    #             batteryType_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.batteryType, model=BatteryType)
    #     except:
    #         batteryType_obj = None
    #     # If exists
    #     if batteryType_obj:
    #         # Set the entended quotationOrder batteryType
    #         model.batteryType = batteryType_obj
        
    #     # TODO: IF the batteryServiceType reletion relation exists
    #     try:
    #         batteryServiceType_obj = None
    #         if data.batteryServiceType is not None:
    #             batteryServiceType_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.batteryServiceType, model=BatteryServiceType)
    #     except:
    #         batteryServiceType_obj = None
    #     # If exists
    #     if batteryServiceType_obj:
    #         # Set the entended quotationOrder batteryServiceType
    #         model.batteryServiceType = batteryServiceType_obj
        
    #     # TODO: IF the batteryCapacity reletion relation exists
    #     try:
    #         batteryCapacity_obj = None
    #         if data.batteryCapacity is not None:
    #             batteryCapacity_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.batteryCapacity, model=BatteryCapacity)
    #     except:
    #         batteryCapacity_obj = None
    #     # If exists
    #     if batteryCapacity_obj:
    #         # Set the entended quotationOrder batteryCapacity
    #         model.batteryCapacity = batteryCapacity_obj
        
    #     # TODO: IF the carState reletion relation exists
    #     try:
    #         carState_obj = None
    #         if data.carState is not None:
    #             carState_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.carState, model=CarState)
    #     except:
    #         carState_obj = None
    #     # If exists
    #     if carState_obj:
    #         # Set the entended quotationOrder carState
    #         model.carState = carState_obj
        
    #     # TODO: IF the oilType reletion relation exists
    #     try:
    #         oilType_obj = None
    #         if data.oilType is not None:
    #             oilType_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.oilType, model=OilType)
    #     except:
    #         oilType_obj = None
    #     # If exists
    #     if oilType_obj:
    #         # Set the entended quotationOrder oilType
    #         model.oilType = oilType_obj
        
    #     # TODO: IF the filterType reletion relation exists
    #     try:
    #         filterType_obj = None
    #         if data.filterType is not None:
    #             filterType_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.filterType, model=FilterType)
    #     except:
    #         filterType_obj = None
    #     # If exists
    #     if filterType_obj:
    #         # Set the entended quotationOrder filterType
    #         model.filterType = filterType_obj
        
    #     # TODO: IF the carLiterCapacity reletion relation exists
    #     try:
    #         carLiterCapacity_obj = None
    #         if data.carLiterCapacity is not None:
    #             carLiterCapacity_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.carLiterCapacity, model=CarLiterCapacity)
    #     except:
    #         carLiterCapacity_obj = None
    #     # If exists
    #     if carLiterCapacity_obj:
    #         # Set the entended quotationOrder carLiterCapacity
    #         model.carLiterCapacity = carLiterCapacity_obj
        
    #     # TODO: IF the washType reletion relation exists
    #     try:
    #         washType_obj = None
    #         if data.washType is not None:
    #             washType_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.washType, model=WashType)
    #     except:
    #         washType_obj = None
    #     # If exists
    #     if washType_obj:
    #         # Set the entended quotationOrder washType
    #         model.washType = washType_obj
        
    #     # TODO: IF the tireCompany reletion relation exists
    #     try:
    #         tireCompany_obj = None
    #         if data.tireCompany is not None:
    #             tireCompany_obj = HelperCLass.setRelationalModelData(
    #                 self, relational=data.tireCompany, model=TireCompany)
    #     except:
    #         tireCompany_obj = None
    #     # If exists
    #     if tireCompany_obj:
    #         # Set the entended quotationOrder tireCompany
    #         model.tireCompany = tireCompany_obj

    #     return model
    


#########################################
#TODO:        The root Mutation         #
#########################################


class Mutation(ObjectType):
    create_quotation_order = CreateQuotationOrderMutation.Field()

