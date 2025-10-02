import ee

# Inicializar la librería
ee.Initialize()

# Ejemplo: cargar un dataset
image = ee.Image('NASA/NASADEM_HGT/001')
print(image.getInfo())
