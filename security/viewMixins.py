from rest_framework import mixins
from rest_framework import viewsets


# List Create and Retrieve Function
class ListCreateRetrieveMixins(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):

    """ Class Provides basic functionality to List, Create , Retrieve and
        Update Existing Models in the Application Hierarchy
    """

    pass


# Crate and List Functions
class CreateListMixins(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    """ Class Provides basic Create and List Operations """

    pass


# Create List and Delete Functionality for the  Model
class CreateListDeleteMixins(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    """ Class Provides basic Create, List and Destroy Operations """

    pass


# Disable update functionality for the Model
class RestrictUpdateMixins(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    """ Class Provides all except Update and partial_update Operations """

    pass


# Disable delete for the given model
class RestrictDeleteMixins(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):

    """ Disable Destroy method viewsets """

    pass


# Disable Create Functionality for the Model
class RestrictCreateMixins(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):

    """ Disable Create Method. Create May be imlemented with additional
    logic if necessary when need be. """

    pass


# Update and Delete Functionality for selected Model
class UpdateDeleteMixins(mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):

    """ Provides Update and Delete Functionality """

    pass


# Retrieve Data Values from selected model
class RetrieveMixins(mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    """ Provides Retrieve  Functionality """

    pass


# Retrieve Data Values from selected model
class GetListMixins(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    """ Provides Retrieve  Functionality """

    pass
