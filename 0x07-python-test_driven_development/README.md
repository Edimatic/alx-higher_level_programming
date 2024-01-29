				0x07 Python - Test-driven development 

Test-driven development (TDD) is a software development methodology that emphasizes writing tests before writing the actual code. The process involves short development cycles where you write a test, then write the minimum amount of code to make the test pass, and finally refactor the code while ensuring that the tests continue to pass. This cycle is often referred to as the "Red-Green-Refactor" cycle:

    Red: Write a failing test that describes the desired functionality.
    Green: Write the minimum amount of code necessary to make the test pass.
    Refactor: Refactor the code while keeping the tests passing.

The key steps in TDD are as follows:

    Write a Test:
        Before writing any production code, write a test that defines a function or improves an existing function. This test should be small, focused, and cover a specific piece of functionality.
        Initially, the test is expected to fail since the corresponding code doesn't exist.

    Run the Test:
        Run all the tests in the test suite to ensure that the new test fails. This validates that the test is correctly checking for the desired functionality.

    Write the Code:
        Write the minimum amount of code necessary to make the test pass. The goal is not to write perfect or complete code but to make the test pass.

    Run the Tests:
        Run the test suite again to ensure that the newly written code, as well as the existing code, hasn't broken any functionality. All tests should pass.

    Refactor:
        Refactor the code while ensuring that the tests continue to pass. Refactoring may involve improving code readability, removing duplication, or optimizing performance.

    Repeat:
        Repeat the process by writing additional tests for new functionality or improving existing tests. This iterative cycle helps improve code quality and maintainability.
