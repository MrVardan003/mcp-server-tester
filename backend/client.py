class MCPClient:
    def __init__(self, installation_code, api_key, config):
        self.installation_code = installation_code
        self.api_key = api_key
        self.config = config

    async def call(self, json_input):
        # Simulate a dummy API response for now
        return {"status": "success", "data": json_input}
