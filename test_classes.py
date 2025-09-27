from test_result import TestResult
from test_loader import TestLoader
from test_loader_test import TestLoaderTest
from test_runner import TestRunner

# Testando com Teste Loader
result = TestResult()
loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)
suite.run(result)
print(result.summary())

# Testando com Teste Runner
loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)