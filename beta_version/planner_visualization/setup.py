from setuptools import setup

package_name = 'planner_visualization'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sperling',
    maintainer_email='max-leon.sperling@man.eu',
    description='coupling_autocoup',
    license='MAN TRUCK AND BUS SE',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'planner_visualization = planner_visualization.node:main'
        ],
    },
)
