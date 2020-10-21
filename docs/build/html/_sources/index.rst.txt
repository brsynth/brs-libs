inchikeyMIRIAM's Documentation
==============================

Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Introduction
############

.. _rpBase: https://github.com/Galaxy-SynBioCAD/rpBase
.. _rpCache: https://github.com/Galaxy-SynBioCAD/rpCache

Welcome to the documentation of inchikeyMIRIAM. This project parses SBML files, scans the species cross-references and tries to find the appropriate inchikeys. If found, its added to the same MIRIAM annotation.

Usage
#####

First build the rpBase_ and rpCache_ dockers before building the local one:

.. code-block:: bash

   docker build -t brsynth/inchikeymiriam-standalone:v2 .

The docker can be called locally using the following command:

.. code-block:: bash

   python run.py -input_sbml input_sbml.xml -output_sbml output_sbml.xml

API
###

.. toctree::
   :maxdepth: 1
   :caption: Contents:

.. currentmodule:: inchikeyMIRIAM

.. autoclass:: inchikeyMIRIAM
    :show-inheritance:
    :members:
    :inherited-members:

.. currentmodule:: run

.. autoclass:: main
    :show-inheritance:
    :members:
    :inherited-members:
