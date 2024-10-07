from setuptools import setup, Extension
import pybind11

#python3.12 setup.py build_ext --inplace
# Definir el módulo de extensión
ext_modules = [
    Extension(
        'pi_montecarlo',                        # Nombre del módulo
        ['pi_montecarlo.cpp'],               # Archivo fuente C++
        include_dirs=[pybind11.get_include()],  # Incluir encabezados de Pybind11
        language='c++'
    )
]

# Configuración del paquete
setup(
    name='pi_montecarlo',
    version='0.1',
    ext_modules=ext_modules,
    install_requires=['pybind11'],
    zip_safe=False,
)
