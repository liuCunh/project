#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

typedef struct {
	int pro_id = 0;       //进程的ID
	int address;           //内存块的起始地址
	int id;                   //内存块的编号
	bool flag;              //内存块是否被占用（false表示未被占用）
	int length;             //内存块的长度
}MemBlock;

void InitBlock(int num, vector<MemBlock>& block) {
	block[0].address = 0;
	for (int i = 0; i < num; i++) {
		if (i > 0)
			block[i].address = block[i - 1].address + block[i - 1].length;
		block[i].id = i + 1;
		block[i].flag = false;
		block[i].length = int(pow(2, i));
	}
}

bool comp0(MemBlock B1, MemBlock B2) {
	return B1.address < B2.address;
}
 
void PrintBlock(vector<MemBlock>& Block) {
	sort(Block.begin(), Block.end(), comp0);
	int num = Block.size();
	cout << "进程编号";
	cout.width(18); cout << "内存块编号";
	cout.width(26); cout << "内存块起始地址";
	cout.width(18); cout << "内存块长度";
	cout.width(26); cout << "内存块占用情况" << endl;
	for (int i = 0; i < num; i++) {
		cout << Block[i].pro_id;
		cout.width(16); cout << Block[i].id;
		cout.width(16); cout << Block[i].address;
		cout.width(16); cout << Block[i].length;
		cout.width(16); cout << Block[i].flag << endl;
	}
}

bool comp1(MemBlock B1, MemBlock B2) {
	return B1.id < B2.id;
}

void First_Fit(vector<MemBlock>& block) {
	MemBlock mb;
	mb.flag = true;
	cout << "输入进程的ID:"; cin >> mb.pro_id;
	cout << "输入进程所需的存储空间:"; cin >> mb.length;
	sort(block.begin(), block.end(), comp1);
	int num = block.size();
	for (int i = 0; i < num; i++) {
		if (block[i].length >= mb.length && !block[i].flag) {
			if (block[i].length == mb.length) {
				block[i].pro_id = mb.pro_id;
				block[i].flag = true;
				return;
			}
			else {
				mb.id = block[i].id;
				mb.address = block[i].address;
				block[i].address += mb.length;
				block[i].length -= mb.length;
				block.insert(block.begin() + i, mb);
				return;
			}
		}
	}
}

bool comp2(MemBlock B1, MemBlock B2) {
	return B1.length < B2.length;
}

void Best_Fit(vector<MemBlock>& block) {
	MemBlock mb;
	mb.flag = true;
	cout << "输入进程的ID:"; cin >> mb.pro_id;
	cout << "输入进程所需的存储空间:"; cin >> mb.length;
	sort(block.begin(), block.end(), comp2);
	int num = block.size();
	for (int i = 0; i < num; i++) {
		if (block[i].length >= mb.length && !block[i].flag) {
			if (block[i].length == mb.length) {
				block[i].pro_id = mb.pro_id;
				block[i].flag = true;
				return;
			}
			else {
				mb.id = block[i].id;
				mb.address = block[i].address;
				block[i].address += mb.length;
				block[i].length -= mb.length;
				block.insert(block.begin() + i, mb);
				return;
			}
		}
	}
}
bool comp3(MemBlock B1, MemBlock B2) {
	return B1.length > B2.length;
}

void Worst_Fit(vector<MemBlock>& block) {
	MemBlock mb;
	mb.flag = true;
	cout << "输入进程的ID:"; cin >> mb.pro_id;
	cout << "输入进程所需的存储空间:"; cin >> mb.length;
	sort(block.begin(), block.end(), comp3);
	int num = block.size();
	for (int i = 0; i < num; i++) {
		if (block[i].length >= mb.length && !block[i].flag) {
			if (block[i].length == mb.length) {
				block[i].flag = true;
				block[i].pro_id = mb.pro_id;
				return;
			}
			else {
				mb.id = block[i].id;
				mb.address = block[i].address;
				block[i].address += mb.length;
				block[i].length -= mb.length;
				block.insert(block.begin() + i, mb);
				return;
			}
		}
	}
}

void Recycle(vector<MemBlock>& block, int pro_id, int id) {
	int num = block.size();
	for (int i = 0; i < num; i++) {
		if (block[i].pro_id == pro_id) {
			if (i == 0) {
				if (!block[i + 1].flag && block[i + 1].id == id) {
					block[i + 1].address = block[i].address;
					block[i + 1].length += block[i].length;
					block.erase(block.begin());
				}
				else {
					block[i].flag = false;
					block[i].pro_id = 0;
				}
				return;
			}
			else if (i == num - 1) {
				if (!block[i - 1].flag && block[i - 1].id == id) {
					block[i - 1].length += block[i].length;
					block.erase(block.begin() + i);
				}
				else {
					block[i].flag = false;
					block[i].pro_id = 0;
				}
				return;
			}
			else {
				if (!block[i - 1].flag && block[i - 1].id == id) {
					if (!block[i + 1].flag && block[i + 1].id == id) {
						block[i - 1].length += block[i].length + block[i + 1].length;
						block.erase(block.begin() + i);
						block.erase(block.begin() + i);
					}
					else {
						block[i - 1].length += block[i].length;
						block.erase(block.begin() + i);
					}
				}
				else {
					if (!block[i + 1].flag && block[i + 1].id == id) {
						block[i + 1].address = block[i].address;
						block[i + 1].length += block[i].length;
						block.erase(block.begin() + i);
					}
					else {
						block[i].flag = false;
						block[i].pro_id = 0;
					}
				}
				return;
			}
		}
	}
}
void ShowMenu() {
	cout << "*************************************************************************************" << endl;
	cout << "\t1-首次适应\t";
	cout << "\t2-最佳适应\t";
	cout << "\t3-最坏适应\t";
	cout << "\t4-退出\t" << endl;
}

void Doing(vector<MemBlock>& block) {
	while (1) {
		ShowMenu();
		int select;
		cout << "输入要调用的内存块分配算法:"; cin >> select;
		switch (select) {
		case 1:First_Fit(block);
			break;
		case 2:Best_Fit(block);
			break;
		case 3:Worst_Fit(block);
			break;
		case 4:cout << "调用结束";
			return;
		}
		PrintBlock(block);
		cout << "是否需要回收内存空间(0表示否，1表示是)："; cin >> select;
		if (select){
			int pro_id, id;
			cout << "输入需要回收的进程的ID："; cin >> pro_id;
			cout << "输入进程所处的内存块的编号："; cin >> id;
			Recycle(block, pro_id, id);
			PrintBlock(block);
		}
	}
}

int main() {
	int nums;
	cout << "输入内存块的个数："; cin >> nums;
	vector<MemBlock> block(nums);
	cout << "初始化内存块:" << endl;
	InitBlock(nums, block);
	PrintBlock(block);
	Doing(block);
	int cnt = 0;
	for (int i = 0; i < block.size(); i++) {
		if (block[i].flag) {
			cout << "第" << cnt + 1 << "次内存回收" << endl;
			Recycle(block, block[i].pro_id, block[i].id);
			PrintBlock(block);
			cout << endl;
		}
	}
	system("pause");
}
