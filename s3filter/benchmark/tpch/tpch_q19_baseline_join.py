# -*- coding: utf-8 -*-
"""TPCH Q19 Baseline Benchmark

"""

import os

from s3filter import ROOT_DIR
from s3filter.plan.query_plan import QueryPlan
from s3filter.query import tpch_q19
from s3filter.util.test_util import gen_test_id


def main():
    run(True)
    run(False)


def run(is_streamed):
    """

    :return: None
    """

    print('')
    print("TPCH Q19 Baseline Join")
    print("----------------------")

    query_plan = QueryPlan(None, is_streamed)

    # Define the operators
    lineitem_scan = query_plan.add_operator(tpch_q19.sql_scan_lineitem_select_all_op())
    part_scan = query_plan.add_operator(tpch_q19.sql_scan_part_select_all_op())
    lineitem_project = query_plan.add_operator(
        tpch_q19.project_partkey_quantity_extendedprice_discount_shipinstruct_shipmode_op())
    part_project = query_plan.add_operator(tpch_q19.project_partkey_brand_size_container_op())
    lineitem_part_join = query_plan.add_operator(tpch_q19.join_op())
    filter_op = query_plan.add_operator(tpch_q19.filter_def())
    aggregate = query_plan.add_operator(tpch_q19.aggregate_def())
    aggregate_project = query_plan.add_operator(tpch_q19.aggregate_project_def())
    collate = query_plan.add_operator(tpch_q19.collate_op())

    # Connect the operators
    lineitem_scan.connect(lineitem_project)
    part_scan.connect(part_project)
    lineitem_part_join.connect_left_producer(lineitem_project)
    lineitem_part_join.connect_right_producer(part_project)
    lineitem_part_join.connect(filter_op)
    filter_op.connect(aggregate)
    aggregate.connect(aggregate_project)
    aggregate_project.connect(collate)

    # Write the plan graph
    query_plan.write_graph(os.path.join(ROOT_DIR, "../benchmark-output"), gen_test_id())

    # Start the query
    query_plan.execute()

    # Assert the results
    # num_rows = 0
    # for t in collate.tuples():
    #     num_rows += 1
    #     print("{}:{}".format(num_rows, t))

    collate.print_tuples()

    # Write the metrics
    query_plan.print_metrics()

    field_names = ['revenue']

    assert len(collate.tuples()) == 1 + 1

    assert collate.tuples()[0] == field_names

    # NOTE: This result has been verified with the equivalent data and query on PostgreSQL
    assert collate.tuples()[1] == [3468861.097000001]


if __name__ == "__main__":
    main()