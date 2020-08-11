tn_path = #local path for maximum temperature data
tx_path = #local path for minimum temperature data

spring = []
freeze = []
counter = 0
for i in range(0,100,10):
    mint, maxt, lat = open_nc(tn_path, tx_path, i, i+10)
    spring_year, freeze_year = run_batches(maxt, mint, lat, 5, spring_index)
    spring.append(spring_year)
    freeze.append(freeze_year)
    counter = counter + 10
    print('\n', '\n', '\n', counter, 'ensemble members finished',  '\n', '\n', '\n')
    
spring_ens = np.concatenate(spring)
freeze_ens = np.concatenate(freeze)