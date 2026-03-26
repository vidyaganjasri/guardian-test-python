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

    def test_numpy_legacy_types(self):
        """
        PASSES on numpy 1.x
        FAILS on numpy 2.x — np.bool, np.int, np.float were removed
        """
        import numpy as np
        value = np.bool(True)
        count = np.int(42)
        ratio = np.float(3.14)
        assert value == True
        assert count == 42
        assert ratio == 3.14
