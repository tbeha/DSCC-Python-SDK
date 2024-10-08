# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.qos_policy import QosPolicy

class TestQosPolicy(unittest.TestCase):
    """QosPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QosPolicy:
        """Test QosPolicy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QosPolicy`
        """
        model = QosPolicy()
        if include_optional:
            return QosPolicy(
                qospolicy_details = dscc.models.qospolicy_details.qospolicyDetails(
                    qos_capped_objs_data = dscc.models.capped_obj_data.cappedObjData(
                        items = [
                            dscc.models.obj_data.objData(
                                customer_id = 'string', 
                                generation = 0, 
                                target_name = 'volume1', 
                                target_type = 'vv', 
                                timestampms = [
                                    1605063600
                                    ], 
                                type = 'string', )
                            ], 
                        page_limit = 1, 
                        page_offset = 1, 
                        total = 1, ), 
                    qos_un_capped_objs_data = dscc.models.uncapped_obj_data.uncappedObjData(
                        page_limit = 1, 
                        page_offset = 1, 
                        total = 1, ), 
                    recvd_total = 1, 
                    total = 1, ),
                request_uri = '/api/v1/storage-systems/device-type1/SGH014XGSP/qos-policy'
            )
        else:
            return QosPolicy(
        )
        """

    def testQosPolicy(self):
        """Test QosPolicy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
