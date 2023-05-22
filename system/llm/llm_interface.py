# -*- coding: utf-8 -*-
# Purpose: abstract interface for all aigc api

class LLMInterface(object):
    def __init__(self):
        pass

    def InterfaceGetSupplyName(self):
        raise NotImplementedError

    def InterfaceGetAllModelNames(self):
        raise NotImplementedError

    def InterfaceChatRequest(self, **kwargs):
        raise NotImplementedError

    def InterfaceEmbeddingRequest(self, **kwargs):
        raise NotImplementedError

    def InterfaceGetEstimateCost(self, **kwargs):
        raise NotImplementedError

    def InterfaceIsValid(self):
        raise NotImplementedError