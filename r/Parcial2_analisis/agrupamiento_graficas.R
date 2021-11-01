library(dplyr)
attach(datos)
grupo_datos = aggregate(calificacion ~ restaurante.nombre, data=datos,FUN = mean)
library(ggplot2)
ggplot(grupo_datos,aes(x=restaurante.nombre,y=calificacion))+geom_bar(stat="identity")+ggtitle("Calificaciones promedio")+ylab("Calificacion")+xlab("Restaurante")

attach(grupo_datos2)
grupo_datos3 = aggregate(x ~ restaurante.nombre, data = new_df, FUN = sum)

ggplot(grupo_datos3,aes(x=restaurante.nombre,y=x))+geom_bar(stat="identity")+ggtitle("Visitas de los restaurantes")+ylab("Visitas")+xlab("Restaurante")

