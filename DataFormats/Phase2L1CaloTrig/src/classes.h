/// ////////////////////////////////////////
/// Stacked Tracker Simulations          ///
/// ////////////////////////////////////////

#include "DataFormats/Common/interface/Wrapper.h"


/*********************/
/** L1 CALO TRIGGER **/
/*********************/

#include "DataFormats/Phase2L1CaloTrig/interface/L1EGCrystalCluster.h"
#include "DataFormats/Phase2L1CaloTrig/interface/L1CaloCluster.h"

namespace DataFormats_Phase2L1CaloTrigger {
  L1CaloCluster cluster;
  edm::Wrapper<L1CaloCluster> w_cluster;

  std::vector<L1CaloCluster> caloClusterCollection;
  edm::Wrapper<std::vector<L1CaloCluster> > w_caloClusterCollection;

};

namespace {
  namespace {

    L1CaloCluster cluster;
    edm::Wrapper<L1CaloCluster> w_cluster;
    
    std::vector<L1CaloCluster> caloClusterCollection;
    edm::Wrapper<std::vector<L1CaloCluster> > w_caloClusterCollection;
    
    l1slhc::L1EGCrystalCluster                       egcrystalcluster;
    std::vector<l1slhc::L1EGCrystalCluster>         l1egcrystalclustervec;
    l1slhc::L1EGCrystalClusterCollection            l1egcrystalclustercoll;
    edm::Wrapper<l1slhc::L1EGCrystalClusterCollection>   wl1egcrystalclustercoll;
    
  }
}

