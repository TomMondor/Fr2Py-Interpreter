class InvalidArgumentsException(Exception):
    def __init__(self, function_name : str, args_count : int, params_count : int):
        self.function_name = function_name
        self.args_count = args_count
        self.params_count = params_count

    def __str__(self):
        return f"InvalidArgumentsException: Function {self.function_name} expected {self.params_count} arguments, but got {self.args_count}."
