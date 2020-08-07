.. sphinx-demo documentation master file, created by
   sphinx-quickstart on Tue Aug  4 18:07:13 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===================
PyCaret教程文档
===================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


分类模型 classification
=======================

| PyCaret的分类模型集成了sklearn中主要的机器学习分类模型, 并能够实现:
| 1. 模型自动对比和筛选
| 2. 模型自动调参
| 3. 模型输出可视化

数据准备
--------

.. 注意此处多个member插入的用法.

.. automodule:: src.classification
   :members: load_test_data, process_data

建模
----

首先setup

   ::

      task = setup(
          data,
          target = 'VTE',
          numeric_features = numeric_cols,
          categorical_features = categoric_cols,
          verbose = False,
          remove_multicollinearity = True,
          multicollinearity_threshold = 0.6,
          ignore_low_variance = True,
      )

各模型对比

   ::

      model_store_final = compare_models(
          whitelist = ['lr', 'rf', 'ridge', 'xgboost'],
          sort = 'F1',
          verbose = True
      )

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
