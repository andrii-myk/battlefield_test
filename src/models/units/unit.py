from abc import ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta):
    """Abstract class which describes unit"""
    @abstractmethod
    def set_recharge(self):
        raise NotImplementedError("Please implement <set_recharge> method")

    @abstractmethod
    def damage(self):
        raise NotImplementedError("Please implement <damage> method")

    @abstractmethod
    def under_attack(self, damage):
        raise NotImplementedError("Please implement <under_attack> method")

    @abstractmethod
    def increase_exp(self):
        raise NotImplementedError("Please implement <increase_exp> method")

    @abstractmethod
    def compute_att_succ_prob(self):
        raise NotImplementedError("Please implement <compute_att_succ_prob> method")