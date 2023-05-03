#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
std::vector<int> ReadFile(std::string Path);
void GenerateClonePairs(std::vector<int> functionIDs);
void WriteToCSV(const std::vector<std::pair<int, int>>& pairs);
int main(){
	std::cout << "It works!" << std::endl;
	std::vector<int> outputVec=ReadFile("IdsOnly.txt");
	//for (int i =0; i < 10; i++){
	//	std::cout << outputVec[i] << std::endl;
	//}
	std::cout << "There are a total of: " << outputVec.size() << " functions" << std::endl; 
	GenerateClonePairs(outputVec);
	return 0;
}
void GenerateClonePairs(std::vector<int> functionIDs){
	std::vector<std::pair<int, int>> pairs;
	int myVecSize= 10000;
	for (int i =0; i < myVecSize; i++){
		if(i % 1000 == 0 ){
			std::cout << i;
			std::cout << " out of ";
			std::cout << myVecSize << std::endl;
		}
		for(int j = i+1; j < myVecSize; j++){
			pairs.emplace_back(functionIDs[i], functionIDs[j]);
		}
	}

	WriteToCSV(pairs);

}
void WriteToCSV(const std::vector<std::pair<int, int>>& pairs){
	std::string filename= "OutputPairs.csv";
	std::ofstream file(filename);
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

std::vector<int> ReadFile(std::string path){
	std::ifstream file(path);
	if(!file){
		std::cerr << "Failed!" << std::endl;
	}
	std::cout << "success!" << std::endl;
	
	std::vector<int> numbers;
	int currNumber;
	while(file >> currNumber){
		numbers.push_back(currNumber);
	}
	file.close();
	return numbers;
}
