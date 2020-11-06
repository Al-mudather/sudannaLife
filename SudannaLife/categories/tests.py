import json
from graphene_django.utils.testing import GraphQLTestCase
# GraphQLTestCase.
from monjid.schema import schema

class QoutationOrderTestcases(GraphQLTestCase):
    ''' 
        for versions before v2.13 you need to define a schema
        on the GraphQLTestCase class
    '''
    GRAPHQL_SCHEMA = schema

    def test_get_all_car_models(self):
        response = self.query(
            ''' 
                mutation CreateQuotationOrder {
                createQuotationOrder (data: {
                    customerName: "mudather",
                    phoneNumber: "",
                    orderNumber: "",
                    lat: "",
                    lon: "",
                    carModel: "",
                    carType: "",
                    industryDate: "",
                    tireType: "",
                    tireService: "",
                    tireServicePrice: "",
                    jumpStartupPrice: "",
                    batteryPurchasePrice: "",
                    batteryType: "",
                    batteryServiceType: "",
                    batteryCapacity: "",
                    carState: "",
                    towingServicePrice: "",
                    oilType: "",
                    filterType: "",
                    currentCounter: "",
                    oilPrice: "",
                    filterPrice: "",
                    carLiterCapacity: "",
                    oilChangePrice: "",
                    washType: "",
                    carWashPrice: "",
                    tireCompany: "",
                    tireSize: "",
                    tireUnit: "",
                    productType: "",
                    productUnit: "",
                    productPrice: ""
                    
                }) {
                    quotationOrder {
                    customerName,
                    phoneNumber,
                    orderNumber,
                    lat,
                    lon,
                    carModel {
                        id,
                        name
                    },
                    carType {
                        id,
                        name
                    },
                    industryDate {
                        id,
                        name
                    },
                    tireType {
                        id,
                        name
                    },
                    tireService {
                        id,
                        name
                    },
                    tireServicePrice,
                    jumpStartupPrice,
                    batteryPurchasePrice,
                    batteryType {
                        id,
                        name
                    },
                    batteryServiceType {
                        id,
                        name
                    },
                    batteryCapacity {
                        id,
                        name
                    },
                    carState {
                        id,
                        name
                    },
                    towingServicePrice,
                    oilType {
                        id,
                        name
                    },
                    filterType {
                        id,
                        name
                    },
                    currentCounter,
                    oilPrice,
                    filterPrice,
                    carLiterCapacity {
                        id,
                        name
                    },
                    oilChangePrice,
                    washType {
                        id,
                        name
                    },
                    carWashPrice,
                    tireCompany {
                        id,
                        name
                    },
                    tireSize,
                    tireUnit,
                    productType,
                    productUnit,
                    productPrice
                    }
                }
                }
            ''',
            op_name='createQuotationOrder'
        )

        content = json.loads(response.content)
        # This validates the status code and if you get errors
        # self.assertResponseNoErrors(response)