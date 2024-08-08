# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.task_properties_source_resource import TaskPropertiesSourceResource

class TestTaskPropertiesSourceResource(unittest.TestCase):
    """TaskPropertiesSourceResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskPropertiesSourceResource:
        """Test TaskPropertiesSourceResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskPropertiesSourceResource`
        """
        model = TaskPropertiesSourceResource()
        if include_optional:
            return TaskPropertiesSourceResource(
                name = '',
                resource_uri = '',
                type = ''
            )
        else:
            return TaskPropertiesSourceResource(
                resource_uri = '',
                type = '',
        )
        """

    def testTaskPropertiesSourceResource(self):
        """Test TaskPropertiesSourceResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
