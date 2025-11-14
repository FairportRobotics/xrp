# Add in any imports you need here


class ComponentName:
    # Add any variables and their types here.  You access these in other methods as self.variable_name
    version: int

    def setup(self) -> None:
        # Initialization variables here.  Think of this as __init__ for the component.
        self.version = 1

    def execute(self) -> None:
        # This method executes actions based on control and informational methods.
        pass

    # Control/Informational methods below, preferably in alphabetical order

    def get_version(self) -> int:
        """Returns the version number of the component"""
        return self.version

    def set_version(self, version: int) -> None:
        """
        Sets the version number of the component
        :param version: The new version number
        """
        self.version = version
