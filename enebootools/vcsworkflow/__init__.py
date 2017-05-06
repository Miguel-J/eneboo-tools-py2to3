# encoding: UTF-8
import enebootools
from enebootools import EnebooToolsInterface
import sys, traceback

class VCSInterface(EnebooToolsInterface):
    module_description = "Herramientas para la integración con un VCS"

class GITInterface(VCSInterface):
    module_description = "Herramientas para la integración con GIT"
