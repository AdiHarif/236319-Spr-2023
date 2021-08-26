"""
Mini-Lisp-evaluate on Mini-Lisp-evaluate

The following file includes all the tests for evaluate on evaluate,
which based on the test: test_evaluate_1.in.lisp

For example:
    Original test:
        * (evaluate 'a '(a.x t.t nil.nil)) ; X

    New test:
        * (evaluate '(evaluate (quote a) (quote (a.X t.t nil.nil))) '(environment)) ; X

    Where environment includes all the definitions used by evaluate:
        (t.t nil.nil apply.(lambda ...) evaluate.(lambda ...) quote.(nlambda ...) ...)

Steps:
    1. Generate the latest lisp files from the Mini-lisp book.
    2. Open communication with the mini-lisp executable in Mini-Lisp.Chic.
    3. Feed the shell with all the files from the book. (create our `executable alist`)
    4. Generate environment (string) which will be used by the evaluate function,
       using all the files from the book, similar to step 2. (create our `evaluate alist`)
    5. Create our s-expression as a string (including `evaluate alist` and our `applied evaluate alist`)
    6. Feed the shell with the input s-expression.
    6. Communicate with the mini-lisp process.
    7. Compare our output with expected.
    8. If the strings are identical then the test passed, else failed and show diffs.
Environment:
    1. executable alist - our real alist from the C code, includes all functions
                          that will be feeded from the book (step 3)

    2. evaluate alist - our alist for the top evlauate function, includes all functions
                          that will be feeded from the book (step 4).
                          It (almost) similar to the executable alist, but will
                          be executed only when running the s-expression.

    3. applied evaluate alist - out alist for the applied evaluate function,
                          can be very small (e.g: (t.t nil.nil))
"""
import pytest
from framework.lib.flow_test_framework import FlowTestFramework
from framework.lib.utils import get_flow, get_env


@pytest.fixture
def flow() -> FlowTestFramework:
    """
    Return a flow loaded with all the functions
    from the latest auto-generated files from the Mini-lisp book
    """
    return get_flow(polling=True, filter_newline=False)


@pytest.fixture
def env() -> str:
    """
    Return an a-list string.
    Calculated once before the tests.
    """
    return get_env()


def test_lookup(flow, env):
    """
    Original tests:
        * (evaluate 'a '(a.T t.t nil.nil)) ; T
        * (evaluate 'a '(a.x t.t nil.nil)) ; X
    """
    raise NotImplementedError


def test_atomic_one_arguments(flow, env):
    """
    Original tests:
        * (evaluate '(atom a) '(a.x t.t nil.nil))      ; T
        * (evaluate '(atom a) '(a.(x) t.t nil.nil))    ; NIL
        * (evaluate '(car a) '(a.(x) t.t nil.nil))     ; X
        * (evaluate '(car a) '(a.(x y z) t.t nil.nil)) ; X
        * (evaluate '(car a) '(a.(x.y) t.t nil.nil))   ; X.Y
        * (evaluate '(cdr a) '(a.(x) t.t nil.nil))     ; NIL
        * (evaluate '(cdr a) '(a.(x y z) t.t nil.nil)) ; (Y Z)
        * (evaluate '(cdr a) '(a.(x.y) t.t nil.nil))   ; NIL
        * (evaluate '(eval a) '(a.x x.y t.t nil.nil))  ; Y
    """
    raise NotImplementedError


def test_atomic_two_arguments(flow, env):
    """
    Original tests:
        * (evaluate '(cons a b) '(a.x b.y t.t nil.nil))  ; (X.Y)
        * (evaluate '(cons a b) '(a.x b.x t.t nil.nil))  ; (X.X)
        * (evaluate '(eq a a) '(a.x t.t nil.nil))        ; T
        * (evaluate '(eq a b) '(a.x b.y t.t nil.nil))    ; NIL
        * (evaluate '(eq a b) '(a.x b.x t.t nil.nil))    ; T
        * (evaluate '(set a b) '(a.x b.y t.t nil.nil))   ; Y
    """
    raise NotImplementedError


def test_cond(flow, env):
    """
    Original tests:
        * (evaluate '(cond (())) '(t.t nil.nil))                    ; NIL
        * (evaluate '(cond (t nil)) '(t.t nil.nil))                 ; NIL
        * (evaluate '(cond (a t)) '(a.t t.t nil.nil))               ; T
        * (evaluate '(cond (a b)) '(a.t b.t t.t nil.nil))           ; T
        * (evaluate '(cond (t a) (nil b)) '(a.a b.b t.t nil.nil))   ; A
        * (evaluate '(cond (nil a) (t b)) '(a.a b.b t.t nil.nil))   ; B
        * (evaluate '(cond (a b) (b a)) '(a.t b.t t.t nil.nil))     ; T
        * (evaluate '(cond (a b) (b a)) '(a.nil b.t t.t nil.nil))   ; NIL
        * (evaluate '(cond (a b) (a b) (b a)) '(a.nil b.t t.t nil.nil)) ; NIL
    """
    raise NotImplementedError


def test_error(flow, env):
    """
    Original tests:
        * (evaluate '(error) '(t.t nil.nil)) ; NIL
        * (evaluate '(error a) '(a.my_err t.t nil.nil)) ; MY_ERR
    """
    raise NotImplementedError


def test_evaluate_error(flow, env):
    """
    Original tests:
        * (evaluate '(bla) '(t.t nil.nil))
        * (evaluate '(NIL NIL) '(t.t nil.nil))
    """
    raise NotImplementedError
