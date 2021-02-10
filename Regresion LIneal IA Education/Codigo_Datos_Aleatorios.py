p3 = plt.figure(figsize=(15,10)).gca(projection='3d')
x1, x2 = np.meshgrid(range(100), range(100))

z_modelo = modelo.coef_[0][0]*x1 + modelo.coef_[0][1]*x2

z_real = coeficientes_reales[0]*x1 + coeficientes_reales[1]*x2

	p3.plot_surface(x1, x2, z_modelo, alpha=0.3, color='green')
	p3.plot_surface(x1, x2, z_real, alpha=0.3, color='yellow')

		p3.scatter(X[:,0], X[:,1], Y)
		p3.set_title(u'Regresión lineal usando dos variables \
              (X1,X2) para predecir Y')
	p3.set_xlabel('Eje X1')
	p3.set_ylabel('Eje X2')
	p3.set_zlabel('Eje Y')
	p3.view_init(10, )
plt.show()
