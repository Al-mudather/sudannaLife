import graphene
from graphene import relay
from graphql_jwt.exceptions import PermissionDenied
from graphene.relay.node import Node

class CustomNode(graphene.Node):
    pk = graphene.Int()

    class Meta:
        name = 'MyNode'

    def resolve_pk(self, info):
        return self.id


def auth_resolver(attname, default_value, root, info, **args):
    if info.context.user.is_authenticated:
        return getattr(root, attname, default_value)
    raise PermissionDenied()


class ExtendedConnection(relay.Connection):
    class Meta:
        abstract = True

    total_count = graphene.Int()
    edge_count = graphene.Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length

    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)

class HelperCLass:
    # TODO: Reusable object model deletion
    def deleteOneItem(self, id, model):
        # Decode the id
        if type(id) == str:
            _, id = Node.from_global_id(id)  # parsing global id to (type, id)
        try:
            # search about the item by id
            model_qs = model.objects.get(id=id)
            # Make initial message
            message = f"This item of id ( {model_qs.id} ) can not be deleted"
            # If the item exists
            if model_qs:
                # Delete the item
                model.delete(model_qs)
                # Make success message
                message = f"This item was deleted successfully"
                item = None
                ok = True 
        except TypeError as e:
            message = e
            item = None
            ok = False

        return {"item": item, "message": message, 'ok': ok}

    # TODO: Reusable filling model relation data
    def setRelationalModelData(self, relational, model):
        # Get the encripted id
        multi_objects = []
        for id in relational:
            # Get the parsed id from the encripted id
            if type(id) == str:
                # parsing global id to (type, id)
                _, id = Node.from_global_id(id)
            # Find the entended parent category bu the id
            relational_object = model.objects.get(pk=id)
            multi_objects.append(relational_object)
        if multi_objects:
            if len(relational) > 1:
                return multi_objects
            return multi_objects[0]

        return None

    # TODO: General Updata Function
    def UpdateModelData(self, id, data, model):
        try:
            model_obj = model.objects.get(id=id)
        except TypeError as e:
            return "The item was not found"

        for key in data:
            try:

                # TODO: Do not update any empty string
                if type(data[key]) is str:
                    str_val = data[key].strip()
                    if str_val is not None and str_val != '':
                        model_obj.__dict__[key] = str_val
                        
                    else:
                        model_obj.__dict__[key] = model_obj.__dict__[key]
                else:
                    model_obj.__dict__[
                        key] = data[key] if data[key] is not None else model_obj.__dict__[key]

                try:
                    # TODO: Update the relations models , but many2many relation has a differnet approach.
                    # Only (one2One & foreignKey)
                    if model_obj.__dict__[key+"_id"] or model_obj.__dict__[key+"_id"] is None:
                        id = data[key][0]
                        if type(id) == str:
                            _, id = Node.from_global_id(id)
                        model_obj.__dict__[key+"_id"] = id

                except:
                    pass
            except:
                pass
        
        return model_obj

    # TODO: General Create Function
    def CreateModelData(self, data, model):

        model_obj = model()
        for key in data:
            try:
                model_obj.__dict__[key] = data[key]
            except Exception as e:
                # print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                # print(e)
                # print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                pass
        return model_obj
