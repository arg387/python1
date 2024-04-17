import sympy as sp
from sympy.parsing.latex import parse_latex

def main():
    # Define the LaTeX equation string directly
    equation_string = "b_{\\grad} = \\frac{x_c}{2}|\\nabla{c}|^2"

    def parse_latex_to_sympy(latex_string):
        return parse_latex(latex_string)

    def equations(expressions):
        print("Math Equations:")
        print("----------------")
        for idx, expr in enumerate(expressions, start=1):
            latex_string = sp.latex(expr)
            print(f"{idx}.")
            print(sp.pretty(expr, use_unicode=True, wrap_line=False))  # Use unicode characters for formatting
            print()

    # Parse the LaTeX equation string to SymPy expression
    sympy_expression = parse_latex_to_sympy(equation_string)

    # Display the equation
    equations([sympy_expression])

# Call the function
main()