import FWCore.ParameterSet.Config as cms

from Configuration.Generator.HerwigppDefaults_cfi import *
from Configuration.Generator.HerwigppUE_EE_5C_cfi import *


generator = cms.EDFilter("ThePEGHadronizerFilter",
	herwigDefaultsBlock,
	herwigppUESettingsBlock,

	configFiles = cms.vstring(),
	parameterSets = cms.vstring(
		'cmsDefaults',
		'EE5C',
		'lheDefaults',
		'cm13TeV',
	),

        crossSection = cms.untracked.double(-1.),
        filterEfficiency = cms.untracked.double(1.0),
)
ProductionFilterSequence = cms.Sequence(generator)
