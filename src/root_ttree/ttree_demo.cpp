// ttree_demo.cpp
#include <TFile.h>
#include <TTree.h>
#include <vector>
#include <random>
#include <iostream>

int main() {
  TFile f("data/ttree_demo.root","RECREATE");
  TTree tree("Events","Demo TTree");

  int run=1, evt=0;
  std::vector<float> px;
  tree.Branch("run",&run);
  tree.Branch("evt",&evt);
  tree.Branch("px",&px);

  std::mt19937 rng(42);
  std::normal_distribution<float> dist(0.0,1.0);

  for (evt=0; evt<1000; ++evt) {
    px.clear();
    int n = (evt % 5) + 1;
    for (int i=0;i<n;++i) px.push_back(dist(rng));
    tree.Fill();
  }

  tree.Write();
  f.Close();
  std::cout<<"Wrote data/ttree_demo.root\n";
  return 0;
}

