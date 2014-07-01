// -*- C++ -*-
//
// Package:    MyPatMatchingTask2
// Class:      MyPatMatchingTask2
// 
/**\class MyPatMatchingTask2 MyPatMatchingTask2.cc UserCode/MyPatMatching/src/MyPatMatchingTask2.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Phat Srimanobhas,40 1-A11,+41227671646,
//         Created:  Thu Nov 24 21:39:38 CET 2011
// $Id: MyPatMatchingTask2.cc,v 1.2 2012/11/30 23:29:10 srimanob Exp $
//
//


// system include files
#include <memory>
#include <map>
#include <string>


// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "Math/VectorUtil.h"
#include "TH1.h"
#include "TH2.h"
#include "TTree.h"
#include "TLorentzVector.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Math/interface/deltaPhi.h"

//
// class declaration
//

class MyPatMatchingTask2 : public edm::EDAnalyzer {
public:
  explicit MyPatMatchingTask2(const edm::ParameterSet&);
  ~MyPatMatchingTask2();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  
private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  
  // ----------member data ---------------------------
  std::map<std::string,TH1F*> histContainer_;

  // input tags
  edm::InputTag muonSrc_;

  //how many muons have no match
  unsigned int noMatch;
  unsigned int yesMatch;
  unsigned int decayInFlight;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
MyPatMatchingTask2::MyPatMatchingTask2(const edm::ParameterSet& iConfig)
{
  //
  muonSrc_  = iConfig.getUntrackedParameter<edm::InputTag>("muonSrc");
  
  //
  edm::Service<TFileService> fs;

  // book histograms:
  // Example: DR_
  histContainer_["DR_defaultMatch"]=fs->make<TH1F>("DR_defaultMatch", "DR_defaultMatch", 100, 0., 0.02);
  histContainer_["DR_status1Match"]=fs->make<TH1F>("DR_status1Match", "DR_status1Match", 100, 0., 0.02);
  histContainer_["DR_status3Match"]=fs->make<TH1F>("DR_status3Match", "DR_status3Match", 100, 0., 0.02);
  // Exercise: DPt_
  histContainer_["DPt_defaultMatch"]=fs->make<TH1F>("DPt_defaultMatch", "DPt_defaultMatch", 10, 0,  1.2);
  histContainer_["DPt_status1Match"]=fs->make<TH1F>("DPt_status1Match", "DPt_status1Match", 10, 0,  1.2);
  histContainer_["DPt_status3Match"]=fs->make<TH1F>("DPt_status3Match", "DPt_status3Match", 10, 0,  1.2);
  
  //
  noMatch = 0;
  yesMatch = 0;
  decayInFlight = 0;
}


MyPatMatchingTask2::~MyPatMatchingTask2(){}

//
// member functions
//

// ------------ method called for each event  ------------
void
MyPatMatchingTask2::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;
   using namespace pat;
   using namespace std; 

   // get muon collection
   edm::Handle<edm::View<pat::Muon> > muonCollection;
   iEvent.getByLabel(muonSrc_,muonCollection);
   
   //-------------------------------------------------------------------------
   // Task 1:
   //
   // Example:
   //
   /*
   for(edm::View<pat::Muon>::const_iterator muon=muonCollection->begin(); muon!=muonCollection->end(); ++muon){
   for(unsigned int i = 0 ; i < muon->genParticleRefs().size() ; ++i ){
   switch( muon->genParticle(i)->status() ){
   case 1:
   histContainer_["DR_status1Match"]->Fill( ROOT::Math::VectorUtil::DeltaR(muon->p4() , muon->genParticle(i)->p4() ) ); 
   histContainer_["DPt_status1Match"]->Fill(muon->pt() - muon->genParticle(i)->pt() );
   break;
   case 3:
   histContainer_["DR_status3Match"]->Fill( ROOT::Math::VectorUtil::DeltaR(muon->p4() , muon->genParticle(i)->p4() ) );
   histContainer_["DPt_status3Match"]->Fill(muon->pt() - muon->genParticle(i)->pt() ); 
   break;
   default:
   histContainer_["DR_defaultMatch"]->Fill( ROOT::Math::VectorUtil::DeltaR(muon->p4() , muon->genParticle(i)->p4() ) ); 
   histContainer_["DPt_defaultMatch"]->Fill(muon->pt() - muon->genParticle(i)->pt() );
   break;
   }
   }
   }
   */
   
   // Exercise: Practise how to use genParticleByID
   for(edm::View<pat::Muon>::const_iterator muon=muonCollection->begin(); muon!=muonCollection->end(); ++muon){
     if(muon->genParticleById(0,1).isNonnull() ){
       histContainer_["DR_status1Match"]->Fill( ROOT::Math::VectorUtil::DeltaR(muon->p4() , (muon->genParticleById(0,1))->p4() ) ); 
       histContainer_["DPt_status1Match"]->Fill(muon->pt() - (muon->genParticleById(0,1) )->pt() );
     }
     if(muon->genParticleById(0,3).isNonnull() ){
       histContainer_["DR_status3Match"]->Fill( ROOT::Math::VectorUtil::DeltaR(muon->p4() , (muon->genParticleById(0,3))->p4() ) );
       histContainer_["DPt_status3Match"]->Fill(muon->pt() - (muon->genParticleById(0,3) )->pt() );
     }
     if(muon->genParticleById(0,-1).isNonnull() ){
       histContainer_["DR_defaultMatch"]->Fill( ROOT::Math::VectorUtil::DeltaR(muon->p4() , (muon->genParticleById(0,-1))->p4() ) ); 
       histContainer_["DPt_defaultMatch"]->Fill(muon->pt() - (muon->genParticleById(0,-1) )->pt() );
     }
     //How to check noMatch?
     if(muon->genParticleById(0,1).isNull() && muon->genParticleById(0,3).isNull() && muon->genParticleById(0,-1).isNull()) noMatch++;
     else if(muon->genParticleById(0,1).isNull() && muon->genParticleById(0,3).isNull() && muon->genParticleById(0,-1).isNonnull())decayInFlight++;
     else yesMatch++;
   }
   
}


// ------------ method called once each job just before starting event loop  ------------
void 
MyPatMatchingTask2::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MyPatMatchingTask2::endJob() 
{
  std::cout<<"Match = "<<yesMatch
	   <<", Not match = "<<noMatch
	   <<", decayInFlight = "<<decayInFlight
	   <<std::endl;
}

// ------------ method called when starting to processes a run  ------------
void 
MyPatMatchingTask2::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
MyPatMatchingTask2::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
MyPatMatchingTask2::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
MyPatMatchingTask2::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MyPatMatchingTask2::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MyPatMatchingTask2);
