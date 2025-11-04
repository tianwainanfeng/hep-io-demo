// rntuple_demo.cpp
#include <ROOT/RDataFrame.hxx>
#include <ROOT/RNTupleDS.hxx>
#include <TCanvas.h>
#include <TH1D.h>

int main() {
    // Read an RNTuple dataset (assuming file.root contains "myntuple")
    auto df = ROOT::RDF::RNTupleDS("myntuple", "file.root");
    ROOT::RDataFrame rdf(*df);

    rdf.Describe().Print();

    auto h = rdf.Histo1D<double>({"h", "Example", 100, 0, 10}, "some_column");
    h->Draw();

    return 0;
}

