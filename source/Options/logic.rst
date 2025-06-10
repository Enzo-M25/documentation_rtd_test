
Logic
+++++

Le lien du paragraphe doit amené ici = début du paraph suivant

.. _hwcodeOptions:

Exemple liste
=============

Ceci forme une liste :

* point 1
* pt 2
    * 2.1
* pt 3

ou

#. 1
#. 2
#. 3


Exemple image
=============

.. image:: /images/image.png

Exemple tableaux
----------------

Méthode 1 : tableau

.. table:: Titre

    ================ =============== ====== ===========
    Platform         Self-contained? Cost   Flexibility
    ================ =============== ====== ===========
    Row 1            No              30     Limitless
    Row 2            Yes             350    Medium
    ================ =============== ====== ===========


Méthode 2 : list-table

.. list-table:: Comparison
    :widths: 20 10 10 15
    :header-rows: 1

    * - Platform
      - Self-Contained?
      - Cost
      - Flexibility
    * - Raspberry Pi
      - No
      - $30
      - Limitless
    * - Lego Mindstorms
      - Yes
      - $350
      - Medium

Méthode 3 : csv-table

.. csv-table:: Comparison
    :header: Platform,Self-Contained?,Cost,Flexibility
    :widths: 15 10 30 30

    Raspberry Pi,No,$30,Limitless
    Lego Mindstorms,Yes,$350,Medium

Hyperlinks
----------

Hyperlink 1 : 

lien vers une page web en "brut" :

https://cydre.univ-rennes.fr/

ou autrement :

`Cydre <https://cydre.univ-rennes.fr/>`_

Hyperlink 2 :

lien vers un autre endroit du read the docs :

:doc:`../Guidelines/contents`

ou en ajoutant un texte

Voir la page :doc:`contenu des guidelines <../Guidelines/contents>`

Hyperlink 3 :

référence à un paragraphe spécifique :

Voir la section :ref:`Ref à un paraph <hwcodeOptions>` pour plus d'infos.
