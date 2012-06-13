from distutils.core import setup

setup(
    name='bottu-faq',
    version='0.1',
    py_modules=['bottu_faq'],
    url='',
    license='BSD',
    author='Jonas Obrist',
    author_email='ojiidotch@gmail.com',
    description='',
    entry_points = {
        'bottu.plugins': [
            'faq = bottu_faq:register'
        ],
    }
)
