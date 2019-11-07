#################################################################################################
# To run execute do
# cmsRun tmtt_tf_analysis_cfg.py Events=50 inputMC=Samples/Muons/PU0.txt histFile=outputHistFile.root
# where the arguments take default values if you don't specify them. You can change defaults below.
#################################################################################################

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("L1TVertexFinder")

process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2023D17_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('L1Trigger.TrackFindingTracklet.L1TrackletTracks_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS3', '')
process.load("FWCore.MessageLogger.MessageLogger_cfi")


options = VarParsing.VarParsing ('analysis')
options.register('analysis',True,VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.bool,"Run vertex finding analysis code")
options.register('histFile','Hist.root',VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string,"Name of output histogram file")
#options.register('l1Tracks','TMTrackProducer:TML1TracksKF4ParamsComb', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, 'L1 track collection to use')
#options.register('l1Tracks','TMTrackProducer:TML1TracksSimpleLR', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, 'L1 track collection to use')
options.register('l1Tracks','TTTracksFromTracklet:Level1TTTracks', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, 'L1 track collection to use')
options.register('timevalues','ttTrackTimeValueMapProducer30ps:TTTracksFromTrackletL1ConfigurableFlatResolutionModel', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, 'time collection to use')
options.parseArguments()


#--- input and output
##inputFiles = ["root://cms-xrd-global.cern.ch///store/mc/PhaseIIFall17D/ZMM_14TeV_TuneCUETP8M1_Pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/60000/24D16EB5-60AF-E811-9584-0CC47AFC3C76.root"]
#inputFiles = ["root://cms-xrd-global.cern.ch///store/relval/CMSSW_9_3_7/RelValZMM_14/GEN-SIM-DIGI-RAW/PU25ns_93X_upgrade2023_realistic_v5_2023D17PU200-v1/10000/00556BB5-1931-E811-8164-4C79BA180C71.root"]
##for filePath in options.inputFiles:
##    if filePath.endswith(".root"):
##        inputFiles.append(filePath)
##    else:
##        inputFiles += FileUtils.loadListFromFile(filePath)


if options.l1Tracks.count(':') != 1:
    raise RuntimeError("Value for 'l1Tracks' command-line argument (= '{}') should contain one colon".format(options.l1Tracks))

l1TracksTag = cms.InputTag(options.l1Tracks.split(':')[0], options.l1Tracks.split(':')[1])
print "  INPUT TRACK COLLECTION = {0}  {1}".format(*options.l1Tracks.split(':')) 

if options.timevalues.count(':') != 1:
    raise RuntimeError("Value for 'timevalues' command-line argument (= '{}') should contain one colon".format(options.timevalues))
    
timevaluesTag = cms.InputTag(options.timevalues.split(':')[0], options.timevalues.split(':')[1])
print "  INPUT Time COLLECTION = {0}  {1}".format(*options.timevalues.split(':'))

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )

#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
if options.analysis:
    process.TFileService = cms.Service("TFileService", fileName = cms.string(options.histFile))

process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring(
                                '/store/mc/PhaseIIFall17D/ZMM_14TeV_TuneCUETP8M1_Pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/60000/AA50ED70-3FAF-E811-AF2B-0242AC130002.root',
                                '/store/mc/PhaseIIFall17D/ZMM_14TeV_TuneCUETP8M1_Pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/60000/AA1CBD5C-A4AE-E811-AC66-001E67DFF4F6.root',
                                '/store/mc/PhaseIIFall17D/ZMM_14TeV_TuneCUETP8M1_Pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/60000/AA162E8D-35AF-E811-961C-0242AC130002.root',
                                '/store/mc/PhaseIIFall17D/ZMM_14TeV_TuneCUETP8M1_Pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/60000/A6EB0478-3EAF-E811-98A3-0242AC130002.root',
                                '/store/mc/PhaseIIFall17D/ZMM_14TeV_TuneCUETP8M1_Pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/60000/A60F69E1-65AF-E811-9627-246E96D10990.root',
                                '/store/mc/PhaseIIFall17D/ZMM_14TeV_TuneCUETP8M1_Pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/60000/A46E315B-AEAE-E811-B9C2-44A842CFCA00.root',
                                '/store/mc/PhaseIIFall17D/ZMM_14TeV_TuneCUETP8M1_Pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/60000/A2F1D50C-40AF-E811-9FD8-0242AC130002.root',
                                '/store/mc/PhaseIIFall17D/ZMM_14TeV_TuneCUETP8M1_Pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/60000/A2DA0DBB-A3AE-E811-A87F-44A842CFD674.root',
                                '/store/mc/PhaseIIFall17D/ZMM_14TeV_TuneCUETP8M1_Pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/60000/A2C7CEC5-85AF-E811-917F-001E0BED0560.root',
                                '/store/mc/PhaseIIFall17D/ZMM_14TeV_TuneCUETP8M1_Pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/60000/A28C4275-66AF-E811-8BA3-246E96D14B94.root'
                                ),
