#! /bin/sh

echo "--------------------------Serialized Floyd-Warshall Algorithm--------------------------"
python3 serializedFloydWarshall.py
echo "---------------------------------------------------------------------------------------\n\n"

echo "-------------------------Parallelized Floyd-Warshall Algorithm-------------------------"

echo "----------------------------------------1 Core-----------------------------------------"
mpiexec -n 1 python3 -m mpi4py parallelizedFloydWarshall.py
echo "---------------------------------------------------------------------------------------\n\n"

echo "----------------------------------------2 Cores----------------------------------------"
mpiexec -n 2 python3 -m mpi4py parallelizedFloydWarshall.py
echo "---------------------------------------------------------------------------------------\n\n"

echo "----------------------------------------4 Cores----------------------------------------"
mpiexec -n 4 python3 -m mpi4py parallelizedFloydWarshall.py
echo "---------------------------------------------------------------------------------------\n\n"

# echo "6 Cores"
# mpiexec -n 6 python3 -m mpi4py parallelizedFloydWarshall.py