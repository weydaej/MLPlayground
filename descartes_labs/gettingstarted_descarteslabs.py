import descarteslabs as dl
import matplotlib.pyplot as plt
import my_secrets

from descarteslabs.catalog import Product, Band

DESCARTESLABS_CLIENT_ID = my_secrets.getClientID()
DESCARTESLABS_CLIENT_SECRET = my_secrets.getClientSecret()

matches = dl.places.find('new-mexico_taos')
print(matches)

aoi = matches[0]
shape = dl.places.shape(aoi['slug'], geom='low')

product = Product.get('landsat:LC08:PRE:TOAR')
bands = product.bands()
print([band.name for band in bands])

scenes, ctx = dl.scenes.search(shape['geometry'],
                               products = "landsat:LC08:01:RT:TOAR",
                               start_datetime="2017-11-01",
                               end_datetime="2018-07-01",
                            #    cloud_fraction=0.7,
                               limit=500)

print(ctx)
highres_context = ctx.assign(resolution=120)
print(ctx.geometry)
print(scenes)


scene = scenes[16]
arr = scene.ndarray("red green blue", highres_context)
dl.scenes.display(arr, title="Partial Coverage")