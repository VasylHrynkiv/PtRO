from timeit import default_timer as timer
from multiprocessing import Pool

def f(x):
    return x*x

start = timer()

if __name__ == '__main__':
    with Pool(processes=2) as pool:         
        print(pool.apply_async(f, (100,)).get(timeout=1))   

        print(pool.map(f, range(25)))       

        it = pool.imap(f, range(3))
        print(next(it))                     
        print(next(it))                     
        print(it.next(timeout=1))

        print('Took: %.2f seconds.' % (timer() - start))

#Василь Васильович Гриньків, група КІПЗс-2017
