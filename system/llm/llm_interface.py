# -*- coding: utf-8 -*-
# Purpose: abstract interface for all aigc api

class LLMInterface(object):

    class ReasonCode(object):
        SUCCESS = 0
        FAILED = 1
        NEW_REPLY = 2

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