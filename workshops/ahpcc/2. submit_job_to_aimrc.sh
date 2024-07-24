echo "Showing you the available nodes..."
echo "=================================="
sinfo

echo "Showing you the current queue..."
echo "=================================="

echo "Submitting your job to the queue..."
echo "=================================="
sbatch --partition condo --constraint 'aimrc' --nodes=1 myjob.sh

echo "Job completed."