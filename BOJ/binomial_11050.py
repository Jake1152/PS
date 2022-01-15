#n! / k! * (n - k)!
n, k = map(int, input().split())
n_mul = 1
k_mul = 1
n_k_mul = 1
for n_fac in range(n, 0, -1):
	n_mul *= n_fac

for k_fac in range(k, 0, -1):
	k_mul *= k_fac

for n_k_fac in range(n - k, 0, -1):
	n_k_mul *= n_k_fac

print(n_mul // (k_mul * n_k_mul))
