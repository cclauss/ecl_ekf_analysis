# /usr/bin/env python3
"""
the numerical analysis
"""
from pyulog import ULog
import numpy as np


from checks.base_check import Check
import grpc_interfaces.check_data_pb2 as check_data_api
import config.thresholds as thresholds


class NumericalCheck(Check):
    """
    the numerical check.
    """
    def __init__(self, ulog: ULog):
        """
        :param ulog:
        """
        super(NumericalCheck, self).__init__(
            ulog, check_type=check_data_api.CHECK_TYPE_ECL_FILTER_FAULT_STATUS)


    def calc_statistics(self) -> None:
        """
        :return:
        """
        estimator_status_data = self.ulog.get_dataset('estimator_status').data

        filter_fault_flag = self.add_statistic(
            check_data_api.CHECK_STATISTIC_TYPE_ECL_FILTER_FAULT_FLAG)
        filter_fault_flag.value = float(
            np.amax(estimator_status_data['filter_fault_flags']))
        filter_fault_flag.thresholds.failure.value = thresholds.ecl_filter_fault_flag_failure()