#process.source = cms.Source ("PoolSource",
#                               fileNames = cms.untracked.vstring(inputFiles),
#                               secondaryFileNames = cms.untracked.vstring(),
                               # skipEvents = cms.untracked.uint32(500)
                              inputCommands=cms.untracked.vstring(
                                'keep *',
                                'drop l1tEMTFHit2016Extras_simEmtfDigis_CSC_HLT',
                                'drop l1tEMTFHit2016Extras_simEmtfDigis_RPC_HLT',
                                'drop l1tEMTFHit2016s_simEmtfDigis__HLT',
                                'drop l1tEMTFTrack2016Extras_simEmtfDigis__HLT',
                                'drop l1tEMTFTrack2016s_simEmtfDigis__HLT'
                              )
                            )

# process.out = cms.OutputModule("PoolOutputModule",
#     fileName = cms.untracked.string(options.outputFile),
#     outputCommands = cms.untracked.vstring(
#     	"keep *",
#     	"keep *_producer_*_*",
#     	"keep *_VertexProducer_*_*"
#     	)
# )


from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '100X_upgrade2023_realistic_v1', '')

process.Timing = cms.Service("Timing", summaryOnly = cms.untracked.bool(True))

#process.L1TrackTrigger_step = cms.Path(process.L1TrackletTracksWithAssociators)

#track times
process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)

#track times
process.load("SimTracker.TrackTriggerAssociation.ttTrackTimeValueMapProducer_cfi")
process.ttTrackTimeValueMapProducer30ps                     = process.ttTrackTimeValueMapProducer.clone()
process.ttTrackTimeValueMapProducer30ps.tkTriggerTrackTruth = cms.InputTag("TTTrackAssociatorFromPixelDigis", "Level1TTTracks")
process.ttTrackTimeValueMapProducer30ps.tkTriggerTrackSrc   = cms.InputTag("TTTracksFromTracklet", "Level1TTTracks")
process.ttTrackTimeValueMapProducer30ps.resolutionModels    = cms.VPSet(cms.PSet( modelName = cms.string('L1ConfigurableFlatResolutionModel'),
                                                                                  resolutionInNs = cms.double(0.030) ),
                                                                        cms.PSet( modelName = cms.string('L1PerfectResolutionModel') ) )

#--- Load config fragment that configures vertex producer
process.load('L1Trigger.VertexFinder.VertexProducer_cff')
process.VertexProducer.l1TracksInputTag = l1TracksTag
process.VertexProducer.timingValuesNominal = timevaluesTag
#--- Load config fragment that configures vertex analyzer
process.load('L1Trigger.VertexFinder.VertexAnalyzer_cff')
process.L1TVertexAnalyzer.l1TracksInputTag = l1TracksTag

if (options.analysis):
    print "p1.1"
    process.p = cms.Path(process.L1TrackletTracksWithAssociators + process.ttTrackTimeValueMapProducer30ps + process.VertexProducer + process.L1TVertexAnalyzer)
else:
    process.p = cms.Path(process.L1TrackletTracksWithAssociators + process.ttTrackTimeValueMapProducer30ps + process.VertexProducer)
    print "p1.2"
# process.e = cms.EndPath(process.out)
