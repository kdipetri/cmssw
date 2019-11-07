from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'p15_Vertex_Zmm_PU200_Dec18v1'
config.General.workArea = 'crab_prod'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'vertexFinder_cfg.py'

config.Data.inputDataset = '/ZMM_14TeV_TuneCUETP8M1_Pythia8/PhaseIIFall17D-L1TPU200_93X_upgrade2023_realistic_v5-v1/GEN-SIM-DIGI-RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
config.Data.outLFNDirBase = '/store/user/nlu'
config.Data.publication = True
config.Data.outputDatasetTag = 'p15_Vertex_Zmm_PU200_Dec18v1'
config.Site.blacklist = ['T2_IT_Legnaro']
config.Site.storageSite = 'T2_CH_CERN'
