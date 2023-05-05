#include <iostream>
#include <random>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <limits>
#include <chrono>
using namespace std;
vector<int> ReadIdFile(string Path);
void GenerateClonePairs(vector<int> functionIDs, vector<pair<int, int>> knownPairs);
void WriteToCSV(const vector<std::pair<int, int>>& pairs);
std::vector<int> getRandomSample(const vector<int>& inputVector, size_t sampleSize);
bool CheckIfKnownPair(vector<int> samplefuncIDs, int i, int j, vector<pair<int, int>> knownPairs);
vector<pair<int, int>> ReadBCBFile();
int main(){
	//std::cout << "It works!" << std::endl;
	vector<int> outputVec=ReadIdFile("MethodsContainingTypes1_3.csv");
	vector<pair<int, int>> knownPairs = ReadBCBFile();
	std::cout << "There are a total of: " << outputVec.size() << " functions" << std::endl; 
	auto startTime = chrono::high_resolution_clock::now();
	GenerateClonePairs(outputVec, knownPairs);
	auto endTime=chrono::high_resolution_clock::now();
	auto duration = chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime);
	std::cout << "Execution time: " << duration.count() << " milliseconds" << std::endl;
	return 0;
}
void GenerateClonePairs(vector<int> functionIDs, vector<pair<int, int>> knownPairs){
	vector<int> sampleFuncIDs = functionIDs;
	int myVecSize= sampleFuncIDs.size();
	std::vector<std::pair<int, int>> pairs;
	std::cout << "reserve memory..." << std::endl;
	//std::cout << std::numeric_limits<size_t>::max() << std::endl;
	pairs.reserve(myVecSize * (myVecSize - 1) / 2);  // Reserve memory for all pairs
	std::cout << "start..." << std::endl;
	for (int i =0; i < myVecSize; i++){
		if(i % 1 == 0 ){
			std::cout << i;
			std::cout << " out of ";
			std::cout << myVecSize << std::endl;
		}
		for(int j = i+1; j < myVecSize; j++){
			if (!CheckIfKnownPair(sampleFuncIDs, i, j, knownPairs)) {
				pairs.emplace_back(sampleFuncIDs[i], sampleFuncIDs[j]);
			}
		}
	}

	WriteToCSV(pairs);

}
bool CheckIfKnownPair(vector<int> samplefuncIDs, int i, int j, vector<pair<int, int>> knownPairs) {
	for (pair<int, int> pair : knownPairs) {
		if ((pair.first == samplefuncIDs[i] && pair.second == samplefuncIDs[j]) || (pair.second == samplefuncIDs[i] && pair.first == samplefuncIDs[j])) {
			return true;
		}
	}
	return false;
}
void WriteToCSV(const vector<std::pair<int, int>>& pairs){
	string filename= "OutputExtraNonPairs.csv";
	ofstream file(filename);
	if (!file){
		std::cerr << "failed to open the file." << std::endl;
		return;
	}
	file << ",id1, id2, label" << "\n";
	int index=0;
	for(const auto& pair : pairs){
		file << index << "," << pair.first << "," << pair.second << "," << "0" << "\n";
		index+=1;
	}
	file.close();
}

vector<int> ReadIdFile(string path){
	ifstream file(path);
	if(!file){
		std::cerr << "Failed!" << std::endl;
	}
	std::cout << "success!" << std::endl;
	
	vector<int> numbers;
	int currNumber;
	while(file >> currNumber){
		numbers.push_back(currNumber);
	}
	file.close();
	return numbers;
}
vector<pair<int, int>> ReadBCBFile() {
	ifstream file("bcb_clonePairs.csv"); // Replace "data.csv" with your CSV file path

	if (!file) {
		cout << "Failed to open the file." << endl;
	}

	vector<pair<int, int>> numberPairs; // Vector to store the number pairs

	string line;
	bool isFirstLine = true; // Flag to track the first line


	while (getline(file, line)) {
		if (isFirstLine) {
			isFirstLine = false;
			continue;
		}
		
		stringstream ss(line);
		string token;

		while (getline(ss, token, ',')) { // Assuming comma-separated values
			int num1, num2;
			istringstream(token) >> num1;

			if (getline(ss, token, ',')) {
				istringstream(token) >> num2;
				numberPairs.emplace_back(num1, num2);
			}
			else {
				cout << "Invalid number pair format in the CSV file." << endl;
				break;
			}
		}
	}
	return numberPairs;
}
/*
vector<int> getRandomSample(const std::vector<int>& inputVector, size_t sampleSize) {
	if (sampleSize >= inputVector.size()) {
		return inputVector;
	}
	vector<int> shuffledVector = inputVector;
	//create random number generator
	random_device rd;
	mt19937 generator(rd());
	//shuffle
	shuffle(shuffledVector.begin(), shuffledVector.end(), generator);

	//extract
	vector<int> sample(shuffledVector.begin(), shuffledVector.begin() + sampleSize);
	
	return sample;
}
*/
