#!/bin/bash

cmsrel CMSSW_10_1_7
cd CMSSW_10_1_7/src
cmsenv
git cms-init
git remote add cms-l1t-offline git@github.com:cms-l1t-offline/cmssw.git
git fetch cms-l1t-offline phase2-l1t-integration-CMSSW_10_1_7
git cms-merge-topic -u cms-l1t-offline:l1t-phase2-v2.22.0
git cms-merge-topic -u lgray:topic_l1tracktrigger_times_1017
git cms-merge-topic -u isobelojalvo:l1caloclusters

git cms-addpkg L1Trigger/L1TCommon

scram b -j 8

