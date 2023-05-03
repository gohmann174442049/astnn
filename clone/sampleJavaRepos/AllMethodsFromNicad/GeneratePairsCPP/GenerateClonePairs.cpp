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
vector<int> ReadFile(string Path);
void GenerateClonePairs(vector<int> functionIDs);
void WriteToCSV(const vector<std::pair<int, int>>& pairs);
std::vector<int> getRandomSample(const vector<int>& inputVector, size_t sampleSize);
int main(){
	std::cout << "It works!" << std::endl;
	vector<int> outputVec=ReadFile("IdsOnly.txt");
	std::cout << "There are a total of: " << outputVec.size() << " functions" << std::endl; 
	auto startTime = chrono::high_resolution_clock::now();
	GenerateClonePairs(outputVec);
	auto endTime=chrono::high_resolution_clock::now();
	auto duration = chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime);
	std::cout << "Execution time: " << duration.count() << " milliseconds" << std::endl;
	return 0;
}
void GenerateClonePairs(vector<int> functionIDs){
	vector<int> sampleFuncIDs = getRandomSample(functionIDs, 775000);
	int myVecSize= sampleFuncIDs.size();
	std::vector<std::pair<int, int>> pairs;
	std::cout << "reserve memory..." << std::endl;
	//std::cout << std::numeric_limits<size_t>::max() << std::endl;
	//pairs.reserve(myVecSize * (myVecSize - 1) / 2);  // Reserve memory for all pairs
	std::cout << "start..." << std::endl;
	for (int i =0; i < myVecSize; i++){
		if(i % 10000 == 0 ){
			std::cout << i;
			std::cout << " out of ";
			std::cout << myVecSize << std::endl;
		}
		for(int j = i+1; j < myVecSize; j++){
			pairs.emplace_back(sampleFuncIDs[i], sampleFuncIDs[j]);
		}
	}

	WriteToCSV(pairs);

}
void WriteToCSV(const vector<std::pair<int, int>>& pairs){
	string filename= "OutputPairs.csv";
	ofstream file(filename);
	if (!file){
		std::cerr << "failed to open the file." << std::endl;
		return;
	}
	file << ",id1, id2, label" << "\n";
	int index=0;
	for(const auto& pair : pairs){
		file << index << "," << pair.first << "," << pair.second << "," << "-1" << "\n";
		index+=1;
	}
	file.close();
}

vector<int> ReadFile(string path){
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
