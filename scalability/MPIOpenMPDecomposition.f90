! MPI/OpenMP Decomposition for PiNet-Manager Scalability
PROGRAM mpi_openmp_decomposition
  IMPLICIT NONE
  INCLUDE 'mpif.h'
  INTEGER, PARAMETER :: num_tiles = 100
  INTEGER, PARAMETER :: num_ranks = 4
  INTEGER :: ij, i, j, k
  REAL :: v_phytmp(num_tiles, num_ranks), u_phytmp(num_tiles, num_ranks)

  CALL MPI_INIT(ierr)
  CALL MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierr)
  CALL MPI_COMM_SIZE(MPI_COMM_WORLD, num_ranks, ierr)

  !$OMP PARALLEL DO &
  !$OMP PRIVATE (ij, i, j, k)
  DO ij = 1, num_tiles
    DO j = j_start(ij), j_end(ij)
      DO k = kms, kme
        DO i = i_start(ij), i_end(ij)
          v_phytmp(i, k, j) = 0
          u_phytmp(i, k, j) = 0
        END DO
      END DO
    END DO
  END DO

  CALL MPI_FINALIZE(ierr)
END PROGRAM mpi_openmp_decomposition
