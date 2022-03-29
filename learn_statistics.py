from matplotlib import pyplot as plt
import statistics as stats

# Example of using the statistics built-in module
# And my own statistics 

def my_mean(lst):
    return sum(lst)/len(lst)

def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


normalD = [0.12,1.09,-0.17,-0.21,0.27,-1.07,-2.45,-0.14,0.12,0.58,-1.82,2.28,-0.58,-0.45,-1.54,0.54,-0.81,1.77,1.5,-1.04,0.02,-0.08,0.7,-0.97,0.74,0.1,1.5,0.46,-0.15,1.33,-2.46,0.52,-0.25,0.28,-0.52,0.62,0.82,-0.12,1.22,-0.91,-1.34,-0.78,-0.51,0.03,-0.9,0.16,2.26,-0.02,0.92,-0.82,-1.17,2.05,1.79,1.78,-0.24,-1.25,0.07,-0.5,-0.14,0.17,-0.61,-0.24,0.73,0.52,-2.08,1.3,-0.11,-0.85,-0.79,0.37,-1.11,-0.57,-1.36,0.21,1.22,-0.75,-1.23,-0.38,-0.17,-1.34,-0.8,0.14,-1.29,0.95,-0.66,1.44,0.75,0.38,-0.78,-0.44,0.26,-1.86,-1.04,0.11,-1.04,0.15,-0.21,-0.7,-0.06,-0.36]
normalD100 = [el*100 for el in normalD]

plt.plot(normalD100) 
print(my_mean(normalD100))
print( stats.mean(normalD100) )
print( stats.median(normalD100) )
print( max(normalD100) - min(normalD100) )

print( quantile(normalD100, 0.75) )     
print( quantile(normalD100, 0.25) )
print( interquartile_range(normalD100) )

print( stats.pvariance(normalD100) )
print( stats.pstdev(normalD100) )


