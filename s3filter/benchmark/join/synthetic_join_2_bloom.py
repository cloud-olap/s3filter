# -*- coding: utf-8 -*-
"""Synthetic Bloom Join Benchmarks

"""
from s3filter.benchmark.join import runner
from s3filter.query.join import synthetic_join_bloom
from s3filter.query.join.synthetic_join_settings import SyntheticBloomJoinSettings
from s3filter.util.test_util import gen_test_id


def main():
    settings = SyntheticBloomJoinSettings(
        parallel=True, use_pandas=True, secure=False, use_native=False, buffer_size=0,
        use_shared_mem=False, shared_memory_size=-1, sf=1,
        table_A_key='customer',
        table_A_parts=2,
        table_A_sharded=False,
        table_A_field_names=['c_custkey'],
        table_A_filter_sql='cast(c_custkey as int) <= 100',
        table_A_AB_join_key='c_custkey',
        table_B_key='orders',
        table_B_parts=2,
        table_B_sharded=False,
        table_B_field_names=['o_orderkey', 'o_custkey', 'o_orderdate', 'o_shippriority', 'o_totalprice'],
        table_B_filter_sql='cast(o_orderdate as timestamp) < cast(\'1992-01-15\' as timestamp)',
        table_B_AB_join_key='o_custkey',
        table_B_BC_join_key=None,
        table_B_detail_field_name='o_totalprice',
        table_C_key=None,
        table_C_parts=None,
        table_C_sharded=None,
        table_C_field_names=None,
        table_C_filter_sql=None,
        table_C_BC_join_key=None,
        table_C_detail_field_name=None)

    # expected_result = 1171288505.15
    expected_result = 868482.17

    query_plan = synthetic_join_bloom.query_plan(settings)

    runner.run(query_plan, expected_result=expected_result, test_id=gen_test_id())


if __name__ == "__main__":
    main()