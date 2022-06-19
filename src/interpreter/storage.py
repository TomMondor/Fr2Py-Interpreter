from tokens_parser.ast_nodes import *
from interpreter.invalid_identifier_exception import InvalidIdentifierException
from interpreter.invalid_function_definition_exception import InvalidFunctionDefinitionException



class Storage:
    """Storage class for the interpreter.
        Simple symbol table that does double duty as a memory space.
    """

    def __init__(self):
        self.global_scope = {}
        self.current_scope = self.global_scope
        self.parent_scopes = "" #space-separated scope names, the last being the current scope

    def get(self, symbol : str, line_nbr : int) -> Union[int, float, str, AST_Node]:
        """Get the value of a symbol.
            That includes variables and function declarations (AST_Node).
            If the symbol is not found, raises an InvalidIdentifierException.
        """
        if symbol in self.current_scope:
            return self.current_scope[symbol]
        elif symbol in self.global_scope and isinstance(self.global_scope[symbol], AST_Node):
            return self.global_scope[symbol]
        else:
            raise InvalidIdentifierException(symbol, line_nbr)

    def store(self, symbol : str, value : Union[int, float, str, AST_Node]) -> None:
        """Store a symbol's value in the current scope.
            Raises InvalidSyntaxException if trying to define a function in a scope other than the global scope."""
        if len(self.parent_scopes) != 0 and isinstance(symbol, AST_Node):
            raise InvalidFunctionDefinitionException(symbol.function_name, self.function.line_nbr)
        self.current_scope[symbol] = value

    def exit_scope(self) -> None:
        """Exit the current scope."""
        exited_scope = self.parent_scopes.split(" ")[-1]

        self.current_scope = self.global_scope
        for scope_name in self.parent_scopes.split(" ")[:-1]:
            self.current_scope = self.current_scope[scope_name]
        
        self.current_scope.pop(exited_scope)
        self.parent_scopes = self.parent_scopes.removesuffix(exited_scope)
        self.parent_scopes = self.parent_scopes.removesuffix(" ")

    def enter_scope(self, scope_name : str) -> None:
        """Enter a new scope.
            Args:
                scope_name (str): the entered function's name
        """
        scope_name = f"{scope_name}:scope"
        self.parent_scopes += " " if len(self.parent_scopes) > 0 else ""
        self.parent_scopes += scope_name
        self.current_scope[scope_name] = {}
        self.current_scope = self.current_scope[scope_name]
