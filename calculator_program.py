number_types = (int, float, complex)


class Calculator:

    @staticmethod
    def validate_args(x_var, y_var):
        if not isinstance(x_var, number_types) and not isinstance(y_var, number_types):
            raise ValueError

    def add(self, x_var, y_var):
        self.validate_args(x_var, y_var)
        return x_var + y_var

    def multiply(self, x_var, y_var):
        self.validate_args(x_var, y_var)
        return x_var*y_var

    def sub(self, x_var, y_var):
        self.validate_args(x_var, y_var)
        return x_var-y_var

    def div(self, x_var, y_var):
        self.validate_args(x_var, y_var)
        return x_var/y_var

