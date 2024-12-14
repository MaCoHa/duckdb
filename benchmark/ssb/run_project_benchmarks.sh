#!/bin/bash
#take all
# all thread test
build/release/benchmark/benchmark_runner "benchmark/ssb/sf1/.*" --threads=1 --out=timings_sf1_t1.csv --log=log_sf1_t1.json --detailed-profile
build/release/benchmark/benchmark_runner "benchmark/ssb/sf1/.*" --threads=4 --out=timings_sf1_t4.csv --log=log_sf1_t4.json --detailed-profile
build/release/benchmark/benchmark_runner "benchmark/ssb/sf1/.*" --threads=8 --out=timings_sf1_t8.csv --log=log_sf1_t8.json --detailed-profile
# all query test q01, q07, q12
build/release/benchmark/benchmark_runner "benchmark/ssb/sf1/.*" --threads=4 --out=timings_sf1_t4.csv --log=log_sf1_t4.json --detailed-profile
build/release/benchmark/benchmark_runner "benchmark/ssb/sf10/.*" --threads=4 --out=timings_sf10_t4.csv --log=log_sf10_t4.json --detailed-profile
build/release/benchmark/benchmark_runner "benchmark/ssb/sf100/.*" --threads=4 --out=timings_sf100_t4.csv --log=log_sf100_t4.json --detailed-profile


build/release/benchmark/benchmark_runner "benchmark/ssb/sf10/.*" --threads=4 --out=timings_Q1_DP.csv --detailed-profile
build/release/benchmark/benchmark_runner "benchmark/ssb/sf10/.*" --threads=4 --out=timings_Q1_P.csv --profile
build/release/benchmark/benchmark_runner "benchmark/ssb/sf10/.*" --threads=4 --out=timings_Q1_NP.csv 





