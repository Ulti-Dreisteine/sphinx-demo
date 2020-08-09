.. sphinx-demo documentation master file, created by
   sphinx-quickstart on Tue Aug  4 18:07:13 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===================
PyCaret练练手
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

1. 建立任务
:::::::::::

   该步骤是所有PyCaret建模必经初始化步骤.

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

   **【注意】**
      1. target, numerical_features和categorical_features相互独立;
      #. 在setup过程中可以对特征进行处理, 比如上述代码中对特征进行了共线性筛选并忽略了
         低方差特征;


2. 各模型对比
:::::::::::::

   | 在这一步中将会把测试数据代入PyCaret所有已经集成好的分类模型中进行训练, 计算各自的AUC,
   | Recall, F1, Precision等指标, 保存在图表中.

   在PyCaret中各模型名称缩写如下:

   ========== ==========================
   ID         Name
   ========== ==========================
   lr         Logistic Regression
   knn        K Nearest Neighbour
   nb         Naive Bayes
   dt         Decision Tree Classifier
   svm        SVM - Linear Kernel
   rbfsvm     SVM - Radial Kernel
   gpc        Gaussian Process Classifier
   mlp        Multi Level Perceptron
   ridge      Ridge Classifier
   rf         Random Forest Classifier
   qda        Quadratic Discriminant Analysis
   ada        Ada Boost Classifier
   gbc        Gradient Boosting Classifier
   lda        Linear Discriminant Analysis
   et         Extra Trees Classifier
   xgboost    Extreme Gradient Boosting
   lightgbm   Light Gradient Boosting
   catboost   CatBoost Classifier
   ========== ==========================

   | 如果需要计算某些特定模型, 可将其加入whitelist中; 反之, 如果想避免某些模型计算, 则将其加入blacklist中,
   | 代码如下:

   ::

      model_store_final = compare_models(
          whitelist = ['lr', 'rf', 'ridge', 'xgboost'],
          sort = 'F1',
          verbose = True
      )

   评估所得结果如下:

   == ========================== ========= ====== ====== ====== ====== ====== ====== ========
   id Model                      Accuracy  AUC    Recall Prec.  F1     Kappa  MCC    TT (Sec)
   == ========================== ========= ====== ====== ====== ====== ====== ====== ========
   0  Extreme Gradient Boosting	 0.7754	   0.7253 0.2319 0.4844 0.3071 0.1909 0.2137 0.1909
   1  Ridge Classifier	         0.7898	   0.0000 0.1802 0.5438 0.2620 0.1755 0.2144 0.0099
   2  Logistic Regression        0.7802    0.7477 0.1780 0.5021 0.2559 0.1575 0.1914 0.0422
   3  Random Forest Classifier	 0.7834	   0.7108 0.1198 0.4425 0.1803 0.1101 0.1389 0.0301
   == ========================== ========= ====== ====== ====== ====== ====== ====== ========

3. 单模型计算
:::::::::::::

   首先建立单个模型:

   ::

      params = {'max_depth': 4, 'min_samples_leaf': 5, 'min_samples_split': 10}
      clf = create_model('rf', verbose = True, **params)

   模型默认采用10折检验, 计算结果保留小数点后4位. 得到的各指标如下:

   ==== ========= ====== ====== ====== ====== ======= =======
   fold Accuracy  AUC    Recall Prec.  F1     Kappa   MCC    
   ==== ========= ====== ====== ====== ====== ======= =======
   0	0.7937    0.6754 0.1538 0.5000 0.2353 0.1531  0.1889
   1	0.7778    0.7115 0.0000 0.0000 0.0000 -0.0304 -0.0648
   2	0.8413    0.7538 0.3077 0.8000 0.4444 0.3725  0.4307
   3	0.8095    0.8469 0.0769 1.0000 0.1429 0.1168  0.2491
   4	0.7778    0.6356 0.1429 0.5000 0.2222 0.1370  0.1740
   5	0.7619    0.7376 0.0714 0.3333 0.1176 0.0426  0.0598
   6	0.7619    0.6633 0.0000 0.0000 0.0000 -0.0305 -0.0679
   7	0.7460    0.6093 0.2143 0.3750 0.2727 0.1325  0.1402
   8	0.7581    0.6931 0.0769 0.2500 0.1176 0.0211  0.0260
   9	0.8065    0.7818 0.1538 0.6667 0.2500 0.1860  0.2531
   Mean	0.7834    0.7108 0.1198 0.4425 0.1803 0.1101  0.1389
   SD	0.0277    0.0678 0.0904 0.3067 0.1274 0.1139  0.1474
   ==== ========= ====== ====== ====== ====== ======= =======

   模型获得了平均指标和对应的标准差.

   接下来, 可以使用PyCaret中的模型调参进行优化, 使用的算法为Stratified Cross Validation.

   ::

      clf_tuned = tune_model(clf, optimize = 'F1', n_iter = 20, fold = 10, round = 4)

   得到的指标为:

   ==== ========= ====== ====== ====== ====== ======= =======
   fold Accuracy  AUC    Recall Prec.  F1     Kappa   MCC
   ==== ========= ====== ====== ====== ====== ======= =======
   0	0.7460    0.6577 0.1538	0.2857 0.2000 0.0649  0.0693
   1	0.8413    0.8038 0.3077	0.8000 0.4444 0.3725  0.4307
   2	0.8095    0.8085 0.1538	0.6667 0.2500 0.1871  0.2543
   3	0.7778    0.7177 0.1538	0.4000 0.2222 0.1215  0.1405
   4	0.8254    0.7529 0.4286	0.6667 0.5217 0.4211  0.4364
   5	0.7778    0.7762 0.1429	0.5000 0.2222 0.1370  0.1740
   6	0.8413    0.8061 0.4286	0.7500 0.5455 0.4578  0.4842
   7	0.7778    0.6370 0.2143	0.5000 0.3000 0.1923  0.2168
   8	0.7419    0.6319 0.1538	0.2857 0.2000 0.0624  0.0666
   9	0.8065    0.8116 0.1538	0.6667 0.2500 0.1860  0.2531
   Mean	0.7945    0.7403 0.2291	0.5521 0.3156 0.2203  0.2526
   SD	0.0341    0.0702 0.1103	0.1762 0.1284 0.1374  0.1440
   ==== ========= ====== ====== ====== ====== ======= =======

   可以看出, 优化后的模型在目标指标上得到了显著提升.

   **【注意】**
      | 1. PyCaret中经过tune_model优化后的模型参数可能不合理, 比如优化后的随机森林模型最大树深度max_depth可
      | 达20, 目前也没有发现可以提供给用户进行参数边界设置的接口, 可能相关功能还在迭代中;

4. 模型可视化评估
:::::::::::::::::

   | PyCaret中提供了plot_model, evaluate_model, interpret_model等函数, 方便进行模型效果评估, 解释和可视化.
   | 其中, 模型评估提供了Hyperparameters, AUC, Confusion Matrix, Threshold, PR Curve, Error, Class Report,
   | Feature Selection, Learning Curve, Manifold Learning等功能.

   ::

      evaluate_model(clf_tuned)
      interpret_model(clf_tuned, plot = 'correlation')
      interpret_model(clf_tuned, plot = 'reason', observation = 0)

   **【注意】**
      | 1. 模型解释interpret_model只能用于树模型, 且偶尔会因为对底层shap包的调用报错, 目前未找到解决办法;

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
