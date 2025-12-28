from enum import Enum


class ForgotPasswordAction(str, Enum):
    CONTACTADMIN = "ContactAdmin"
    INNETWORKREQUIRED = "InNetworkRequired"
    PINCODE = "PinCode"

    def __str__(self) -> str:
        return str(self.value)
