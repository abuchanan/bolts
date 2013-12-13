from distutils.core import setup


setup(
    name='bolts',
    description="Nuts and bolts. Small recipes I've found occasionally useful.",
    version='1.2.0',
    author='Alex Buchanan',
    author_email='buchanae@gmail.com',
    license='MIT',
    py_modules=[
        'bolts.initializer',
        'bolts.keyedset',
        'bolts.sampler',
        'bolts.tree',
    ],
)
