# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API

    The version of the OpenAPI document: 1.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dscc.models.create_quorum_witness_input import CreateQuorumWitnessInput

class TestCreateQuorumWitnessInput(unittest.TestCase):
    """CreateQuorumWitnessInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateQuorumWitnessInput:
        """Test CreateQuorumWitnessInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateQuorumWitnessInput`
        """
        model = CreateQuorumWitnessInput()
        if include_optional:
            return CreateQuorumWitnessInput(
                parameters = dscc.models.create_quorum_witness_input_parameters.CreateQuorumWitnessInput_parameters(
                    ip_address = '15.112.47.239', 
                    port = 8843, 
                    ssl = True, ),
                replication_partner_system_id = '7CE816P0SR',
                src_replication_id = 'afb4961e47212e5bc88dd35db5be5c83',
                start_quorum_witness = True,
                target_replication_id = 'afb4961e47212e5bc88dd35db5be5c83'
            )
        else:
            return CreateQuorumWitnessInput(
                parameters = dscc.models.create_quorum_witness_input_parameters.CreateQuorumWitnessInput_parameters(
                    ip_address = '15.112.47.239', 
                    port = 8843, 
                    ssl = True, ),
                replication_partner_system_id = '7CE816P0SR',
                src_replication_id = 'afb4961e47212e5bc88dd35db5be5c83',
                target_replication_id = 'afb4961e47212e5bc88dd35db5be5c83',
        )
        """

    def testCreateQuorumWitnessInput(self):
        """Test CreateQuorumWitnessInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
