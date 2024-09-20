print("Act 9 Clase Humano")
print("Melany Chairez Mat:22308051281058")
#zona de clases
class humano1058:
    #zona de atributos
    edad=0
    estatura=0
    fecha_nac=""
    genero=""
    ojos=""
    cab=""
    peso=""
#funciones dentro de la clase
    def dormir1058(self,n):
        print(f"{n} esta durmiendo")
    def comer1058(self,n):
        print(f"{n} ya se alimento hoy")    
    def estudiar1058(self,n):
        print(f"{n} va a estudiar para su examen")   
    def leer1058(self,n):
        print(f"{n} esta leyendo")  
    def jugar1058(self,n):
        print(f"{n} esta jugano Ark")   
#creacion de objetos
mel=humano1058()
mel.edad=16
mel.estatura=1.63
mel.fecha_nac="22/10/2007"
mel.genero="Femenino"
mel.peso="73 kg"
adri=humano1058()
adri.edad=17
adri.estatura=1.75
adri.fecha_nac="18/12/2007"
adri.genero="Masculino"
adri.ojos="Cafe"
adri.cab="Rizado"
#usando objetos
print("\n Resultados para Melany")
print(f"Edad: {mel.edad}") 
print(f"Estatura: {mel.estatura}")
print(f"Fecha de nacimiento: {mel.fecha_nac}")
print(f"Genero: {mel.genero}")
print(f"Peso: {mel.peso}")
mel.dormir1058("Melany" )
mel.comer1058("Melany" )
mel.estudiar1058("Melany" )
mel.leer1058("Melany" )
print("\n Resultados para Adriel")
print(f"Edad: {adri.edad}")
print(f"Estatura: {adri.estatura}")
print(f"Fecha de nacimiento: {adri.fecha_nac}")
print(f"Genero: {adri.genero}")
print(f"Color de ojos: {adri.ojos}")
adri.dormir1058("Adriel" )
adri.comer1058("Adriel" )
adri.estudiar1058("Adriel" )
adri.leer1058("Adriel" )
adri.jugar1058("Adriel" )