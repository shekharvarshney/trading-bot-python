import abc
from typing import TypeVar, Generic, List
from core.fxtrading.account.account import Account

T = TypeVar('T')

class AccountDataProvider(Generic[T],metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_account_info(self, account_id: T) -> Account[T]:
        raise NotImplementedError('developers must implement get_account_info to use this base class')
    @abc.abstractmethod
    def get_accounts_info(self) -> List[Account[T]]:
        raise NotImplementedError('developers must implement get_accounts_info to use this base class')
