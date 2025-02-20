import json
from typing import Union, Dict, Any

class JSONDifference:
    def __init__(self, json1: Union[str, dict], json2: Union[str, dict]):
        self.json1 = self._validate_input(json1)
        self.json2 = self._validate_input(json2)
    
    def _validate_input(self, input_json: Union[str, dict]) -> dict:
        """Validate and convert input to dictionary"""
        if isinstance(input_json, str):
            try:
                return json.loads(input_json)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(f"Invalid JSON string: {e.msg}", e.doc, e.pos)
        elif isinstance(input_json, dict):
            return input_json
        else:
            raise TypeError("Input must be either a JSON string or dictionary")
    
    def get_difference(self) -> Dict[str, Dict[str, Any]]:
        """Get different values and missing keys"""
        different_values = {}
        missing_keys = []
        
        # Check keys in first JSON
        for key in self.json1:
            if key not in self.json2:
                missing_keys.append(key)
            elif self.json1[key] != self.json2[key]:
                different_values[key] = {
                    'json1_value': self.json1[key],
                    'json2_value': self.json2[key]
                }
        
        return {
            'different_values': different_values,
            'missing_in_json2': missing_keys
        }

# Test 
json1 = {"name": "Aditi", "age": 22, "college": "KIIT"}
json2 = {"name": "Riddhi", "marks": 30, "country": "USA"}

diff_checker = JSONDifference(json1, json2)
result = diff_checker.get_difference()
print("Different values:", result['different_values'])
print("Missing in second JSON:", result['missing_in_json2'])