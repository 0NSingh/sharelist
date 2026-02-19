class JWTService:
    def __init__(self,data:dict[str,any],duration:str):
        self.data=data
        self.duration=duration
    def generate_token(self):
        