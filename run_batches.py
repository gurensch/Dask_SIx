import time
import numpy as np
from dask import as_completed
from dask.distributed import Client, LocalCluster
cluster = LocalCluster(threads_per_worker = 2, n_workers = 4, processes = True)
client = Client(cluster) 

def run_batches(max_ens, min_ens, lat, batches, model):
    total_start = time.time()
    num_ens = min_ens.shape[0]
    num_lats = min_ens.shape[1]
    size = int(num_lats / batches)
    spring_index = []
    freeze_index = []
    counter = 0
    for ens in range(0, num_ens):
        sn = [None] * batches
        fn = [None] * batches
        futures = [
            client.submit(model, max_ens[ens, size*r:size*(r+1),:,:], min_ens[ens,size*r:size*(r+1),:,:],lat[size*r:size*(r+1)], r, pure = False)
            for r in range(batches)
        ]
        start = time.time();
        print(batches, 'batches started for ensemble', ens)
        for future, result in as_completed(futures, with_results = True, raise_errors = True):
            s, f, r = result
            sn[r] = s
            fn[r] = f
            print('Batch', r, 'finished in', time.time() - start, 'seconds')
        print(batches, 'batches finished in', time.time() - start, 'seconds')
        spring_index.append(np.concatenate(sn))
        freeze_index.append(np.concatenate(fn))
    spring_index = np.array(spring_index) 
    freeze_index = np.array(freeze_index)
    print(time.time() - total_start, "seconds for full ensemble")
    return spring_index, freeze_index
