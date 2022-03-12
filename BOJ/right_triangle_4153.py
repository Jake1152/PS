while (True):
	base, perpendicular, hypotenuse = sorted(map(int, input().split()))
	if base==0 and perpendicular==0 and hypotenuse==0:
		break
	elif base**2+perpendicular**2 == hypotenuse**2:
		print("right")
	else:
		print("wrong")
