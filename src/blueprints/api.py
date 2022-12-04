from flask import Blueprint, request, abort
from enemy_color import EnemyColor
from numpy import array
from PIL.ImageColor import getcolor

api = Blueprint("api", __name__, url_prefix="/api/v1/")

color = EnemyColor()

@api.get("/getEnemy")
def get_enemy():
    print(request.host_url)
    args = request.args
    canales:list = [args.get(i) for i in "rgb"]
    hex_color:str = args.get("color")

    if not all(canales) and not hex_color:
        return abort(400)
    
    r, g, b = getcolor(f'#{hex_color}', "RGB") if hex_color else canales
    prediccion = color.predict(array([r, g, b]))

    return {k:v for k,v in zip('rgb', prediccion)}