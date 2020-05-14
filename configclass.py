import json

class Config():
    def __init__(self,problem_data,solution_data):
        self.problem_name = problem_data['problem_name']
        self.start_time = problem_data['start_time']
        self.end_time = problem_data['end_time']
        self.echo_level = problem_data['echo_level']
        self.solution_name = solution_data['solution_name']
        self.solution_data = solution_data['solution_data']

    @classmethod
    def from_json(cls,json_file):
        json_dict = json.loads(json_file.read())
        return cls(**json_dict)

    def __repr__(self):
        return f'Config {self.problem_name,self.start_time,self.end_time,self.echo_level,self.solution_name,self.solution_data}'

with open ('config.json','r') as json_file:
    config = Config.from_json(json_file)
    print(config)