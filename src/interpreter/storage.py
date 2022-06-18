from tokens_parser.ast_nodes import *
from interpreter.invalid_identifier_exception import InvalidIdentifierException



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
        else: 
            raise InvalidIdentifierException(symbol, line_nbr)

    def store(self, symbol : str, value : Union[int, float, str, AST_Node]) -> None:
        """Store a symbol's value in the current scope."""
        self.current_scope[symbol] = value

    def exit_scope(self) -> None:
        """Exit the current scope."""
        exited_scope = self.parent_scopes.split(" ")[-1]

        self.current_scope = self.global_scope
        for scope_name in self.parent_scopes.split(" ")[:-1]:
            self.current_scope = self.current_scope[scope_name]
        
        self.current_scope.pop(exited_scope)
        self.parent_scopes.removesuffix(" " + exited_scope)

    def enter_scope(self, scope_name : str) -> None:
        """Enter a new scope.
            Args:
                scope_name (str): the entered function's name
        """
        self.parent_scopes += " " if len(self.parent_scopes) > 0 else ""
        self.parent_scopes += scope_name
        self.current_scope[scope_name] = {}
        self.current_scope = self.current_scope[scope_name]
