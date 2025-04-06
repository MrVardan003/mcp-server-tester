import json
import asyncio
from client import MCPClient

# Helper function to run async functions in sync context
def run_async(coro):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:  # Happens in threads without a loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

def run_tests(installation_code, api_key, config, valid_json_input):
    async def perform_tests():
        results = {}

        try:
            config_dict = json.loads(config) if config else {}
        except json.JSONDecodeError:
            config_dict = {}

        try:
            valid_input = json.loads(valid_json_input)
        except json.JSONDecodeError:
            valid_input = valid_json_input  # For wrong input test case

        test_cases = {
            "No Config, Correct API_KEY, Right Input": {
                "config": {},
                "api_key": api_key,
                "input": valid_input
            },
            "Correct Config, Correct API_KEY, Right Input": {
                "config": config_dict,
                "api_key": api_key,
                "input": valid_input
            },
            "Wrong Config, Correct API_KEY, Right Input": {
                "config": {"wrong": True},
                "api_key": api_key,
                "input": valid_input
            },
            "Correct Config, Wrong API_KEY, Right Input": {
                "config": config_dict,
                "api_key": "WRONG_API_KEY",
                "input": valid_input
            },
            "Correct Config, Correct API_KEY, Wrong Input": {
                "config": config_dict,
                "api_key": api_key,
                "input": "{"  # invalid JSON
            }
        }

        for case_name, test in test_cases.items():
            try:
                client = MCPClient(
                    installation_code=installation_code,
                    api_key=test["api_key"],
                    config=test["config"]
                )
                result = await client.call(test["input"])
                results[case_name] = {
                    "status": "Success",
                    "message": "succeeded"
                }
            except Exception as e:
                results[case_name] = {
                    "status": "Failed",
                    "message": str(e)
                }

        return results

    return run_async(perform_tests())
