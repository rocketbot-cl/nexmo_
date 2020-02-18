# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import os
import sys
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'nexmo_' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
import nexmo
from pprint import pprint
global client


"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "call_":

    app_id = GetParams('app_id')
    private_key = GetParams('private_key')
    number_ = GetParams('number_')
    message_ = GetParams('message_')
    language_ = GetParams('language_')

    if language_ == "spanish_":
        voice = "Enrique"
    if language_ == "english_":
        voice = "Joey"

    try:

        client = nexmo.Client(
            application_id=app_id,
            private_key=private_key,
        )

        ncco = [
            {
                'action': 'talk',
                'voiceName': voice,
                'text': message_
            }
        ]

        response = client.create_call({
            'to': [{
                'type': 'phone',
                'number': number_
            }],
            'from': {
                'type': 'phone',
                'number': '56999999999'
            },
            'ncco': ncco
        })

        pprint(response)

    except Exception as e:
        PrintException()
        raise e

if module == "numberInsight":

    key_ = GetParams('key_')
    secret_ = GetParams('secret_')
    number_ = GetParams('number_')
    var_ = GetParams('var_')
    print(key_,secret_,number_)

    client = nexmo.Client(key=key_, secret=secret_)
    print(client)

    insight_json = client.get_advanced_number_insight(number=number_)
    pprint(insight_json)

    SetVar(var_,insight_json)


