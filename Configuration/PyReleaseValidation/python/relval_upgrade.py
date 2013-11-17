
# import the definition of the steps and input files:
from  Configuration.PyReleaseValidation.relval_steps import *

# here only define the workflows as a combination of the steps defined above:
workflows = {}

# each workflow defines a name and a list of steps to be done. 
# if no explicit name/label given for the workflow (first arg),
# the name of step1 will be used


#2017
#part gun
workflows[3300]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3301]  = [ 'SingleElectronPt10' ,  ['SingleElectronPt10_UPG2017','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3302]  = [ 'SingleElectronPt1000' ,  ['SingleElectronPt1000_UPG2017','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3303]  = [ 'SingleElectronPt35' ,  ['SingleElectronPt35_UPG2017','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3304]  = [ 'SingleGammaPt10' ,  ['SingleGammaPt10_UPG2017','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3305]  = [ 'SingleGammaPt35' ,  ['SingleGammaPt35_UPG2017','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3306]  = [ 'SingleMuPt1' ,  ['SingleMuPt1_UPG2017','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3307]  = [ 'SingleMuPt10' ,  ['SingleMuPt10_UPG2017','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3308]  = [ 'SingleMuPt100' ,  ['SingleMuPt100_UPG2017','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3309]  = [ 'SingleMuPt1000' ,  ['SingleMuPt1000_UPG2017','DIGIUP17','RECOUP17','HARVESTUP17']]

#std wf @8TeV
workflows[3310]  = [ 'TTbarLepton_8TeV' ,  ['TTbarLepton_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3311]  = [ 'Wjet_Pt_80_120_8TeV' ,  ['Wjet_Pt_80_120_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3312]  = [ 'Wjet_Pt_3000_3500_8TeV' ,  ['Wjet_Pt_3000_3500_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3313]  = [ 'LM1_sfts_8TeV' ,  ['LM1_sfts_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]

workflows[3314]  = [ 'QCD_Pt_3000_3500_8TeV' ,  ['QCD_Pt_3000_3500_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3315]  = [ 'QCD_Pt_600_800_8TeV' ,  ['QCD_Pt_600_800_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3316]  = [ 'QCD_Pt_80_120_8TeV' ,  ['QCD_Pt_80_120_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]

workflows[3317]  = [ 'Higgs200ChargedTaus_8TeV' ,  ['Higgs200ChargedTaus_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3318]  = [ 'JpsiMM_8TeV' ,  ['JpsiMM_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3319]  = [ 'TTbar_8TeV' ,  ['TTbar_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3320]  = [ 'WE_8TeV' ,  ['WE_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3321]  = [ 'ZEE_8TeV' ,  ['ZEE_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3322]  = [ 'ZTT_8TeV' ,  ['ZTT_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3323]  = [ 'H130GGgluonfusion_8TeV' ,  ['H130GGgluonfusion_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3324]  = [ 'PhotonJets_Pt_10_8TeV' ,  ['PhotonJets_Pt_10_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3325]  = [ 'QQH1352T_Tauola_8TeV' ,  ['QQH1352T_Tauola_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]

workflows[3326]  = [ 'MinBias_TuneZ2star_8TeV' ,  ['MinBias_TuneZ2star_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3327]  = [ 'WM_8TeV' ,  ['WM_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3328]  = [ 'ZMM_8TeV' ,  ['ZMM_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]

workflows[3329]  = [ 'ADDMonoJet_d3MD3_8TeV' ,  ['ADDMonoJet_d3MD3_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3330]  = [ 'ZpMM_8TeV' ,  ['ZpMM_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3331]  = [ 'WpM_8TeV' ,  ['WpM_UPG2017_8','DIGIUP17','RECOUP17','HARVESTUP17']]



#std wf @14TeV
#workflows[3332]  = [ 'TTbarLepton_14TeV' ,  ['TTbarLepton_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']] #no gen fragment
workflows[3333]  = [ 'Wjet_Pt_80_120_14TeV' ,  ['Wjet_Pt_80_120_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3334]  = [ 'Wjet_Pt_3000_3500_14TeV' ,  ['Wjet_Pt_3000_3500_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3335]  = [ 'LM1_sfts_14TeV' ,  ['LM1_sfts_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]

workflows[3336]  = [ 'QCD_Pt_3000_3500_14TeV' ,  ['QCD_Pt_3000_3500_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
#workflows[3337]  = [ 'QCD_Pt_600_800_14TeV' ,  ['QCD_Pt_600_800_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']] #no gen fragment
workflows[3338]  = [ 'QCD_Pt_80_120_14TeV' ,  ['QCD_Pt_80_120_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]

workflows[3339]  = [ 'Higgs200ChargedTaus_14TeV' ,  ['Higgs200ChargedTaus_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3340]  = [ 'JpsiMM_14TeV' ,  ['JpsiMM_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3341]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3342]  = [ 'WE_14TeV' ,  ['WE_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3343]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3344]  = [ 'ZTT_14TeV' ,  ['ZTT_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3345]  = [ 'H130GGgluonfusion_14TeV' ,  ['H130GGgluonfusion_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3346]  = [ 'PhotonJets_Pt_10_14TeV' ,  ['PhotonJets_Pt_10_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3347]  = [ 'QQH1352T_Tauola_14TeV' ,  ['QQH1352T_Tauola_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]

workflows[3348]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3349]  = [ 'WM_14TeV' ,  ['WM_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]
workflows[3350]  = [ 'ZMM_14TeV' ,  ['ZMM_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]

#workflows[3351]  = [ 'ADDMonoJet_d3MD3_14TeV' ,  ['ADDMonoJet_d3MD3_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]#no gen fragment
#workflows[3352]  = [ 'ZpMM_14TeV' ,  ['ZpMM_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]#no gen fragment
#workflows[3353]  = [ 'WpM_14TeV' ,  ['WpM_UPG2017_14','DIGIUP17','RECOUP17','HARVESTUP17']]#no gen fragment


#2019
#part gun
workflows[3400]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3401]  = [ 'SingleElectronPt10' ,  ['SingleElectronPt10_UPG2019','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3402]  = [ 'SingleElectronPt1000' ,  ['SingleElectronPt1000_UPG2019','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3403]  = [ 'SingleElectronPt35' ,  ['SingleElectronPt35_UPG2019','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3404]  = [ 'SingleGammaPt10' ,  ['SingleGammaPt10_UPG2019','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3405]  = [ 'SingleGammaPt35' ,  ['SingleGammaPt35_UPG2019','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3406]  = [ 'SingleMuPt1' ,  ['SingleMuPt1_UPG2019','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3407]  = [ 'SingleMuPt10' ,  ['SingleMuPt10_UPG2019','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3408]  = [ 'SingleMuPt100' ,  ['SingleMuPt100_UPG2019','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3409]  = [ 'SingleMuPt1000' ,  ['SingleMuPt1000_UPG2019','DIGIUP19','RECOUP19','HARVESTUP19']]


#std wf @8TeV
workflows[3410]  = [ 'TTbarLepton_8TeV' ,  ['TTbarLepton_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3411]  = [ 'Wjet_Pt_80_120_8TeV' ,  ['Wjet_Pt_80_120_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3412]  = [ 'Wjet_Pt_3000_3500_8TeV' ,  ['Wjet_Pt_3000_3500_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3413]  = [ 'LM1_sfts_8TeV' ,  ['LM1_sfts_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]

workflows[3414]  = [ 'QCD_Pt_3000_3500_8TeV' ,  ['QCD_Pt_3000_3500_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3415]  = [ 'QCD_Pt_600_800_8TeV' ,  ['QCD_Pt_600_800_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3416]  = [ 'QCD_Pt_80_120_8TeV' ,  ['QCD_Pt_80_120_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]

workflows[3417]  = [ 'Higgs200ChargedTaus_8TeV' ,  ['Higgs200ChargedTaus_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3418]  = [ 'JpsiMM_8TeV' ,  ['JpsiMM_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3419]  = [ 'TTbar_8TeV' ,  ['TTbar_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3420]  = [ 'WE_8TeV' ,  ['WE_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3421]  = [ 'ZEE_8TeV' ,  ['ZEE_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3422]  = [ 'ZTT_8TeV' ,  ['ZTT_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3423]  = [ 'H130GGgluonfusion_8TeV' ,  ['H130GGgluonfusion_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3424]  = [ 'PhotonJets_Pt_10_8TeV' ,  ['PhotonJets_Pt_10_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3425]  = [ 'QQH1352T_Tauola_8TeV' ,  ['QQH1352T_Tauola_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]

workflows[3426]  = [ 'MinBias_TuneZ2star_8TeV' ,  ['MinBias_TuneZ2star_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3427]  = [ 'WM_8TeV' ,  ['WM_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3428]  = [ 'ZMM_8TeV' ,  ['ZMM_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]

workflows[3429]  = [ 'ADDMonoJet_d3MD3_8TeV' ,  ['ADDMonoJet_d3MD3_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3430]  = [ 'ZpMM_8TeV' ,  ['ZpMM_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3431]  = [ 'WpM_8TeV' ,  ['WpM_UPG2019_8','DIGIUP19','RECOUP19','HARVESTUP19']]

#std wf @14TeV
#workflows[3432]  = [ 'TTbarLepton_14TeV' ,  ['TTbarLepton_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']] #no gen fragment

workflows[3433]  = [ 'Wjet_Pt_80_120_14TeV' ,  ['Wjet_Pt_80_120_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3434]  = [ 'Wjet_Pt_3000_3500_14TeV' ,  ['Wjet_Pt_3000_3500_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3435]  = [ 'LM1_sfts_14TeV' ,  ['LM1_sfts_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]

workflows[3436]  = [ 'QCD_Pt_3000_3500_14TeV' ,  ['QCD_Pt_3000_3500_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
#workflows[3437]  = [ 'QCD_Pt_600_800_14TeV' ,  ['QCD_Pt_600_800_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']] #no gen fragment
workflows[3438]  = [ 'QCD_Pt_80_120_14TeV' ,  ['QCD_Pt_80_120_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]

workflows[3439]  = [ 'Higgs200ChargedTaus_14TeV' ,  ['Higgs200ChargedTaus_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3440]  = [ 'JpsiMM_14TeV' ,  ['JpsiMM_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3441]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3442]  = [ 'WE_14TeV' ,  ['WE_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3443]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3444]  = [ 'ZTT_14TeV' ,  ['ZTT_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3445]  = [ 'H130GGgluonfusion_14TeV' ,  ['H130GGgluonfusion_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3446]  = [ 'PhotonJets_Pt_10_14TeV' ,  ['PhotonJets_Pt_10_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3447]  = [ 'QQH1352T_Tauola_14TeV' ,  ['QQH1352T_Tauola_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]

workflows[3448]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3449]  = [ 'WM_14TeV' ,  ['WM_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]
workflows[3450]  = [ 'ZMM_14TeV' ,  ['ZMM_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]

#workflows[3451]  = [ 'ADDMonoJet_d3MD3_14TeV' ,  ['ADDMonoJet_d3MD3_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]#no gen fragment
#workflows[3452]  = [ 'ZpMM_14TeV' ,  ['ZpMM_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]#no gen fragment
#workflows[3453]  = [ 'WpM_14TeV' ,  ['WpM_UPG2019_14','DIGIUP19','RECOUP19','HARVESTUP19']]#no gen fragment

############################################################################################################
#aging WFs 2017
workflows[5000]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017_DES','DIGIUP17DES','RECOUP17DES','HARVESTUP17DES']]
workflows[5010]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017_STAR','DIGIUP17STAR','RECOUP17STAR','HARVESTUP17STAR']]
workflows[5001]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017_300','DIGIUP17300','RECOUP17300','HARVESTUP17300']]
workflows[5002]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017_500','DIGIUP17500','RECOUP17500','HARVESTUP17500']]
workflows[5003]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017_1000','DIGIUP171000','RECOUP171000','HARVESTUP171000']]
workflows[5004]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017_3000','DIGIUP173000','RECOUP173000','HARVESTUP173000']]
workflows[5005]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017_1000TkId','DIGIUP171000TkId','RECOUP171000TkId','HARVESTUP171000TkId']]

workflows[5100]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017PU20_DES','DIGIPUUP17DES','RECOPUUP17DES','HARVESTUP17DES']]
workflows[5110]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017PU20_STAR','DIGIPUUP17STAR','RECOPUUP17STAR','HARVESTUP17STAR']]
workflows[5101]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017PU20_300','DIGIPUUP17300','RECOPUUP17300','HARVESTUP17300']]
workflows[5102]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017PU20_500','DIGIPUUP17500','RECOPUUP17500','HARVESTUP17500']]
workflows[5103]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2017PU20_1000','DIGIPUUP171000','RECOPUUP171000','HARVESTUP171000']]

workflows[6000]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2017_14_DES','DIGIUP17DES','RECOUP17DES','HARVESTUP17DES']]
workflows[6010]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2017_14_STAR','DIGIUP17STAR','RECOUP17STAR','HARVESTUP17STAR']]
workflows[6001]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2017_14_300','DIGIUP17300','RECOUP17300','HARVESTUP17300']]
workflows[6002]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2017_14_500','DIGIUP17500','RECOUP17500','HARVESTUP17500']]
workflows[6003]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2017_14_1000','DIGIUP171000','RECOUP171000','HARVESTUP171000']]
workflows[6004]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2017_14_3000','DIGIUP173000','RECOUP173000','HARVESTUP173000']]
workflows[6005]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2017_14_1000TkId','DIGIUP171000TkId','RECOUP171000TkId','HARVESTUP171000TkId']]

workflows[7000]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2017_14_DES','DIGIUP17DES','RECOUP17DES','HARVESTUP17DES']]
workflows[7010]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2017_14_STAR','DIGIUP17STAR','RECOUP17STAR','HARVESTUP17STAR']]
workflows[7001]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2017_14_300','DIGIUP17300','RECOUP17300','HARVESTUP17300']]
workflows[7011]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2017_14_300COMP','DIGIUP17300COMP','RECOUP17300COMP','HARVESTUP17300']]
workflows[7002]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2017_14_500','DIGIUP17500','RECOUP17500','HARVESTUP17500']]
workflows[7003]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2017_14_1000','DIGIUP171000','RECOUP171000','HARVESTUP171000']]
workflows[7013]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2017_14_1000COMP','DIGIUP171000COMP','RECOUP171000COMP','HARVESTUP171000']]
workflows[7004]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2017_14_3000','DIGIUP173000','RECOUP173000','HARVESTUP173000']]
workflows[7014]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2017_14_3000COMP','DIGIUP173000COMP','RECOUP173000COMP','HARVESTUP173000']]
workflows[7005]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2017_14_1000TkId','DIGIUP171000TkId','RECOUP171000TkId','HARVESTUP171000TkId']]
workflows[7015]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2017_14_1000COMPTkId','DIGIUP171000COMPTkId','RECOUP171000COMPTkId','HARVESTUP171000TkId']]

workflows[8000]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017_14_DES','DIGIUP17DES','RECOUP17DES','HARVESTUP17DES']]
workflows[8010]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017_14_STAR','DIGIUP17STAR','RECOUP17STAR','HARVESTUP17STAR']]
workflows[8001]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017_14_300','DIGIUP17300','RECOUP17300','HARVESTUP17300']]
workflows[8002]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017_14_500','DIGIUP17500','RECOUP17500','HARVESTUP17500']]
workflows[8003]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017_14_1000','DIGIUP171000','RECOUP171000','HARVESTUP171000']]
workflows[8004]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017_14_3000','DIGIUP173000','RECOUP173000','HARVESTUP173000']]
workflows[8005]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017_14_1000TkId','DIGIUP171000TkId','RECOUP171000TkId','HARVESTUP171000TkId']]
workflows[8100]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017PU20_14_DES','DIGIPUUP17DES','RECOPUUP17DES','HARVESTUP17DES']]
workflows[8100]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017PU20_14_DES','DIGIPUUP17DES','RECOPUUP17DES','HARVESTUP17DES']]
workflows[8110]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017PU20_14_STAR','DIGIPUUP17STAR','RECOPUUP17STAR','HARVESTUP17STAR']]
workflows[8101]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017PU20_14_300','DIGIPUUP17300','RECOPUUP17300','HARVESTUP17300']]
workflows[8102]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017PU20_14_500','DIGIPUUP17500','RECOPUUP17500','HARVESTUP17500']]
workflows[8103]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2017PU20_14_1000','DIGIPUUP171000','RECOPUUP171000','HARVESTUP171000']]

workflows[9000]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2017_DES','DIGIUP17DES','RECOUP17DES','HARVESTUP17DES']]
workflows[9010]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2017_STAR','DIGIUP17STAR','RECOUP17STAR','HARVESTUP17STAR']]
workflows[9001]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2017_300','DIGIUP17300','RECOUP17300','HARVESTUP17300']]
workflows[9002]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2017_500','DIGIUP17500','RECOUP17500','HARVESTUP17500']]
workflows[9003]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2017_1000','DIGIUP171000','RECOUP171000','HARVESTUP171000']]
workflows[9004]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2017_3000','DIGIUP173000','RECOUP173000','HARVESTUP173000']]
workflows[9005]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2017_1000TkId','DIGIUP171000TkId','RECOUP171000TkId','HARVESTUP171000TkId']]
workflows[9100]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2017PU20_DES','DIGIPUUP17DES','RECOPUUP17DES','HARVESTUP17DES']]
workflows[9110]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2017PU20_STAR','DIGIPUUP17STAR','RECOPUUP17STAR','HARVESTUP17STAR']]
workflows[9101]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2017PU20_300','DIGIPUUP17300','RECOPUUP17300','HARVESTUP17300']]
workflows[9102]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2017PU20_500','DIGIPUUP17500','RECOPUUP17500','HARVESTUP17500']]
workflows[9103]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2017PU20_1000','DIGIPUUP171000','RECOPUUP171000','HARVESTUP171000']]

#aging WFs 2019 
workflows[15000]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019_DES','DIGIUP19DES','RECOUP19DES','HARVESTUP19DES']]
workflows[15010]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019_STAR','DIGIUP19STAR','RECOUP19STAR','HARVESTUP19STAR']]
workflows[15001]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019_300','DIGIUP19300','RECOUP19300','HARVESTUP19300']]
workflows[15002]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019_500','DIGIUP19500','RECOUP19500','HARVESTUP19500']]
workflows[15003]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019_1000','DIGIUP191000','RECOUP191000','HARVESTUP191000']]
workflows[15004]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019_3000','DIGIUP193000','RECOUP193000','HARVESTUP193000']]
workflows[15005]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019_1000TkId','DIGIUP191000TkId','RECOUP191000TkId','HARVESTUP191000TkId']]
workflows[15100]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019PU20_DES','DIGIPUUP19DES','RECOPUUP19DES','HARVESTUP19DES']]
workflows[15110]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019PU20_STAR','DIGIPUUP19STAR','RECOPUUP19STAR','HARVESTUP19STAR']]
workflows[15101]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019PU20_300','DIGIPUUP19300','RECOPUUP19300','HARVESTUP19300']]
workflows[15102]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019PU20_500','DIGIPUUP19500','RECOPUUP19500','HARVESTUP19500']]
workflows[15103]  = [ 'FourMuPt1_200' ,  ['FourMuPt1_200_UPG2019PU20_1000','DIGIPUUP191000','RECOPUUP191000','HARVESTUP191000']]

workflows[16000]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2019_14_DES','DIGIUP19DES','RECOUP19DES','HARVESTUP19DES']]
workflows[16010]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2019_14_STAR','DIGIUP19STAR','RECOUP19STAR','HARVESTUP19STAR']]
workflows[16001]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2019_14_300','DIGIUP19300','RECOUP19300','HARVESTUP19300']]
workflows[16002]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2019_14_500','DIGIUP19500','RECOUP19500','HARVESTUP19500']]
workflows[16003]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2019_14_1000','DIGIUP191000','RECOUP191000','HARVESTUP191000']]
workflows[16004]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2019_14_3000','DIGIUP193000','RECOUP193000','HARVESTUP193000']]
workflows[16005]  = [ 'MinBias_TuneZ2star_14TeV' ,  ['MinBias_TuneZ2star_UPG2019_14_1000TkId','DIGIUP191000TkId','RECOUP191000TkId','HARVESTUP191000TkId']]

workflows[17000]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2019_14_DES','DIGIUP19DES','RECOUP19DES','HARVESTUP19DES']]
workflows[17010]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2019_14_STAR','DIGIUP19STAR','RECOUP19STAR','HARVESTUP19STAR']]
workflows[17001]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2019_14_300','DIGIUP19300','RECOUP19300','HARVESTUP19300']]
workflows[17011]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2019_14_300COMP','DIGIUP19300COMP','RECOUP19300COMP','HARVESTUP19300']]
workflows[17002]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2019_14_500','DIGIUP19500','RECOUP19500','HARVESTUP19500']]
workflows[17003]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2019_14_1000','DIGIUP191000','RECOUP191000','HARVESTUP191000']]
workflows[17013]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2019_14_1000COMP','DIGIUP191000COMP','RECOUP191000COMP','HARVESTUP191000']]
workflows[17004]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2019_14_3000','DIGIUP193000','RECOUP193000','HARVESTUP193000']]
workflows[17014]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2019_14_3000COMP','DIGIUP193000COMP','RECOUP193000COMP','HARVESTUP193000']]
workflows[17005]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2019_14_1000TkId','DIGIUP191000TkId','RECOUP191000TkId','HARVESTUP191000TkId']]
workflows[17015]  = [ 'ZEE_14TeV' ,  ['ZEE_UPG2019_14_1000COMPTkId','DIGIUP191000COMPTkId','RECOUP191000COMPTkId','HARVESTUP191000TkId']]

workflows[18000]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019_14_DES','DIGIUP19DES','RECOUP19DES','HARVESTUP19DES']]
workflows[18010]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019_14_STAR','DIGIUP19STAR','RECOUP19STAR','HARVESTUP19STAR']]
workflows[18001]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019_14_300','DIGIUP19300','RECOUP19300','HARVESTUP19300']]
workflows[18002]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019_14_500','DIGIUP19500','RECOUP19500','HARVESTUP19500']]
workflows[18003]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019_14_1000','DIGIUP191000','RECOUP191000','HARVESTUP191000']]
workflows[18004]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019_14_3000','DIGIUP193000','RECOUP193000','HARVESTUP193000']]
workflows[18005]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019_14_1000TkId','DIGIUP191000TkId','RECOUP191000TkId','HARVESTUP191000TkId']]
workflows[18100]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019PU20_14_DES','DIGIPUUP19DES','RECOPUUP19DES','HARVESTUP19DES']]
workflows[18100]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019PU20_14_DES','DIGIPUUP19DES','RECOPUUP19DES','HARVESTUP19DES']]
workflows[18110]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019PU20_14_STAR','DIGIPUUP19STAR','RECOPUUP19STAR','HARVESTUP19STAR']]
workflows[18101]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019PU20_14_300','DIGIPUUP19300','RECOPUUP19300','HARVESTUP19300']]
workflows[18102]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019PU20_14_500','DIGIPUUP19500','RECOPUUP19500','HARVESTUP19500']]
workflows[18103]  = [ 'TTbar_14TeV' ,  ['TTbar_UPG2019PU20_14_1000','DIGIPUUP191000','RECOPUUP191000','HARVESTUP191000']]

workflows[19000]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2019_DES','DIGIUP19DES','RECOUP19DES','HARVESTUP19DES']]
workflows[19010]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2019_STAR','DIGIUP19STAR','RECOUP19STAR','HARVESTUP19STAR']]
workflows[19001]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2019_300','DIGIUP19300','RECOUP19300','HARVESTUP19300']]
workflows[19002]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2019_500','DIGIUP19500','RECOUP19500','HARVESTUP19500']]
workflows[19003]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2019_1000','DIGIUP191000','RECOUP191000','HARVESTUP191000']]
workflows[19004]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2019_3000','DIGIUP193000','RECOUP193000','HARVESTUP193000']]
workflows[19005]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2019_1000TkId','DIGIUP191000TkId','RECOUP191000TkId','HARVESTUP191000TkId']]
workflows[19100]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2019PU20_DES','DIGIPUUP19DES','RECOPUUP19DES','HARVESTUP19DES']]
workflows[19110]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2019PU20_STAR','DIGIPUUP19STAR','RECOPUUP19STAR','HARVESTUP19STAR']]
workflows[19101]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2019PU20_300','DIGIPUUP19300','RECOPUUP19300','HARVESTUP19300']]
workflows[19102]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2019PU20_500','DIGIPUUP19500','RECOPUUP19500','HARVESTUP19500']]
workflows[19103]  = [ 'TenMuE_0_200' ,  ['TenMuE_0_200_UPG2019PU20_1000','DIGIPUUP191000','RECOPUUP191000','HARVESTUP191000']]



#2023 BE
workflows[4100] = ['', ['FourMuPt1_200_UPG2023_BE','RECOUP23_BE']]
workflows[4101] = ['', ['MinBias_TuneZ2star_UPG2023_14_BE','RECOUP23_BE']]
workflows[4102] = ['', ['TTbar_UPG2023_14_BE','RECOUP23_BE']]

#2023 BE5D
workflows[4400] = ['', ['FourMuPt1_200_UPG2023_BE5D','RECOUP23_BE5D']]
workflows[4401] = ['', ['MinBias_TuneZ2star_UPG2023_14_BE5D','RECOUP23_BE5D']]
workflows[4402] = ['', ['TTbar_UPG2023_14_BE5D','RECOUP23_BE5D']]

#2023 BE5D with tracking
workflows[4500] = ['', ['FourMuPt1_200_UPG2023_BE5D','DIGIUP23_BE5D','NRECOUP23_BE5D','HARVESTUPBE5D']]
workflows[4501] = ['', ['MinBias_TuneZ2star_UPG2023_14_BE5D','DIGIUP23_BE5D','NRECOUP23_BE5D','HARVESTUPBE5D']]
workflows[4502] = ['', ['TTbar_UPG2023_14_BE5D','DIGIUP23_BE5D','NRECOUP23_BE5D','HARVESTUPBE5D']]

#2013 Lb6PS
workflows[4200] = ['', ['FourMuPt1_200_UPG2023_LB6','RECOUP23_LB6']]
workflows[4201] = ['', ['MinBias_TuneZ2star_UPG2023_14_LB6','RECOUP23_LB6']]
workflows[4202] = ['', ['TTbar_UPG2023_14_LB6','RECOUP23_LB6']]


#2013 Lb4LPS_2L2S
workflows[4300] = ['', ['FourMuPt1_200_UPG2023_LB4','RECOUP23_LB4']]
workflows[4301] = ['', ['MinBias_TuneZ2star_UPG2023_14_LB4','RECOUP23_LB4']]
workflows[4302] = ['', ['TTbar_UPG2023_14_LB4','RECOUP23_LB4']]

#Fastsim
workflows[40000] = ['TTbar_14TeV', ['TTbarFSP1','HARVESTFSP1']]
workflows[40001] = ['SingleMuPt10', ['SingleMuPt10FSP1','HARVESTFSP1']]
workflows[40002] = ['SingleMuPt100', ['SingleMuPt100FSP1','HARVESTFSP1']]
workflows[40003] = ['MinBias_14TeV', ['MinBias_TuneZ2starFSP1','HARVESTFSP1']]

workflows[40004] = ['TTbar_8TeV', ['TTbar8FSP1','HARVESTFSP1']]
workflows[40005] = ['MinBias_8TeV', ['MinBias_TuneZ2star8FSP1','HARVESTFSP1']]

workflows[40006]=['TTbar_8TeV',['TTbar8FSPUP1','HARVESTFSP1']]



workflows[50001] = ['TTbar_14TeV', ['TTbarFSP2','HARVESTFSP2']]
workflows[50002] = ['SingleMuPt10', ['SingleMuPt10FSP2','HARVESTFSP2']]
workflows[50003] = ['SingleMuPt100', ['SingleMuPt100FSP2','HARVESTFSP2']]
workflows[50004] = ['MinBias_14TeV', ['MinBias_TuneZ2starFSP2','HARVESTFSP2']]

workflows[50005] = ['TTbar_8TeV', ['TTbar8FSP2','HARVESTFSP2']]
workflows[50006] = ['MinBias_8TeV', ['MinBias_TuneZ2star8FSP2','HARVESTFSP2']]

workflows[50007] = ['TTbar_8TeV', ['TTbar8FSPUP2','HARVESTFSP2']]

workflows[60001] = ['TTbar_14TeV', ['TTbarFSP2Forw','HARVESTFSP2Forw']]
workflows[60002] = ['SingleMuPt10', ['SingleMuPt10FSP2Forw','HARVESTFSP2Forw']]
workflows[60003] = ['SingleMuPt100', ['SingleMuPt100FSP2Forw','HARVESTFSP2Forw']]
workflows[60004] = ['MinBias_14TeV', ['MinBias_TuneZ2starFSP2Forw','HARVESTFSP2Forw']]


