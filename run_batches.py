import numpy as np
import dask
import time

def run_batches(max_ens, min_ens, lat, factor,model):
    total_start = time.clock()
    num_ens = min_ens.shape[0]
    num_lats = min_ens.shape[1]
    batch_size = int(num_lats/factor)
    spring_index = []
    freeze_index = []
    counter = 0
    for ens in range(0,num_ens):
        from dask.diagnostics import ProgressBar
        ProgressBar().register()
        part1 = dask.delayed(model)(max_ens[ens,:batch_size,:,:], min_ens[ens,:batch_size,:,:],lat[:batch_size])
        start_time = time.clock()
        counter = counter + 1
        s1,f1 = part1.compute(scheduler='processes')
        print(time.clock() - start_time, "seconds for model run + counter ", counter, "/ 500")
        part2 = dask.delayed(model)(max_ens[ens,batch_size:batch_size*2,:,:], min_ens[ens,batch_size:batch_size*2,:,:],lat[batch_size:batch_size*2])
        start_time = time.clock()
        counter = counter + 1
        s2,f2 = part2.compute(scheduler='processes')
        print(time.clock() - start_time, "seconds for model run + counter ", counter, "/ 500")
        part3 = dask.delayed(model)(max_ens[ens,batch_size*2:batch_size*3,:,:], min_ens[ens,batch_size*2:batch_size*3,:,:],lat[batch_size*2:batch_size*3])
        start_time = time.clock()
        counter = counter + 1
        s3,f3 = part3.compute(scheduler='processes')
        print(time.clock() - start_time, "seconds for model run + counter ", counter, "/ 500")
        part4 = dask.delayed(model)(max_ens[ens,batch_size*3:batch_size*4,:,:], min_ens[ens,batch_size*3:batch_size*4,:,:],lat[batch_size*3:batch_size*4])
        start_time = time.clock()
        counter = counter + 1
        s4,f4 = part4.compute(scheduler='processes')
        print(time.clock() - start_time, "seconds for model run + counter ", counter, "/ 500")
        part5 = dask.delayed(model)(max_ens[ens,batch_size*4:,:,:], min_ens[ens,batch_size*4:,:,:],lat[batch_size*4:])
        start_time = time.clock()
        counter = counter + 1
        s5,f5 = part5.compute(scheduler='processes')
        print(time.clock() - start_time, "seconds for model sub-run + counter ", counter, "/ 500")
        spring = np.concatenate((s1,s2,s3,s4,s5)) 
        freeze = np.concatenate((f1,f2,f3,f4,f5))
        spring_index.append(spring)
        freeze_index.append(freeze)
    spring_index = np.array(spring_index) 
    freeze_index = np.array(freeze_index)
    print(time.clock() - total_start, "seconds for full ensemble")
    return spring_index, freeze_index

# the factor that is used should be able to devide the number of latitudes used
# when using the full ensemble splitting the work for each ensemble member in 5
# workloads gave the fastest results for me
    
spring_year, freeze_year = run_batches(maxt, mint, lat, 5, spring_index)

# this range gives meaningfull reseults:
spring_year[0,160:180,350:370]
freeze_year[0,160:180,350:370]