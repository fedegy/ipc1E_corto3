from flask import Flask,request,jsonify
from misDatos import misDatos
from Inversor import Inversor


datosget=[]
#Se listan los datos
datosget.append(misDatos(201901073,'Federico'))



app=Flask(__name__)
#Se asigna a dicha ruta el metodo GET
@app.route("/misDatos",methods=['GET'])

#Funcion misDatos
def misDatos():
    if request.method=='GET':

        response={}
        #Se recorren los datos de la lista datosget
        for datos in datosget:
                #se muestran los datos en formato json mediante la funcion dump
                #creada en la clase misDatos
                response["carne"]=datos.carne
                response["nombre"]=datos.nombre
                #retorna todos los valores 
                return response

datoscadenaentrada=[]
datoscadenaentrada.append(Inversor("olpmeje ed anedac anu su atse"))

@app.route("/inversor",methods=['POST'])
def Inversor():
    if request.method=='POST':

        response={}
        cadenaEntrada=request.form.get('cadena_entrada')

        for cadena in datoscadenaentrada:
                response["resultado"]=cadena.resultado
                return response


if __name__ == "__main__":
    app.run(threaded=True,port=5000,debug=True)
