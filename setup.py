import setuptools
setuptools.setup(
    name='BlueMary',
    version='0.0.1dev',
    author='pspiagicw',
    author_email='pspiagicw@gmail.com',
    license='MIT License',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pspiagicw/bluemary',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'bluemary=bluemary.main:run',
            ],
        },
)
              
        
    
    
