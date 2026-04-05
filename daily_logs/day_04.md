# Day 04 — Memory, dtypes, and how PySpark actually works

## Context
Loading 8 tables into pandas for the Home Credit project surfaced some
questions worth understanding properly.

## How pandas loads data into RAM
When you call pd.read_csv(), the entire file is pulled off disk and held
in RAM as a live Python object. Disk is permanent storage, RAM is your
working space — fast but limited. All 8 tables together estimate ~7.8 GB,
which is significant on a single machine.

The Task Manager number will often be lower than that estimate because:
- deep=True in memory_usage() counts Python object overhead for strings,
  which slightly overestimates real usage
- Python's memory allocator doesn't always release memory back to the OS
  immediately, so the number lags

## Why dtype matters
int64 = 8 bytes per value. int32 = 4 bytes. On a 27M row table, that's
~100 MB saved per column. pandas defaults everything to int64 or float64
unless told otherwise. On a single machine you're working within one
machine's RAM limit, so starting lean gives you headroom as feature
engineering adds more columns.

## How PySpark distributes data
PySpark splits data into partitions and distributes them across worker
nodes. Each worker holds only its slice in its own RAM — no single machine
holds the full dataset. Transformations like groupby run locally on each
worker's partition first, then partial results are combined (MapReduce).

What we still worry about in PySpark:
- Shuffles: data moving between workers across the network is expensive
- Skew: one oversized partition means one worker does all the work
- Driver memory: .collect() pulls everything to one machine — never do
  this on large data in production

## Key takeaway
pandas = single machine, you manage memory.
PySpark = distributed, memory is the cluster's problem.
Shuffles and skew become yours instead.