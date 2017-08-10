#coding:utf-8
import sys
import os
import xgboost as xgb



def train():
    dtrain = xgb.DMatrix("weight_training.data")
    #gbtree_param = {'booster':'gbtree', 'max_depth':'3', 'num_class' : 4, 'eta':'0.1', 'objective':'multi:softmax', 'eval_metric':  'merror'}

    gbtree_param = {'booster':'gbtree', 'max_depth':'3', 'eta':'0.1', 'objective':'reg:linear'}
    num_round = 10
    gbtree_bst = xgb.train(gbtree_param, dtrain, num_round, evals=[(dtrain, 'train')])
    dtest = xgb.DMatrix("weight_testing.data")
    pred = gbtree_bst.predict(dtest)
    print pred
    
    return


if __name__ == "__main__":
    train()
