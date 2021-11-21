from aws_cdk import (
        core,
        assertions
    )
import unittest

from cdk.cdk_stack import CdkStack

class Test(unittest.TestCase):
    # example tests. To run these tests, uncomment this file along with the example
    # resource in cdk/cdk_stack.py
    def test_sqs_queue_created(self):
        app = core.App()
        stack = CdkStack(app, "cdk")
        template = assertions.Template.from_stack(stack)

        template.has_resource_properties("AWS::SQS::Queue", {
            "VisibilityTimeout": 300
        })

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()