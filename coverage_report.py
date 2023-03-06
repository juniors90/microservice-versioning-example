import unittest
import sys
from coverage import Coverage

if __name__ == "__main__":
    cov = Coverage(source=["application"])
    cov.start()
    tests = unittest.TestLoader().discover("tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        cov.stop()
        cov.save()
        cov.report()
        cov.html_report(directory="coverage_report")
        cov.xml_report(outfile="coverage.xml")
        sys.exit(0)
    sys.exit(1)
