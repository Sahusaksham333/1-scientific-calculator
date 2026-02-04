import streamlit as st
import math

class ScientificCalculator:
    def __init__(self):
        st.set_page_config(page_title="Scientific Calculator")
        st.title("Scientific Calculator")

        # Input 1st Value
        self.num1 = st.number_input("Enter first number:", value=0.0)
        self.use_degrees = st.checkbox("Use Degrees for Trigonometric Functions (default is radians)")

        self.operation = st.radio(
            "Select Operation",
            (
                "Addition", "Subtraction", "Multiplication", "Division",
                "Power", "Square Root", "Log", "Exponential",
                "Sin", "Cos", "Tan"
            )
        )

        # Input 2nd value
        if self.operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
            self.num2 = st.number_input("Enter second number", value=1.0)
        else:
            self.num2 = None

        if st.button("Calculate"):
            self.calculate()

    def calculate(self):
        try:
            # Convert to radians if needed
            rad = math.radians(self.num1) if self.use_degrees else self.num1

            if self.operation == "Addition":
                result = self.num1 + self.num2

            elif self.operation == "Subtraction":
                result = self.num1 - self.num2

            elif self.operation == "Multiplication":
                result = self.num1 * self.num2

            elif self.operation == "Division":
                if self.num2 == 0:
                    st.error("Error: Division by zero!")
                    return
                result = self.num1 / self.num2

            elif self.operation == "Power":
                result = self.num1 ** self.num2

            elif self.operation == "Square Root":
                result = math.sqrt(self.num1)

            elif self.operation == "Log":
                result = math.log(self.num1)

            elif self.operation == "Exponential":
                result = math.exp(self.num1)

            elif self.operation == "Sin":
                result = math.sin(rad)

            elif self.operation == "Cos":
                result = math.cos(rad)

            elif self.operation == "Tan":
                result = math.tan(rad)

            st.success(f"Result: {result:.4f}")

        except Exception as e:
            st.error(f"Error: {str(e)}")


# Run app
if __name__ == "__main__":
    ScientificCalculator()
