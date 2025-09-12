from pydantic import BaseModel

class ExpectedMessageData(BaseModel):
    expected_message: str

class UserGreetingData(BaseModel):
    user_greeting: str

class WelcomePageData(BaseModel):
    ExpectedMessageData: ExpectedMessageData
    UserGreetingData: UserGreetingData