class MessageRequest(BaseModel):
    message: str
    bot_role: str
    user_id: str
