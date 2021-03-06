from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='feda.torneos',
      version=version,
      description="Content-types for tournament handling in Spanish Chess Federation",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Mikel Larreategi',
      author_email='larreategi@eibar.org',
      url='https://github.com/erral/feda.torneos',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['feda'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [relations]',
          'plone.namedfile [blobs]',
          'plone.app.workflowmanager'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],

      )
