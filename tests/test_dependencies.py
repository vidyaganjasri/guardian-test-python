"""
Dependency Compatibility Tests
If ANY test fails → build fails → RAG suggests fix.
"""


class TestFlask:

    def test_import(self):
        import flask
        assert flask is not None

    def test_app_creation(self):
        from flask import Flask
        app = Flask(__name__)
        assert app is not None


class TestNumpy:

    def test_import(self):
        import numpy as np
        assert np is not None

    def test_array_creation(self):
        import numpy as np
        arr = np.array([1, 2, 3])
        assert arr.sum() == 6

    def test_numpy_string_type(self):
        """
        np.string_ exists in numpy 1.x
        np.string_ removed in numpy 2.0
        PASSES on numpy 1.26.4
        FAILS on numpy 2.1.3
        """
        import numpy as np
        val = np.string_("hello")
        assert val == b"hello"
