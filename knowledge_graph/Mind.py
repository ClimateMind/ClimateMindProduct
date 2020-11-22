import sys

from owlready2 import get_ontology
from typing import List

from knowledge_graph import ontology_processing_utils


Results = List[str]


class Mind:
    def __init__(self):
        self.__ontology_source = "./climate_mind_ontology"
        self.__ontology = self.__load_ontology()

    def __load_ontology(self):
        try:
            onto = get_ontology(self.__ontology_source).load()
            obj_properties = list(onto.object_properties())
            [ontology_processing_utils.give_alias(x) for x in obj_properties]
            return onto

        except (FileNotFoundError, IsADirectoryError, ValueError):
            raise

    def _get_ontology(self):
        try:
            if self.__ontology is None:
                raise ValueError
            return self.__ontology
        except ValueError:
            raise

    def search(self, query: str) -> Results:
        try:
            return make_network.get_edges(self._get_ontology(), query)
        except (ValueError, AttributeError):
            raise ValueError

    def multiParameterSearch(self) -> Results:
        try:
            return make_network.get_edges(self._get_ontology(), None)
        except (ValueError, AttributeError):
            raise ValueError
