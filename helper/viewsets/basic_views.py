from rest_framework import mixins
from rest_framework import viewsets


class ListCreateRetrieveViewSets(mixins.CreateModelMixin,
                                 mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 viewsets.GenericViewSet):

    """ Class Provides basic functionality to List, Create , Retrieve and
        Update Existing Models in the Application Hierarchy
    """

    pass


class CreateListViewSets(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """ Class Provides basic Create and List Operations """

    pass


class CreateListDeleteViewSets(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    """ Class Provides basic Create, List and Destroy Operations """

    pass


class RestrictUpdateViewSets(mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.ListModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    """ Class Provides all except Update and partial_update Operations """

    pass


class RestrictDeleteViewsets(mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.ListModelMixin,
                             mixins.UpdateModelMixin,
                             viewsets.GenericViewSet):

    """ Disable Destroy method viewsets """

    pass


class RestrictCreateViewsets(mixins.RetrieveModelMixin,
                             mixins.ListModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):

    """ Disable Create Method. Create May be imlemented with additional
    logic if necessary when need be. """

    pass


class UpdateDeleteViewsets(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):

    """ Provides Update and Delete Functionality """

    pass
